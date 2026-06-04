"""Nahla mange — mini-jeu pygame."""

import math
import random
import sys
from pathlib import Path

import pygame

WIDTH = 960
HEIGHT = 640
TITLE = "Nahla mange"
FPS = 60

PLAY_TOP = 100
PLAY_BOTTOM = HEIGHT - 150
PLAY_LEFT = 40
PLAY_RIGHT = WIDTH - 40

PLAYER_BASE = 82
PLAYER_SPEED = 5.2
FLEMME_MAX = 100
FLEMME_MOVE_COST = 0.4
FLEMME_REGEN = 0.15

STRESS_MAX = 100
STRESS_NEAR_RATE = 0.35
STRESS_MALIK_BURST = 25
STRESS_HIDE_RATE = -0.55
PURR_STRESS_HEAL = 35
PURR_COOLDOWN_MS = 7000

GOAL_EATS = 12
MATCH_TIME_MS = 90000
SPAWN_MS = 2200
MAX_PICKUPS = 7
PICKUP_R = 22
MEGA_R = 30
EAT_RANGE = 52

MENU = "menu"
PLAYING = "playing"
WIN = "win"
LOSE = "lose"

ROOMS = {
    "salon": {"bg": (48, 40, 58), "floor": (62, 54, 46)},
    "cuisine": {"bg": (40, 48, 55), "floor": (55, 58, 50)},
    "chambre": {"bg": (52, 38, 48), "floor": (60, 50, 52)},
}

TEXT = (245, 238, 225)
ACCENT = (255, 150, 60)
DANGER = (220, 80, 80)
WIN_C = (100, 220, 140)
MEGA_C = (180, 100, 255)
RONRON_C = (255, 140, 180)

ASSETS_DIR = Path(__file__).parent
NAHLA_PHOTO = ASSETS_DIR / "WhatsApp Image 2026-04-24 at 00.18.56.jpeg"
NAHLA_HEAD = ASSETS_DIR / "nahla_head.png"
CROP = (0.24, 0.12, 0.52, 0.40)

LINES = [
    "C'est moi la boss.",
    "Toi t'as rien.",
    "Miaou = dégage.",
    "J'mange, pas toi.",
    "Humain stupide.",
]
MALIK_LINES = ["MALIK COURT !!!", "Il est à poil !!!", "Pourquoi il crie ???"]
MEGA_LINES = ["SAC JACKPOT !!!", "Jackpot de croquettes !!!"]
RONRON_LINES = ["Ronron... stress -50.", "Purr purr purr."]


def load_nahla_base():
    if NAHLA_HEAD.exists():
        img = pygame.image.load(str(NAHLA_HEAD)).convert_alpha()
    else:
        full = pygame.image.load(str(NAHLA_PHOTO)).convert()
        w, h = full.get_size()
        cl, ct, cw, ch = CROP
        rect = pygame.Rect(int(w * cl), int(h * ct), int(w * cw), int(h * ch))
        img = full.subsurface(rect).copy()
        img = pygame.transform.smoothscale(img, (110, 110))
        pygame.image.save(img, str(NAHLA_HEAD))
        img = img.convert_alpha()
    return pygame.transform.smoothscale(img, (PLAYER_BASE, PLAYER_BASE))


def scale_nahla(base, scale):
    size = max(50, int(PLAYER_BASE * scale))
    return pygame.transform.smoothscale(base, (size, size)), size


