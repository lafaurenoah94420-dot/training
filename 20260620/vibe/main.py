"""Nahla Arena — esquive les humains qui veulent la caresser."""

import json
import math
import random
import struct
import sys
from pathlib import Path

import pygame

# --- Fenêtre (ce que tu vois) ---
WIDTH, HEIGHT = 1280, 720
# --- Monde (la vraie map, plus grande) ---
WORLD_WIDTH, WORLD_HEIGHT = 3200, 2200
FPS = 60
TITLE = "Nahla Arena"

ASSETS = Path(__file__).parent
NAHLA_IMG = ASSETS / "nahla_head.png"
HIGHSCORE_FILE = ASSETS / "highscore.json"

# --- États ---
MENU = "menu"
PLAYING = "playing"
OVER = "over"

# --- Couleurs ---
BG = (42, 36, 48)
FLOOR = (58, 50, 62)
FLOOR_ALT = (52, 46, 56)
WALL = (28, 24, 32)
TEXT = (245, 238, 225)
MUTED = (160, 150, 165)
ACCENT = (255, 168, 72)
DANGER = (235, 75, 75)
OK = (100, 210, 140)
CLAW_C = (255, 120, 90)

NAHLA_SPEED = 5.2
NAHLA_R = 34
HIT_R = 26

CLAW_RANGE = 130
CLAW_COOLDOWN_MS = 1500
CLAW_KNOCKBACK = 16
CLAW_FX_MS = 220

HUMAN_TYPES = {
    "malik": {"name": "Malik", "color": (255, 200, 120), "speed": 2.4, "r": 22},
    "kays": {"name": "Kays", "color": (140, 190, 255), "speed": 2.0, "r": 20},
    "noah": {"name": "Noah", "color": (180, 255, 160), "speed": 2.8, "r": 18},
    "maman": {"name": "Maman", "color": (255, 160, 220), "speed": 1.1, "r": 44},
}

PHRASES = {
    "malik": [
        "Viens là !",
        "NAHLA !",
        "Je t'aime !",
        "Bisou bisou !",
        "Attends-moi !",
    ],
    "kays": [
        "Hé le chat !",
        "Laisse-toi faire.",
        "T'es mignonne.",
        "Bouge pas.",
        "C'est pour ton bien.",
    ],
    "noah": [
        "Nahla !",
        "Ma puce !",
        "Caresses !",
        "Viens ici !",
        "T'es trop belle.",
    ],
    "maman": [
        "Oh mon chaton !",
        "Ma puce adorée !",
        "Viens ma chérie !",
        "Le plus beau chat !",
        "Maman t'aime !",
    ],
}

MOVE_LEFT = (pygame.K_LEFT, pygame.K_q, pygame.K_a)
MOVE_RIGHT = (pygame.K_RIGHT, pygame.K_d)
MOVE_UP = (pygame.K_UP, pygame.K_z, pygame.K_w)
MOVE_DOWN = (pygame.K_DOWN, pygame.K_s)

PLAY_MARGIN = 64
PHRASE_MS = 2800
MAMAN_SPAWN_CHANCE = 0.22
MAMAN_GUARANTEE_WAVE = 3
SPAWN_INTERVAL_START_MS = 3200
SPAWN_INTERVAL_MIN_MS = 650
MAX_HUMANS_START = 5
MAX_HUMANS_CAP = 14


def load_font(size, bold=False):
    try:
        return pygame.font.SysFont("Arial", size, bold=bold)
    except Exception:
        return pygame.font.Font(None, size)


def load_highscore():
    if HIGHSCORE_FILE.exists():
        try:
            data = json.loads(HIGHSCORE_FILE.read_text(encoding="utf-8"))
            return int(data.get("best", 0))
        except (json.JSONDecodeError, ValueError, OSError):
            pass
    return 0


def save_highscore(best):
    try:
        HIGHSCORE_FILE.write_text(
            json.dumps({"best": best}, indent=2),
            encoding="utf-8",
        )
    except OSError:
        pass


class SoundBank:
    """Sons générés en code."""

    def __init__(self):
        if not pygame.mixer.get_init():
            pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
        self.enabled = True
        self.sfx = {
            "spawn": self._meow(),
            "claw": self._scratch(),
            "caught": self._non(),
            "new_record": self._chime([520, 780, 1040], 160, 0.28),
        }

    def _pack(self, samples):
        return pygame.mixer.Sound(
            buffer=b"".join(struct.pack("<hh", s, s) for s in samples)
        )

    def _tone(self, freq, ms, vol, sweep_end=None):
        rate = 22050
        n = int(rate * ms / 1000)
        out = []
        for i in range(n):
            t = i / rate
            f = freq + (sweep_end - freq) * (i / n) if sweep_end else freq
            env = min(1.0, i / (rate * 0.005)) * (1 - i / n)
            v = math.sin(2 * math.pi * f * t)
            out.append(int(32767 * vol * env * v))
        return self._pack([max(-32767, min(32767, s)) for s in out])

    def _chime(self, freqs, ms, vol):
        rate = 22050
        n = int(rate * ms / 1000)
        out = [0] * n
        for freq in freqs:
            for i in range(n):
                t = i / rate
                env = min(1.0, i / (rate * 0.008)) * (1 - i / n)
                out[i] += int(
                    32767 * vol * env * math.sin(2 * math.pi * freq * t) / len(freqs)
                )
        return self._pack([max(-32767, min(32767, s)) for s in out])

    def _meow(self):
        rate = 22050
        ms = 180
        n = int(rate * ms / 1000)
        out = []
        for i in range(n):
            t = i / rate
            f = 780 - 300 * (i / n)
            env = math.sin(math.pi * i / n) ** 1.3
            out.append(int(32767 * 0.22 * env * math.sin(2 * math.pi * f * t)))
        return self._pack(out)

    def _scratch(self):
        rate = 22050
        ms = 140
        n = int(rate * ms / 1000)
        out = []
        for i in range(n):
            env = (1 - i / n) ** 1.2
            v = random.uniform(-1, 1) * env
            v += 0.5 * math.sin(2 * math.pi * 180 * i / rate)
            out.append(int(32767 * 0.35 * v))
        return self._pack([max(-32767, min(32767, s)) for s in out])

    def _non(self):
        rate = 22050
        ms = 350
        n = int(rate * ms / 1000)
        out = []
        for i in range(n):
            t = i / rate
            f = 280 - 120 * (i / n)
            env = min(1.0, i / (rate * 0.01)) * (1 - (i / n) ** 0.8)
            v = 1.0 if math.sin(2 * math.pi * f * t) > 0 else -0.6
            out.append(int(32767 * 0.3 * env * v))
        return self._pack(out)

    def play(self, name):
        if self.enabled and name in self.sfx:
            self.sfx[name].play()