def center_text(font, text, y, color=TEXT):
    surf = font.render(text, True, color)
    return surf, ((WIDTH - surf.get_width()) // 2, y)


def draw_bar(screen, x, y, w, h, val, maximum, label, fill_color, border_color):
    pygame.draw.rect(screen, (35, 30, 42), (x, y, w, h), border_radius=6)
    fill = int(w * max(0, min(val, maximum)) / maximum)
    if fill > 0:
        pygame.draw.rect(screen, fill_color, (x, y, fill, h), border_radius=6)
    pygame.draw.rect(screen, border_color, (x, y, w, h), 2, border_radius=6)
    t = pygame.font.SysFont(None, 22).render(f"{label} {int(val)}", True, TEXT)
    screen.blit(t, (x, y - 18))


def couch_rect():
    return pygame.Rect(WIDTH // 2 - 110, HEIGHT - 175, 220, 50)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.font_big = pygame.font.SysFont(None, 52, bold=True)
        self.font = pygame.font.SysFont(None, 30)
        self.font_small = pygame.font.SysFont(None, 24)
        self.nahla_base = load_nahla_base()
        self.state = MENU
        self.room_name = "salon"
        self.reset_play()

    def reset_play(self):
        self.px = WIDTH // 2 - PLAYER_BASE // 2
        self.py = (PLAY_TOP + PLAY_BOTTOM) // 2 - PLAYER_BASE // 2
        self.size_scale = 1.0
        self.player_size = PLAYER_BASE
        self.flemme = FLEMME_MAX
        self.stress = 12
        self.score = 0
        self.combo = 0
        self.last_eat_ms = 0
        self.pickups = []
        self.humans = []
        self.particles = []
        self.float_texts = []
        self.bubble = ""
        self.bubble_ms = 0
        self.chew_flash = 0
        self.wobble = 0.0
        self.time_left_ms = MATCH_TIME_MS
        self.next_spawn_ms = 0
        self.malik_banner_ms = 0
        self.rush_ms = 0
        self.hiding = False
        self.purr_ready_ms = 0
        self.water_used = False
        self.spawn_human()
        self.spawn_human()

    def player_center(self):
        return self.px + self.player_size // 2, self.py + self.player_size // 2

    def on_couch(self):
        feet = pygame.Rect(self.px + 10, self.py + self.player_size - 16, self.player_size - 20, 18)
        return couch_rect().colliderect(feet)

    def add_float(self, x, y, text, color=ACCENT):
        self.float_texts.append({"x": x, "y": y, "text": text, "life": 55, "vy": -1.2, "color": color})

    def spawn_pickup(self):
        if len(self.pickups) >= MAX_PICKUPS:
            return
        roll = random.random()
        if roll < 0.07:
            kind = "mega"
        elif roll < 0.14:
            kind = "ronron"
        else:
            kind = "normal"
        for _ in range(30):
            x = random.randint(PLAY_LEFT + 35, PLAY_RIGHT - 35)
            y = random.randint(PLAY_TOP + 35, PLAY_BOTTOM - 35)
            cx, cy = self.player_center()
            if math.hypot(x - cx, y - cy) > 90:
                self.pickups.append({"x": x, "y": y, "kind": kind, "born": pygame.time.get_ticks()})
                return

    def spawn_human(self, malik_force=False):
        side = random.choice(("left", "right"))
        x = PLAY_LEFT - 40 if side == "left" else PLAY_RIGHT + 40
        y = random.randint(PLAY_TOP + 20, PLAY_BOTTOM - 50)
        vx = random.uniform(1.4, 2.8) * (1 if side == "left" else -1)
        if self.rush_ms > 0:
            vx *= 1.35
        self.humans.append(
            {
                "x": float(x),
                "y": float(y),
                "vx": vx,
                "vy": random.uniform(-0.35, 0.35),
                "malik": malik_force or random.random() < 0.24,
            }
        )

    def apply_eat(self, p):
        kind = p["kind"]
        now = pygame.time.get_ticks()
        if now - self.last_eat_ms < 1800:
            self.combo += 1
        else:
            self.combo = 1
        self.last_eat_ms = now

        if kind == "mega":
            gain = 3
            self.bubble = random.choice(MEGA_LINES)
            self.time_left_ms = min(MATCH_TIME_MS + 15000, self.time_left_ms + 5000)
            color = MEGA_C
            for _ in range(16):
                self._particle(p["x"], p["y"], MEGA_C)
        elif kind == "ronron":
            gain = 1
            self.stress = max(0, self.stress - PURR_STRESS_HEAL)
            self.bubble = random.choice(RONRON_LINES)
            color = RONRON_C
            for _ in range(10):
                self._particle(p["x"], p["y"], RONRON_C)
        else:
            gain = 1 + self.combo // 3
            self.bubble = random.choice(LINES)
            color = ACCENT
            for _ in range(8):
                self._particle(p["x"], p["y"], (255, 210, 120))

        self.score += gain
        self.flemme = min(FLEMME_MAX, self.flemme + 14)
        self.size_scale = min(1.42, 1.0 + self.score * 0.035)
        self.chew_flash = 22
        self.bubble_ms = 2000
        self.add_float(p["x"], p["y"] - 20, f"+{gain}", color)
        if self.combo >= 3:
            self.add_float(self.px, self.py - 30, f"Combo x{self.combo}!", (255, 220, 100))

        if self.score >= 8 and self.rush_ms <= 0:
            self.rush_ms = 14000
            self.bubble = "RUSH ! Les humains débarquent !"
            self.bubble_ms = 2500
            for _ in range(3):
                self.spawn_human(malik_force=random.random() < 0.5)

        if self.score >= GOAL_EATS:
            self.state = WIN

    def _particle(self, x, y, color):
        self.particles.append(
            {
                "x": float(x),
                "y": float(y),
                "vx": random.uniform(-2.5, 2.5),
                "vy": random.uniform(-3.5, -0.5),
                "life": 32,
                "color": color,
            }
        )

    def try_purr(self):
        now = pygame.time.get_ticks()
        if now < self.purr_ready_ms:
            return
        self.purr_ready_ms = now + PURR_COOLDOWN_MS
        self.stress = max(0, self.stress - PURR_STRESS_HEAL)
        self.bubble = "Ronron manuel. Les humains m'énervent moins."
        self.bubble_ms = 1600
        cx, cy = self.player_center()
        for _ in range(12):
            self._particle(cx, cy, RONRON_C)

    def try_water(self):
        if self.water_used:
            self.bubble = "Gamelle vide. Dommage."
            self.bubble_ms = 1200
            return
        cx, cy = self.player_center()
        bowl_x, bowl_y = PLAY_RIGHT - 70, PLAY_TOP + 40
        if math.hypot(cx - bowl_x, cy - bowl_y) < 55:
            self.water_used = True
            self.flemme = FLEMME_MAX
            self.bubble = "Eau fraîche. Flemme au max."
            self.bubble_ms = 1500
            self.add_float(bowl_x, bowl_y, "GLoup", (120, 200, 255))

    def try_eat_nearby(self):
        if self.hiding:
            return
        cx, cy = self.player_center()
        for p in self.pickups[:]:
            r = MEGA_R if p["kind"] == "mega" else PICKUP_R
            if math.hypot(cx - p["x"], cy - p["y"]) < EAT_RANGE + (8 if p["kind"] == "mega" else 0):
                self.pickups.remove(p)
                self.apply_eat(p)
                return

    def handle_move(self):
        keys = pygame.key.get_pressed()
        self.hiding = (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.on_couch()
        if self.hiding or self.flemme < 10:
            return
        dx = dy = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_q] or keys[pygame.K_a]:
            dx -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += 1
        if keys[pygame.K_UP] or keys[pygame.K_z] or keys[pygame.K_w]:
            dy -= 1
        if not self.hiding and (keys[pygame.K_DOWN] or keys[pygame.K_s]):
            dy += 1
        if dx or dy:
            length = math.hypot(dx, dy) or 1
            speed = PLAYER_SPEED * (0.5 if self.flemme < 35 else 1.0)
            self.px += dx / length * speed
            self.py += dy / length * speed
            self.px = max(PLAY_LEFT, min(PLAY_RIGHT - self.player_size, self.px))
            self.py = max(PLAY_TOP, min(PLAY_BOTTOM - self.player_size, self.py))
            self.flemme = max(0, self.flemme - FLEMME_MOVE_COST)

    def update(self, dt):
        if self.state != PLAYING:
            return
        self.wobble += dt * 0.004
        self.time_left_ms = max(0, self.time_left_ms - dt)
        if self.time_left_ms <= 0:
            self.state = LOSE
            self.bubble = "Temps écoulé. Nahla n'a pas assez mangé."
            return

        now = pygame.time.get_ticks()
        spawn_delay = SPAWN_MS // 2 if self.rush_ms > 0 else SPAWN_MS
        if now >= self.next_spawn_ms:
            self.spawn_pickup()
            self.next_spawn_ms = now + spawn_delay

        spawn_chance = 0.004 if self.rush_ms > 0 else 0.0025
        if random.random() < spawn_chance:
            self.spawn_human()
            if random.random() < 0.45:
                self.malik_banner_ms = 2500
                self.bubble = random.choice(MALIK_LINES)
                self.bubble_ms = 2200
                self.stress = min(STRESS_MAX, self.stress + STRESS_MALIK_BURST)

        if self.rush_ms > 0:
            self.rush_ms = max(0, self.rush_ms - dt)

        cx, cy = self.player_center()
        if self.hiding:
            self.stress = max(0, self.stress + STRESS_HIDE_RATE)

        for h in self.humans[:]:
            h["x"] += h["vx"]
            h["y"] += h["vy"]
            if h["x"] < PLAY_LEFT - 90 or h["x"] > PLAY_RIGHT + 90:
                self.humans.remove(h)
                continue
            if not self.hiding and math.hypot(cx - h["x"], cy - h["y"]) < 72:
                rate = STRESS_NEAR_RATE * (2.0 if h["malik"] else 1.0)
                if self.rush_ms > 0:
                    rate *= 1.3
                self.stress = min(STRESS_MAX, self.stress + rate)

        if self.stress >= STRESS_MAX:
            self.state = LOSE
            self.bubble = "Trop de stress. Nahla sous le lit."
            return

        if not self.hiding and self.flemme < FLEMME_MAX:
            self.flemme = min(FLEMME_MAX, self.flemme + FLEMME_REGEN)

        for part in self.particles[:]:
            part["x"] += part["vx"]
            part["y"] += part["vy"]
            part["life"] -= 1
            if part["life"] <= 0:
                self.particles.remove(part)

        for ft in self.float_texts[:]:
            ft["y"] += ft["vy"]
            ft["life"] -= 1
            if ft["life"] <= 0:
                self.float_texts.remove(ft)

        if self.chew_flash > 0:
            self.chew_flash -= 1
        if self.bubble_ms > 0:
            self.bubble_ms = max(0, self.bubble_ms - dt)
        if self.malik_banner_ms > 0:
            self.malik_banner_ms = max(0, self.malik_banner_ms - dt)

        self.nahla_sprite, self.player_size = scale_nahla(self.nahla_base, self.size_scale)

    def draw_room(self):
        colors = ROOMS[self.room_name]
        self.screen.fill(colors["bg"])
        pygame.draw.rect(self.screen, colors["floor"], (0, HEIGHT - 130, WIDTH, 130))
        for fx in range(80, WIDTH, 160):
            pygame.draw.rect(self.screen, (50, 42, 38), (fx, HEIGHT - 130, 8, 130))
        bowl_x, bowl_y = PLAY_RIGHT - 70, PLAY_TOP + 45
        pygame.draw.ellipse(self.screen, (80, 140, 200), (bowl_x - 22, bowl_y - 10, 44, 22))
        if not self.water_used:
            pygame.draw.ellipse(self.screen, (120, 190, 255), (bowl_x - 16, bowl_y - 6, 32, 12))

    def draw_couch(self):
        cr = couch_rect()
        col = (120, 95, 75) if self.hiding else (90, 70, 55)
        pygame.draw.rect(self.screen, col, cr, border_radius=10)
        pygame.draw.rect(self.screen, (55, 42, 35), cr, 2, border_radius=10)
        t = pygame.font.SysFont(None, 20).render("Canapé S/↓ = se cacher", True, (200, 180, 160))
        self.screen.blit(t, (cr.centerx - t.get_width() // 2, cr.top - 18))

    def draw_hud(self):
        secs = math.ceil(self.time_left_ms / 1000)
        timer = self.font.render(f"Temps : {secs}s", True, TEXT)
        self.screen.blit(timer, (WIDTH - timer.get_width() - 24, 18))
        goal = self.font_small.render(f"Objectif : {self.score} / {GOAL_EATS}", True, ACCENT)
        self.screen.blit(goal, (24, 18))
        if self.rush_ms > 0:
            rush = self.font_small.render("RUSH !", True, DANGER)
            self.screen.blit(rush, (WIDTH // 2 - rush.get_width() // 2, 42))
        purr_ok = pygame.time.get_ticks() >= self.purr_ready_ms
        purr_col = (140, 255, 180) if purr_ok else (100, 100, 100)
        purr = self.font_small.render("F = ronron" if purr_ok else "Ronron recharge...", True, purr_col)
        self.screen.blit(purr, (WIDTH - purr.get_width() - 24, 42))
        draw_bar(self.screen, 24, 58, 200, 16, self.flemme, FLEMME_MAX, "Flemme", (80, 160, 220), (50, 90, 120))
        draw_bar(self.screen, 24, 98, 200, 16, self.stress, STRESS_MAX, "Stress", DANGER, (120, 50, 50))

    def draw_pickups(self):
        now = pygame.time.get_ticks()
        for p in self.pickups:
            pulse = int(math.sin(now * 0.008 + p["x"]) * 3)
            if p["kind"] == "mega":
                r = MEGA_R + pulse
                pygame.draw.circle(self.screen, MEGA_C, (int(p["x"]), int(p["y"])), r + 4)
                pygame.draw.circle(self.screen, (255, 220, 255), (int(p["x"]), int(p["y"])), r)
                lbl = pygame.font.SysFont(None, 18).render("SAC", True, (40, 20, 60))
                self.screen.blit(lbl, (int(p["x"]) - 12, int(p["y"]) - 6))
            elif p["kind"] == "ronron":
                r = PICKUP_R + pulse
                pygame.draw.circle(self.screen, RONRON_C, (int(p["x"]), int(p["y"])), r)
                pygame.draw.circle(self.screen, (255, 200, 220), (int(p["x"]), int(p["y"])), r - 8)
            else:
                r = PICKUP_R + pulse
                pygame.draw.circle(self.screen, (200, 150, 50), (int(p["x"]), int(p["y"])), r + 3)
                pygame.draw.circle(self.screen, (255, 220, 100), (int(p["x"]), int(p["y"])), r)

    def draw_humans(self):
        for h in self.humans:
            color = (255, 100, 70) if h["malik"] else (180, 180, 200)
            pygame.draw.circle(self.screen, color, (int(h["x"]), int(h["y"])), 18)
            label = "Malik" if h["malik"] else "Humain"
            t = pygame.font.SysFont(None, 20).render(label, True, TEXT)
            self.screen.blit(t, (int(h["x"]) - t.get_width() // 2, int(h["y"]) - 34))

    def draw_nahla(self):
        if self.hiding:
            cx, cy = self.player_center()
            pygame.draw.ellipse(self.screen, (50, 40, 35), (cx - 40, cy, 80, 28))
        if self.chew_flash > 0:
            cx, cy = self.player_center()
            pygame.draw.circle(self.screen, (255, 200, 120), (cx, cy), 38, 3)
        self.screen.blit(self.nahla_sprite, (int(self.px), int(self.py)))

    def draw_particles(self):
        for p in self.particles:
            c = p.get("color", (255, 210, 120))
            pygame.draw.circle(self.screen, c, (int(p["x"]), int(p["y"])), 4)

    def draw_floats(self):
        font = pygame.font.SysFont(None, 26)
        for ft in self.float_texts:
            alpha = min(255, ft["life"] * 5)
            s = font.render(ft["text"], True, ft["color"])
            s.set_alpha(alpha)
            self.screen.blit(s, (int(ft["x"]), int(ft["y"])))

    def draw_bubble(self):
        if self.bubble_ms <= 0 or not self.bubble:
            return
        box = self.font.render(self.bubble, True, (25, 20, 18))
        pad = 10
        w, h = box.get_width() + pad * 2, box.get_height() + pad * 2
        x = WIDTH // 2 - w // 2
        y = 124
        pygame.draw.rect(self.screen, (252, 248, 235), (x, y, w, h), border_radius=10)
        self.screen.blit(box, (x + pad, y + pad))

    def draw_menu(self):
        self.draw_room()
        t, p = center_text(self.font_big, "Nahla mange", 100, ACCENT)
        self.screen.blit(t, p)
        lines = [
            f"Mange {GOAL_EATS} croquettes avant la fin du temps.",
            "ZQSD · Espace = manger · S/↓ sur canapé = cacher",
            "Violet SAC = +3 et +5 sec · Rose = moins de stress",
            "F = ronron (cooldown) · E = eau (1x, coin haut droit)",
            "À 8 mangées : vague RUSH (humains + Malik)",
            "Nahla grossit en mangeant",
            "",
            "Flèches : pièce · Entrée : jouer",
        ]
        for i, line in enumerate(lines):
            s, pos = center_text(self.font_small, line, 200 + i * 26)
            self.screen.blit(s, pos)

    def draw_play(self):
        self.draw_room()
        self.draw_couch()
        self.draw_pickups()
        self.draw_humans()
        self.draw_particles()
        self.draw_nahla()
        self.draw_floats()
        self.draw_bubble()
        self.draw_hud()
        if self.malik_banner_ms > 0:
            m, mp = center_text(self.font_big, "MALIK !!!", 155, (255, 90, 50))
            self.screen.blit(m, mp)
        hint = self.font_small.render(
            "ZQSD · Espace manger · F ronron · E eau · Canapé cache",
            True,
            (170, 165, 155),
        )
        self.screen.blit(hint, (WIDTH // 2 - hint.get_width() // 2, HEIGHT - 26))

    def draw_end(self, won):
        self.draw_play()
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        self.screen.blit(overlay, (0, 0))
        title = "Nahla est rassasiée !" if won else "Ah je suis foutue..."
        color = WIN_C if won else DANGER
        t, p = center_text(self.font_big, title, 240, color)
        self.screen.blit(t, p)
        sub = f"Score final : {self.score}" if won else self.bubble
        s, sp = center_text(self.font, sub, 310)
        self.screen.blit(s, sp)
        r, rp = center_text(self.font_small, "R rejouer · Échap quitter", 400)
        self.screen.blit(r, rp)

    def run(self):
        while True:
            dt = self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_LEFT:
                        names = list(ROOMS.keys())
                        i = names.index(self.room_name)
                        self.room_name = names[(i - 1) % len(names)]
                    if event.key == pygame.K_RIGHT:
                        names = list(ROOMS.keys())
                        i = names.index(self.room_name)
                        self.room_name = names[(i + 1) % len(names)]
                    if event.key == pygame.K_RETURN and self.state == MENU:
                        self.state = PLAYING
                        self.reset_play()
                    if event.key == pygame.K_SPACE and self.state == PLAYING:
                        self.try_eat_nearby()
                    if event.key == pygame.K_f and self.state == PLAYING:
                        self.try_purr()
                    if event.key == pygame.K_e and self.state == PLAYING:
                        self.try_water()
                    if event.key == pygame.K_r and self.state in (WIN, LOSE):
                        self.state = PLAYING
                        self.reset_play()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.state == MENU:
                        self.state = PLAYING
                        self.reset_play()
                    elif self.state == PLAYING:
                        self.try_eat_nearby()

            if self.state == PLAYING:
                self.handle_move()
                self.update(dt)

            if self.state == MENU:
                self.draw_menu()
            elif self.state == PLAYING:
                self.draw_play()
            elif self.state == WIN:
                self.draw_end(True)
            else:
                self.draw_end(False)

            pygame.display.flip()


if __name__ == "__main__":
    Game().run()