def draw_floor(screen, cam_x=0, cam_y=0):
    screen.fill(BG)
    tile = 64
    start_x = int(cam_x // tile) * tile
    start_y = int(cam_y // tile) * tile
    end_x = int(cam_x + WIDTH) + tile
    end_y = int(cam_y + HEIGHT) + tile
    for y in range(start_y, end_y, tile):
        for x in range(start_x, end_x, tile):
            sx = x - cam_x
            sy = y - cam_y
            c = FLOOR if (x // tile + y // tile) % 2 == 0 else FLOOR_ALT
            pygame.draw.rect(screen, c, (sx, sy, tile, tile))
    border = pygame.Rect(-cam_x, -cam_y, WORLD_WIDTH, WORLD_HEIGHT)
    pygame.draw.rect(screen, WALL, border, 8)


def clamp_world(x, y, margin=PLAY_MARGIN):
    return (
        max(margin, min(WORLD_WIDTH - margin, x)),
        max(margin, min(WORLD_HEIGHT - margin, y)),
    )


def spawn_at_viewport_edge(cam_x, cam_y):
    side = random.randint(0, 3)
    pad = 80
    if side == 0:
        x = cam_x + random.uniform(pad, WIDTH - pad)
        y = cam_y - 40
    elif side == 1:
        x = cam_x + random.uniform(pad, WIDTH - pad)
        y = cam_y + HEIGHT + 40
    elif side == 2:
        x = cam_x - 40
        y = cam_y + random.uniform(pad, HEIGHT - pad)
    else:
        x = cam_x + WIDTH + 40
        y = cam_y + random.uniform(pad, HEIGHT - pad)
    return clamp_world(x, y, margin=20)


class Nahla:
    def __init__(self, image):
        self.x = WORLD_WIDTH / 2
        self.y = WORLD_HEIGHT / 2
        self.vx = 0.0
        self.vy = 0.0
        self.image = image
        self.base_size = 72

    def update(self, keys):
        self.vx = self.vy = 0.0
        if any(keys[k] for k in MOVE_LEFT):
            self.vx -= NAHLA_SPEED
        if any(keys[k] for k in MOVE_RIGHT):
            self.vx += NAHLA_SPEED
        if any(keys[k] for k in MOVE_UP):
            self.vy -= NAHLA_SPEED
        if any(keys[k] for k in MOVE_DOWN):
            self.vy += NAHLA_SPEED

        length = math.hypot(self.vx, self.vy)
        if length > NAHLA_SPEED:
            self.vx = self.vx / length * NAHLA_SPEED
            self.vy = self.vy / length * NAHLA_SPEED

        self.x += self.vx
        self.y += self.vy
        self.x, self.y = clamp_world(self.x, self.y)

    def draw(self, screen, cam_x, cam_y):
        sx = int(self.x - cam_x)
        sy = int(self.y - cam_y)
        if self.image:
            w = self.base_size
            h = int(self.base_size * self.image.get_height() / self.image.get_width())
            scaled = pygame.transform.smoothscale(self.image, (w, h))
            rect = scaled.get_rect(center=(sx, sy))
            screen.blit(scaled, rect)
        else:
            pygame.draw.circle(screen, ACCENT, (sx, sy), NAHLA_R)
            pygame.draw.circle(screen, (255, 220, 160), (sx, sy), NAHLA_R, 3)

    def collides(self, hx, hy, hr):
        return math.hypot(self.x - hx, self.y - hy) < HIT_R + hr


class Human:
    def __init__(self, kind, x, y):
        self.kind = kind
        info = HUMAN_TYPES[kind]
        self.name = info["name"]
        self.color = info["color"]
        self.base_speed = info["speed"]
        self.speed = info["speed"]
        self.r = info["r"]
        self.x = x
        self.y = y
        self.phrase = random.choice(PHRASES[kind])
        self.phrase_ms = PHRASE_MS
        self.kb_x = 0.0
        self.kb_y = 0.0
        self.kb_ms = 0

    def apply_knockback(self, from_x, from_y, force):
        dx = self.x - from_x
        dy = self.y - from_y
        dist = math.hypot(dx, dy) or 1
        self.kb_x = dx / dist * force
        self.kb_y = dy / dist * force
        self.kb_ms = 350

    def update(self, target_x, target_y, dt):
        self.phrase_ms = max(0, self.phrase_ms - dt)
        if self.kb_ms > 0:
            self.kb_ms -= dt
            self.x += self.kb_x
            self.y += self.kb_y
            self.kb_x *= 0.88
            self.kb_y *= 0.88
            self.x, self.y = clamp_world(self.x, self.y, PLAY_MARGIN - 8)
            return

        dx = target_x - self.x
        dy = target_y - self.y
        dist = math.hypot(dx, dy) or 1
        self.x += dx / dist * self.speed
        self.y += dy / dist * self.speed

    def draw(self, screen, font, font_xs, cam_x, cam_y):
        sx = int(self.x - cam_x)
        sy = int(self.y - cam_y)
        if self.kind == "maman":
            pygame.draw.circle(screen, (255, 190, 230), (sx, sy), self.r + 4)
        pygame.draw.circle(screen, self.color, (sx, sy), self.r)
        pygame.draw.circle(screen, (255, 255, 255), (sx, sy), self.r, 2)
        label = font.render(self.name[0], True, (30, 30, 40))
        screen.blit(label, label.get_rect(center=(sx, sy)))

        if self.phrase_ms > 0:
            self._draw_bubble(screen, font_xs, sx, sy)

    def _draw_bubble(self, screen, font, sx, sy):
        text = font.render(self.phrase, True, (30, 28, 38))
        pad_x, pad_y = 10, 6
        bw = text.get_width() + pad_x * 2
        bh = text.get_height() + pad_y * 2
        bx = int(sx - bw / 2)
        by = int(sy - self.r - bh - 14)
        bx = max(8, min(WIDTH - bw - 8, bx))
        by = max(60, by)
        rect = pygame.Rect(bx, by, bw, bh)
        pygame.draw.rect(screen, (250, 245, 255), rect, border_radius=8)
        pygame.draw.rect(screen, (180, 170, 190), rect, 2, border_radius=8)
        screen.blit(text, (bx + pad_x, by + pad_y))
        tip = [(sx - 6, by + bh), (sx + 6, by + bh), (sx, by + bh + 8)]
        pygame.draw.polygon(screen, (250, 245, 255), tip)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = load_font(28)
        self.font_sm = load_font(20)
        self.font_xs = load_font(16)
        self.font_lg = load_font(52, bold=True)
        self.font_md = load_font(34, bold=True)

        self.nahla_img = None
        if NAHLA_IMG.exists():
            self.nahla_img = pygame.image.load(str(NAHLA_IMG)).convert_alpha()

        self.sounds = SoundBank()
        self.best = load_highscore()
        self.caught_by = ""
        self.state = MENU
        self.reset_run()

    def reset_run(self):
        self.nahla = Nahla(self.nahla_img)
        self.humans = []
        self.elapsed_ms = 0
        self.spawn_timer = 0
        self.spawn_interval = SPAWN_INTERVAL_START_MS
        self.speed_mult = 1.0
        self.max_humans = MAX_HUMANS_START
        self.wave = 1
        self.last_maman_wave = 0
        self.score = 0
        self.claw_cd = 0
        self.claw_fx = 0
        self.caught_by = ""
        self.cam_x = 0.0
        self.cam_y = 0.0
        self.update_camera()

    def update_camera(self):
        self.cam_x = self.nahla.x - WIDTH / 2
        self.cam_y = self.nahla.y - HEIGHT / 2
        if WORLD_WIDTH > WIDTH:
            self.cam_x = max(0, min(WORLD_WIDTH - WIDTH, self.cam_x))
        else:
            self.cam_x = 0
        if WORLD_HEIGHT > HEIGHT:
            self.cam_y = max(0, min(WORLD_HEIGHT - HEIGHT, self.cam_y))
        else:
            self.cam_y = 0

    def difficulty(self):
        seconds = self.elapsed_ms / 1000
        self.speed_mult = 1.0 + seconds * 0.035
        self.spawn_interval = max(
            SPAWN_INTERVAL_MIN_MS,
            SPAWN_INTERVAL_START_MS - int(seconds * 28),
        )
        self.wave = 1 + int(seconds // 15)
        self.max_humans = min(MAX_HUMANS_CAP, MAX_HUMANS_START + int(seconds // 18))

    def spawn_human(self, kind=None):
        if len(self.humans) >= self.max_humans:
            return
        if kind is None:
            no_maman = not any(h.kind == "maman" for h in self.humans)
            if no_maman and self.wave >= MAMAN_GUARANTEE_WAVE and self.wave > self.last_maman_wave:
                kind = "maman"
                self.last_maman_wave = self.wave
            elif no_maman and random.random() < MAMAN_SPAWN_CHANCE:
                kind = "maman"
            else:
                kind = random.choice(["malik", "kays", "noah"])
        sx, sy = spawn_at_viewport_edge(self.cam_x, self.cam_y)
        self.humans.append(Human(kind, sx, sy))
        self.sounds.play("spawn")

    def maybe_spawn(self):
        self.spawn_timer += self.clock.get_time()
        if self.spawn_timer < self.spawn_interval:
            return
        self.spawn_timer = 0
        self.spawn_human()

    def do_claw(self):
        if self.claw_cd > 0:
            return
        self.claw_cd = CLAW_COOLDOWN_MS
        self.claw_fx = CLAW_FX_MS
        self.sounds.play("claw")
        for human in self.humans:
            dist = math.hypot(human.x - self.nahla.x, human.y - self.nahla.y)
            if dist <= CLAW_RANGE + human.r:
                human.apply_knockback(self.nahla.x, self.nahla.y, CLAW_KNOCKBACK)

    def update_playing(self, dt):
        keys = pygame.key.get_pressed()
        self.nahla.update(keys)
        self.update_camera()
        self.elapsed_ms += dt
        self.score = int(self.elapsed_ms / 1000)
        self.claw_cd = max(0, self.claw_cd - dt)
        self.claw_fx = max(0, self.claw_fx - dt)
        self.difficulty()
        self.maybe_spawn()

        for human in self.humans:
            human.speed = human.base_speed * self.speed_mult
            human.update(self.nahla.x, self.nahla.y, dt)
            if self.nahla.collides(human.x, human.y, human.r):
                self.caught_by = human.name
                new_best = max(self.best, self.score)
                if new_best > self.best:
                    self.best = new_best
                    save_highscore(self.best)
                    self.sounds.play("new_record")
                else:
                    self.best = new_best
                self.sounds.play("caught")
                self.state = OVER
                return

    def draw_claw_fx(self, cam_x, cam_y):
        if self.claw_fx <= 0:
            return
        alpha = int(180 * self.claw_fx / CLAW_FX_MS)
        surf = pygame.Surface((CLAW_RANGE * 2, CLAW_RANGE * 2), pygame.SRCALPHA)
        pygame.draw.circle(surf, (*CLAW_C, alpha), (CLAW_RANGE, CLAW_RANGE), CLAW_RANGE, 4)
        for angle in (-0.5, 0, 0.5):
            lx = CLAW_RANGE + math.cos(angle) * CLAW_RANGE * 0.7
            ly = CLAW_RANGE + math.sin(angle) * CLAW_RANGE * 0.7
            pygame.draw.line(surf, (*CLAW_C, alpha), (CLAW_RANGE, CLAW_RANGE), (lx, ly), 5)
        self.screen.blit(
            surf,
            (int(self.nahla.x - cam_x - CLAW_RANGE), int(self.nahla.y - cam_y - CLAW_RANGE)),
        )

    def draw_hud(self):
        bar = pygame.Surface((WIDTH, 52), pygame.SRCALPHA)
        bar.fill((20, 16, 28, 180))
        self.screen.blit(bar, (0, 0))
        left = self.font.render(f"Survie : {self.score}s", True, TEXT)
        mid = self.font.render(f"Vague {self.wave}", True, ACCENT)
        right = self.font_sm.render(f"Record : {self.best}s", True, MUTED)
        self.screen.blit(left, (20, 12))
        self.screen.blit(mid, (WIDTH // 2 - mid.get_width() // 2, 12))
        self.screen.blit(right, (WIDTH - right.get_width() - 20, 14))

        cd_w = 120
        cd_x = WIDTH // 2 - cd_w // 2
        pygame.draw.rect(self.screen, (50, 44, 58), (cd_x, 38, cd_w, 8), border_radius=4)
        if self.claw_cd <= 0:
            fill = OK
            ratio = 1.0
        else:
            fill = MUTED
            ratio = 1.0 - self.claw_cd / CLAW_COOLDOWN_MS
        if ratio > 0:
            pygame.draw.rect(
                self.screen, fill, (cd_x, 38, int(cd_w * ratio), 8), border_radius=4
            )

        hint = self.font_sm.render(
            f"{len(self.humans)}/{self.max_humans} humains — ESPACE : griffe",
            True,
            MUTED,
        )
        self.screen.blit(hint, (20, HEIGHT - 36))

    def draw_menu(self):
        draw_floor(self.screen)
        title = self.font_lg.render("NAHLA ARENA", True, ACCENT)
        sub = self.font.render("Ils veulent te caresser. Nahla dit non.", True, TEXT)
        go = self.font_md.render("ESPACE — jouer", True, OK)
        ctrl = self.font_sm.render("Flèches/ZQSD bouger · ESPACE griffe", True, MUTED)
        self.screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 80)))
        self.screen.blit(sub, sub.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20)))
        self.screen.blit(go, go.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50)))
        self.screen.blit(ctrl, ctrl.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100)))

        rec = self.font_sm.render(f"Record : {self.best}s", True, ACCENT)
        self.screen.blit(rec, rec.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150)))

    def draw_playing(self):
        draw_floor(self.screen, self.cam_x, self.cam_y)
        for human in self.humans:
            human.draw(self.screen, self.font_sm, self.font_xs, self.cam_x, self.cam_y)
        self.nahla.draw(self.screen, self.cam_x, self.cam_y)
        self.draw_claw_fx(self.cam_x, self.cam_y)
        self.draw_hud()

    def draw_over(self):
        self.draw_playing()
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((20, 10, 30, 170))
        self.screen.blit(overlay, (0, 0))

        title = self.font_lg.render("ATTRAPÉE !", True, DANGER)
        msg = self.font.render(
            f"{self.caught_by} t'a caressée. Nahla est furieuse.", True, TEXT
        )
        score = self.font_md.render(f"Survie : {self.score}s", True, ACCENT)
        rec = self.font_sm.render(f"Record : {self.best}s", True, MUTED)
        retry = self.font_md.render("R — rejouer   ESC — menu", True, OK)

        self.screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 70)))
        self.screen.blit(msg, msg.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 10)))
        self.screen.blit(score, score.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40)))
        self.screen.blit(rec, rec.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 80)))
        self.screen.blit(retry, retry.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 140)))

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            return False
        if event.type != pygame.KEYDOWN:
            return True

        if self.state == MENU and event.key == pygame.K_SPACE:
            self.reset_run()
            self.state = PLAYING
        elif self.state == OVER:
            if event.key == pygame.K_r:
                self.reset_run()
                self.state = PLAYING
            elif event.key == pygame.K_ESCAPE:
                self.state = MENU
        elif self.state == PLAYING:
            if event.key == pygame.K_ESCAPE:
                self.state = MENU
            elif event.key == pygame.K_SPACE:
                self.do_claw()

        return True

    def run(self):
        running = True
        while running:
            dt = self.clock.get_time()
            for event in pygame.event.get():
                if not self.handle_event(event):
                    running = False

            if self.state == PLAYING:
                self.update_playing(dt)

            if self.state == MENU:
                self.draw_menu()
            elif self.state == PLAYING:
                self.draw_playing()
            elif self.state == OVER:
                self.draw_over()

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    Game().run()
