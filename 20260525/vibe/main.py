"""Nahla vs l'aspirateur — boss fight pygame."""

import math
import random
import sys
from pathlib import Path

import pygame

WIDTH = 960
HEIGHT = 640
TITLE = "Nahla vs l'aspirateur"
FPS = 60

BG_TOP = (45, 38, 55)
BG_BOTTOM = (28, 24, 32)
FLOOR = (55, 48, 42)
COUCH = (90, 70, 55)
COUCH_CUSHION = (110, 85, 65)
TEXT = (245, 240, 230)
ACCENT = (255, 140, 50)
DANGER = (220, 70, 70)
WIN_COLOR = (90, 220, 130)

MENU = "menu"
PLAYING = "playing"
WIN = "win"
LOSE = "lose"

PLAYER_SIZE = 78
PLAYER_SPEED = 5.5
PLAYER_MARGIN = 20
PLAY_TOP = 95
PLAY_BOTTOM = HEIGHT - PLAYER_SIZE - 30

BOSS_W = 120
BOSS_H = 90
BOSS_MAX_HP = 100
BOSS_SPEED = 2.4
BOSS_SPEED_PHASE2 = 4.8
BOSS_PHASE_HP = BOSS_MAX_HP // 2
BOSS_DAMAGE_TOUCH = 0.35
BOSS_DAMAGE_NEAR = 0.12
NEAR_RADIUS = 140
FEAR_NEAR_RATE_PHASE2 = 0.30
FEAR_TOUCH_RATE_PHASE2 = 0.62

FUR_RADIUS = 46
FUR_DURATION_MS = 9000
FUR_SLOW_MULT = 0.35
MAX_FUR_PATCHES = 7

FEAR_MAX = 100
FEAR_NEAR_RATE = 0.22
FEAR_TOUCH_RATE = 0.55
FEAR_HIDE_RATE = -0.45
FEAR_IDLE_RATE = -0.08

FLEMME_MAX = 100
FLEMME_MOVE_COST = 0.35
FLEMME_REGEN = 0.25
FLEMME_MIN_MOVE = 8

CLAW_RANGE = 95
CLAW_DAMAGE = 12
CLAW_COUNTER_BONUS = 10
CLAW_COOLDOWN_MS = 450
COUNTER_TOUCH_DIST = 60
COUNTER_WINDOW_MS = 400
BOSS_RECOIL_MS = 500
BOSS_RECOIL_SPEED = 9
BOSS_PREDICT_NORMAL = 7
BOSS_PREDICT_PHASE2 = 12
FUR_AVOID_PENALTY = 100
BOSS_STUCK_FRAMES = 16

CROQUETTE_SIZE = 30
CROQUETTE_SPAWN_MS = 11000
CROQUETTE_FEAR_HEAL = 18
CROQUETTE_FLEMME_HEAL = 28

HIDE_KEYS = (pygame.K_DOWN, pygame.K_s)

# Meubles (obstacles)
FURNITURE = [
    pygame.Rect(140, 250, 155, 78),
    pygame.Rect(470, 175, 58, 58),
    pygame.Rect(695, 310, 105, 50),
]

ASSETS_DIR = Path(__file__).parent
NAHLA_PHOTO = ASSETS_DIR / "WhatsApp Image 2026-04-24 at 00.18.56.jpeg"
NAHLA_HEAD = ASSETS_DIR / "nahla_head.png"
CROP_LEFT, CROP_TOP = 0.24, 0.12
CROP_WIDTH, CROP_HEIGHT = 0.52, 0.40
SPRITE_SOURCE_SIZE = 110


def load_nahla_source():
    if NAHLA_HEAD.exists():
        return pygame.image.load(str(NAHLA_HEAD)).convert_alpha()
    full = pygame.image.load(str(NAHLA_PHOTO)).convert()
    w, h = full.get_size()
    crop = pygame.Rect(
        int(w * CROP_LEFT),
        int(h * CROP_TOP),
        int(w * CROP_WIDTH),
        int(h * CROP_HEIGHT),
    )
    head = full.subsurface(crop).copy()
    head = pygame.transform.smoothscale(head, (SPRITE_SOURCE_SIZE, SPRITE_SOURCE_SIZE))
    pygame.image.save(head, str(NAHLA_HEAD))
    return head.convert_alpha()


def scale_sprite(source, size):
    if source.get_size() == (size, size):
        return source
    return pygame.transform.smoothscale(source, (size, size))


def couch_rect():
    w, h = 220, 56
    return pygame.Rect((WIDTH - w) // 2, HEIGHT - 110, w, h)


def all_obstacles():
    return list(FURNITURE) + [couch_rect()]


def resolve_rect(rect, obstacles):
    """Repousse rect hors des obstacles (collisions solides)."""
    out = rect.copy()
    for _ in range(4):
        moved = False
        for obs in obstacles:
            if not out.colliderect(obs):
                continue
            moved = True
            overlap_l = out.right - obs.left
            overlap_r = obs.right - out.left
            overlap_t = out.bottom - obs.top
            overlap_b = obs.bottom - out.top
            m = min(overlap_l, overlap_r, overlap_t, overlap_b)
            if m == overlap_l:
                out.right = obs.left
            elif m == overlap_r:
                out.left = obs.right
            elif m == overlap_t:
                out.bottom = obs.top
            else:
                out.top = obs.bottom
        if not moved:
            break
    return out


def draw_furniture(screen):
    table, plant, shelf = FURNITURE
    pygame.draw.rect(screen, (75, 55, 40), table, border_radius=6)
    pygame.draw.rect(screen, (95, 70, 50), table.inflate(-8, -12), border_radius=4)
    pygame.draw.ellipse(screen, (55, 90, 45), plant)
    pygame.draw.rect(screen, (80, 55, 35), (plant.x + 14, plant.bottom - 18, 30, 18), border_radius=4)
    pygame.draw.circle(screen, (40, 110, 50), (plant.centerx - 8, plant.centery - 6), 14)
    pygame.draw.circle(screen, (50, 130, 60), (plant.centerx + 10, plant.centery - 12), 12)
    pygame.draw.rect(screen, (70, 52, 38), shelf, border_radius=4)
    pygame.draw.rect(screen, (88, 68, 50), shelf.inflate(-6, -10), border_radius=3)


def draw_croquette(screen, x, y, pulse):
    r = CROQUETTE_SIZE // 2 + int(math.sin(pulse) * 3)
    pygame.draw.circle(screen, (200, 150, 50), (x, y), r + 4)
    pygame.draw.circle(screen, (255, 210, 80), (x, y), r)
    font = pygame.font.SysFont(None, 20)
    label = font.render("C", True, (120, 80, 20))
    screen.blit(label, (x - label.get_width() // 2, y - label.get_height() // 2))


def draw_gradient_bg(screen):
    for y in range(HEIGHT - 120):
        t = y / max(1, HEIGHT - 120)
        c = (
            int(BG_TOP[0] * (1 - t) + BG_BOTTOM[0] * t),
            int(BG_TOP[1] * (1 - t) + BG_BOTTOM[1] * t),
            int(BG_TOP[2] * (1 - t) + BG_BOTTOM[2] * t),
        )
        pygame.draw.line(screen, c, (0, y), (WIDTH, y))
    pygame.draw.rect(screen, FLOOR, (0, HEIGHT - 120, WIDTH, 120))


def draw_couch(screen, rect, highlight):
    color = COUCH_CUSHION if highlight else COUCH
    pygame.draw.rect(screen, color, rect, border_radius=10)
    pygame.draw.rect(screen, (60, 45, 35), rect, 3, border_radius=10)
    label = pygame.font.SysFont(None, 22).render("canapé — cache-toi (S / ↓)", True, (200, 180, 160))
    screen.blit(label, (rect.centerx - label.get_width() // 2, rect.top - 22))


def draw_bar(screen, x, y, w, h, value, maximum, label, colors):
    pygame.draw.rect(screen, (40, 35, 45), (x, y, w, h), border_radius=6)
    fill = int(w * max(0, min(value, maximum)) / maximum)
    if fill > 0:
        pygame.draw.rect(screen, colors[0], (x, y, fill, h), border_radius=6)
    pygame.draw.rect(screen, colors[1], (x, y, w, h), 2, border_radius=6)
    font = pygame.font.SysFont(None, 24)
    txt = font.render(f"{label} {int(value)}", True, TEXT)
    screen.blit(txt, (x, y - 20))


def draw_fur_patches(screen, patches, now):
    for p in patches:
        age = (now - p["born"]) / FUR_DURATION_MS
        alpha = int(200 * (1 - age * 0.35))
        r = FUR_RADIUS
        surf = pygame.Surface((r * 2, r * 2), pygame.SRCALPHA)
        for i in range(14):
            ang = i * 0.9 + p["born"] * 0.001
            fx = r + int(math.cos(ang) * (r * 0.55))
            fy = r + int(math.sin(ang) * (r * 0.4))
            blob = 5 + (i * 3 + p["born"]) % 7
            pygame.draw.circle(surf, (210, 195, 170, alpha), (fx, fy), blob)
        pygame.draw.ellipse(surf, (180, 160, 140, alpha // 2), (8, r - 12, r * 2 - 16, 22))
        screen.blit(surf, (int(p["x"] - r), int(p["y"] - r)))


def draw_vacuum(screen, x, y, wobble, phase2, eye_on):
    if phase2:
        for i in range(4):
            lx = x - 28 - i * 14
            ly = y + 40 + int(math.sin(wobble + i) * 4)
            pygame.draw.line(screen, (255, 90, 60), (lx, ly), (lx - 18, ly - 6), 3)

    body = pygame.Rect(x, y, BOSS_W, BOSS_H)
    shell = (95, 55, 55) if phase2 else (70, 75, 85)
    inner = (130, 85, 85) if phase2 else (100, 105, 120)
    pygame.draw.ellipse(screen, shell, body)
    pygame.draw.ellipse(screen, inner, body.inflate(-16, -20))
    hx = x + BOSS_W - 10 + int(math.sin(wobble) * (10 if phase2 else 6))
    pygame.draw.line(screen, (50, 50, 60), (hx, y + 20), (hx + 50, y - 30), 8)
    eye = (x + 28 + int(math.sin(wobble * 2) * 3), y + 32)
    if eye_on:
        glow = 20 if phase2 else 14
        pygame.draw.circle(screen, (255, 30, 20), eye, glow)
        pygame.draw.circle(screen, (255, 220, 200), eye, 6)
    elif phase2:
        pygame.draw.circle(screen, (60, 20, 20), eye, 10)
    for wx in (x + 22, x + BOSS_W - 34):
        pygame.draw.circle(screen, (30, 30, 35), (wx, y + BOSS_H - 6), 12)


def draw_nahla(screen, sprite, px, py, hiding, claw_flash):
    if hiding:
        pygame.draw.ellipse(screen, (50, 40, 35), (px - 10, py + 40, PLAYER_SIZE + 20, 28))
        small = scale_sprite(sprite, int(PLAYER_SIZE * 0.55))
        screen.blit(small, (px + 20, py + 38))
    else:
        screen.blit(sprite, (px, py))
    if claw_flash > 0:
        alpha = min(255, claw_flash * 8)
        surf = pygame.Surface((CLAW_RANGE, CLAW_RANGE), pygame.SRCALPHA)
        pygame.draw.arc(
            surf,
            (255, 200, 120, alpha),
            (10, 10, CLAW_RANGE - 20, CLAW_RANGE - 20),
            0.2,
            2.8,
            6,
        )
        screen.blit(surf, (px + PLAYER_SIZE - 20, py - 10))


def center_text(font, text, y, color=TEXT):
    surf = font.render(text, True, color)
    return surf, ((WIDTH - surf.get_width()) // 2, y)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.font_big = pygame.font.SysFont(None, 52, bold=True)
        self.font = pygame.font.SysFont(None, 32)
        self.font_small = pygame.font.SysFont(None, 26)
        self.nahla_src = load_nahla_source()
        self.nahla_sprite = scale_sprite(self.nahla_src, PLAYER_SIZE)
        self.state = MENU
        self.reset_run()

    def reset_run(self):
        self.px = WIDTH // 2 - PLAYER_SIZE // 2
        self.py = HEIGHT // 2 - PLAYER_SIZE // 2
        self.boss_x = WIDTH - BOSS_W - 100
        self.boss_y = PLAY_TOP + 40
        self.boss_hp = BOSS_MAX_HP
        self.boss_dir = -1
        self.fear = 25
        self.flemme = FLEMME_MAX
        self.hiding = False
        self.wobble = 0.0
        self.claw_flash = 0
        self.claw_cd = 0
        self.moved_this_frame = False
        self.fur_patches = []
        self.phase2_banner_ms = 0
        self.croquette = None
        self.next_croquette_ms = pygame.time.get_ticks() + 6000
        self.boss_recoil_ms = 0
        self.boss_recoil_vx = 0.0
        self.boss_recoil_vy = 0.0
        self.last_boss_touch_ms = 0
        self.counter_banner_ms = 0
        self.pickup_banner_ms = 0
        self._prev_px = self.px
        self._prev_py = self.py
        self._boss_stuck = 0
        self._last_bx = self.boss_x
        self._last_by = self.boss_y

    def player_hitbox(self):
        return pygame.Rect(self.px + 6, self.py + 6, PLAYER_SIZE - 12, PLAYER_SIZE - 12)

    def boss_hitbox(self):
        return pygame.Rect(self.boss_x + 12, self.boss_y + 12, BOSS_W - 24, BOSS_H - 24)

    def boss_phase2(self):
        return self.boss_hp <= BOSS_PHASE_HP

    def boss_eye_on(self):
        if not self.boss_phase2():
            return True
        return (pygame.time.get_ticks() // 110) % 2 == 0

    def living_fur(self):
        now = pygame.time.get_ticks()
        self.fur_patches = [p for p in self.fur_patches if now - p["born"] < FUR_DURATION_MS]
        return self.fur_patches

    def spawn_fur(self):
        if len(self.fur_patches) >= MAX_FUR_PATCHES:
            self.fur_patches.pop(0)
        cx, cy = self.player_center()
        self.fur_patches.append({"x": cx, "y": cy + 10, "born": pygame.time.get_ticks()})

    def boss_on_fur(self):
        bx, by = self.boss_center()
        for p in self.living_fur():
            if math.hypot(bx - p["x"], by - p["y"]) < FUR_RADIUS + 20:
                return True
        return False

    def player_center(self):
        return self.px + PLAYER_SIZE // 2, self.py + PLAYER_SIZE // 2

    def boss_center(self):
        return self.boss_x + BOSS_W // 2, self.boss_y + BOSS_H // 2

    def dist_boss_player(self):
        bx, by = self.boss_center()
        px, py = self.player_center()
        return math.hypot(bx - px, by - py)

    def on_couch(self):
        feet = pygame.Rect(self.px + 8, self.py + PLAYER_SIZE - 18, PLAYER_SIZE - 16, 20)
        return couch_rect().colliderect(feet)

    def clamp_player(self):
        self.px = max(PLAYER_MARGIN, min(WIDTH - PLAYER_SIZE - PLAYER_MARGIN, self.px))
        self.py = max(PLAY_TOP, min(PLAY_BOTTOM, self.py))

    def resolve_player_position(self):
        box = self.player_hitbox()
        box = resolve_rect(box, all_obstacles())
        self.px = box.x - 6
        self.py = box.y - 6

    def resolve_boss_position(self):
        box = self.boss_hitbox()
        box = resolve_rect(box, all_obstacles())
        self.boss_x = box.x - 12
        self.boss_y = box.y - 12

    def try_spawn_croquette(self):
        if self.croquette is not None:
            return
        now = pygame.time.get_ticks()
        if now < self.next_croquette_ms:
            return
        for _ in range(40):
            x = random.randint(60, WIDTH - 90)
            y = random.randint(PLAY_TOP + 30, PLAY_BOTTOM)
            r = pygame.Rect(x, y, CROQUETTE_SIZE, CROQUETTE_SIZE)
            if any(r.colliderect(o) for o in all_obstacles()):
                continue
            cx, cy = self.player_center()
            if math.hypot(r.centerx - cx, r.centery - cy) < 100:
                continue
            bx, by = self.boss_center()
            if math.hypot(r.centerx - bx, r.centery - by) < 90:
                continue
            self.croquette = {"x": r.centerx, "y": r.centery}
            self.next_croquette_ms = now + CROQUETTE_SPAWN_MS
            return

    def try_pickup_croquette(self):
        if not self.croquette:
            return
        pr = self.player_hitbox()
        cr = pygame.Rect(
            self.croquette["x"] - CROQUETTE_SIZE // 2,
            self.croquette["y"] - CROQUETTE_SIZE // 2,
            CROQUETTE_SIZE,
            CROQUETTE_SIZE,
        )
        if pr.colliderect(cr):
            self.fear = max(0, self.fear - CROQUETTE_FEAR_HEAL)
            self.flemme = min(FLEMME_MAX, self.flemme + CROQUETTE_FLEMME_HEAL)
            self.croquette = None
            self.pickup_banner_ms = 1600

    def handle_input(self):
        self.moved_this_frame = False
        keys = pygame.key.get_pressed()
        on_couch = self.on_couch()
        want_hide = any(keys[k] for k in HIDE_KEYS)
        self.hiding = on_couch and want_hide

        if self.state != PLAYING or self.hiding:
            return

        if self.flemme < FLEMME_MIN_MOVE:
            return

        dx = 0
        dy = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_q] or keys[pygame.K_a]:
            dx -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += 1
        if keys[pygame.K_UP] or keys[pygame.K_z] or keys[pygame.K_w]:
            dy -= 1
        if not on_couch and (keys[pygame.K_DOWN] or keys[pygame.K_s]):
            dy += 1

        if dx or dy:
            length = math.hypot(dx, dy)
            dx /= length
            dy /= length
            self.px += dx * PLAYER_SPEED
            self.py += dy * PLAYER_SPEED
            self.clamp_player()
            self.resolve_player_position()
            self.flemme = max(0, self.flemme - FLEMME_MOVE_COST)
            self.moved_this_frame = True

    def is_counter_attack(self):
        now = pygame.time.get_ticks()
        if self.dist_boss_player() < COUNTER_TOUCH_DIST:
            return True
        return now - self.last_boss_touch_ms < COUNTER_WINDOW_MS

    def apply_boss_recoil(self):
        px, py = self.player_center()
        bx, by = self.boss_center()
        vx, vy = bx - px, by - py
        dist = math.hypot(vx, vy) or 1
        self.boss_recoil_ms = BOSS_RECOIL_MS
        self.boss_recoil_vx = vx / dist
        self.boss_recoil_vy = vy / dist
        self.counter_banner_ms = 1200

    def try_claw(self):
        if self.state != PLAYING or self.claw_cd > 0 or self.hiding:
            return
        if self.flemme < 15:
            return
        if self.dist_boss_player() > CLAW_RANGE + BOSS_W // 2:
            return
        counter = self.is_counter_attack()
        damage = CLAW_DAMAGE + (CLAW_COUNTER_BONUS if counter else 0)
        prev_hp = self.boss_hp
        self.boss_hp = max(0, self.boss_hp - damage)
        self.spawn_fur()
        if counter:
            self.apply_boss_recoil()
        self.claw_flash = 40
        self.claw_cd = CLAW_COOLDOWN_MS
        self.flemme = max(0, self.flemme - 8)
        if prev_hp > BOSS_PHASE_HP >= self.boss_hp:
            self.phase2_banner_ms = 2800
        if self.boss_hp <= 0:
            self.state = WIN

    def boss_can_move_to(self, nx, ny):
        box = pygame.Rect(nx + 12, ny + 12, BOSS_W - 24, BOSS_H - 24)
        return not any(box.colliderect(o) for o in all_obstacles())

    def fur_penalty_at(self, nx, ny):
        cx = nx + BOSS_W // 2
        cy = ny + BOSS_H // 2
        penalty = 0
        for p in self.living_fur():
            d = math.hypot(cx - p["x"], cy - p["y"])
            if d < FUR_RADIUS + 35:
                penalty += FUR_AVOID_PENALTY * (1 - d / (FUR_RADIUS + 35))
        return penalty

    def chase_target(self):
        px, py = self.player_center()
        pvx = px - self._prev_px
        pvy = py - self._prev_py
        self._prev_px, self._prev_py = px, py

        lead = BOSS_PREDICT_PHASE2 if self.boss_phase2() else BOSS_PREDICT_NORMAL
        tx = px + pvx * lead
        ty = py + pvy * lead

        if self.hiding:
            couch = couch_rect()
            tx = couch.centerx
            ty = couch.top - 35
        elif self.croquette:
            cx, cy = self.croquette["x"], self.croquette["y"]
            if math.hypot(px - cx, py - cy) < 130:
                tx = cx + (px - cx) * 0.4
                ty = cy + (py - cy) * 0.4

        return tx, ty

    def smart_boss_chase(self, speed):
        tx, ty = self.chase_target()
        bx, by = self.boss_center()
        dirs = []
        for deg in range(0, 360, 30):
            rad = math.radians(deg)
            dirs.append((math.cos(rad), math.sin(rad)))
        dx, dy = tx - bx, ty - by
        dist = math.hypot(dx, dy)
        if dist > 1:
            dirs.append((dx / dist, dy / dist))
            perp = (-dy / dist, dx / dist)
            dirs.extend([perp, (-perp[0], -perp[1])])

        if self._boss_stuck >= BOSS_STUCK_FRAMES:
            angle = random.uniform(0, math.pi * 2)
            dirs.insert(0, (math.cos(angle), math.sin(angle)))

        best_score = -1e9
        best_pos = None
        for ux, uy in dirs:
            for mult in (1.0, 0.55, 1.35):
                nx = self.boss_x + ux * speed * mult
                ny = self.boss_y + uy * speed * mult
                if not self.boss_can_move_to(nx, ny):
                    continue
                ncx = nx + BOSS_W // 2
                ncy = ny + BOSS_H // 2
                score = -math.hypot(tx - ncx, ty - ncy)
                score -= self.fur_penalty_at(nx, ny)
                if self.boss_on_fur() and self.fur_penalty_at(nx, ny) < self.fur_penalty_at(self.boss_x, self.boss_y):
                    score += 40
                if score > best_score:
                    best_score = score
                    best_pos = (nx, ny)

        if best_pos:
            self.boss_x, self.boss_y = best_pos
            moved = math.hypot(self.boss_x - self._last_bx, self.boss_y - self._last_by)
            if moved < 0.8:
                self._boss_stuck += 1
            else:
                self._boss_stuck = 0
            self._last_bx, self._last_by = self.boss_x, self.boss_y
        else:
            self._boss_stuck += 1

    def move_boss(self, dx, dy):
        if self.boss_can_move_to(self.boss_x + dx, self.boss_y + dy):
            self.boss_x += dx
            self.boss_y += dy
            return
        if self.boss_can_move_to(self.boss_x + dx, self.boss_y):
            self.boss_x += dx
        elif self.boss_can_move_to(self.boss_x, self.boss_y + dy):
            self.boss_y += dy

    def update_boss(self, dt):
        if self.state != PLAYING:
            return
        self.wobble += dt * (0.007 if self.boss_phase2() else 0.004)
        now = pygame.time.get_ticks()
        px, py = self.player_center()
        bx, by = self.boss_center()
        vx, vy = px - bx, py - by
        dist = math.hypot(vx, vy) or 1

        if self.boss_recoil_ms > 0:
            self.boss_recoil_ms = max(0, self.boss_recoil_ms - dt)
            self.move_boss(self.boss_recoil_vx * BOSS_RECOIL_SPEED, self.boss_recoil_vy * BOSS_RECOIL_SPEED)
        elif dist > 12:
            speed = BOSS_SPEED_PHASE2 if self.boss_phase2() else BOSS_SPEED
            if self.boss_on_fur():
                speed *= FUR_SLOW_MULT
            self.smart_boss_chase(speed)

        self.boss_x = max(40, min(WIDTH - BOSS_W - 40, self.boss_x))
        self.boss_y = max(PLAY_TOP - 20, min(PLAY_BOTTOM - 20, self.boss_y))
        self.resolve_boss_position()

        dist = self.dist_boss_player()
        if dist < 55:
            self.last_boss_touch_ms = now
        touch_rate = FEAR_TOUCH_RATE_PHASE2 if self.boss_phase2() else FEAR_TOUCH_RATE
        near_rate = FEAR_NEAR_RATE_PHASE2 if self.boss_phase2() else FEAR_NEAR_RATE
        if self.hiding:
            self.fear = max(0, self.fear + FEAR_HIDE_RATE)
        elif dist < 55:
            self.fear = min(FEAR_MAX, self.fear + touch_rate)
        elif dist < NEAR_RADIUS:
            self.fear = min(FEAR_MAX, self.fear + near_rate)
        else:
            self.fear = max(0, self.fear + FEAR_IDLE_RATE)

        if self.fear >= FEAR_MAX:
            self.state = LOSE

    def update_player(self, dt):
        if self.state != PLAYING:
            return
        if self.claw_cd > 0:
            self.claw_cd -= dt
        if self.claw_flash > 0:
            self.claw_flash -= 1
        if self.phase2_banner_ms > 0:
            self.phase2_banner_ms = max(0, self.phase2_banner_ms - dt)
        if self.counter_banner_ms > 0:
            self.counter_banner_ms = max(0, self.counter_banner_ms - dt)
        if self.pickup_banner_ms > 0:
            self.pickup_banner_ms = max(0, self.pickup_banner_ms - dt)
        self.try_spawn_croquette()
        self.try_pickup_croquette()
        self.living_fur()
        if not self.moved_this_frame and not self.hiding:
            self.flemme = min(FLEMME_MAX, self.flemme + FLEMME_REGEN)

    def draw_hud(self):
        draw_bar(
            self.screen,
            24,
            24,
            220,
            18,
            self.fear,
            FEAR_MAX,
            "Peur",
            (DANGER, (120, 50, 50)),
        )
        draw_bar(
            self.screen,
            24,
            68,
            220,
            18,
            self.flemme,
            FLEMME_MAX,
            "Flemme",
            ((80, 160, 220), (50, 90, 120)),
        )
        draw_bar(
            self.screen,
            WIDTH - 244,
            24,
            220,
            22,
            self.boss_hp,
            BOSS_MAX_HP,
            "Aspirateur",
            ((180, 60, 60), (100, 40, 40)),
        )
        hint = self.font_small.render(
            "ZQSD · Espace griffe · Contre si touché · Croquettes dorées",
            True,
            (180, 170, 160),
        )
        self.screen.blit(hint, (WIDTH // 2 - hint.get_width() // 2, HEIGHT - 28))
        if self.boss_phase2():
            turbo = self.font_small.render("PHASE 2 — TURBO", True, (255, 100, 80))
            self.screen.blit(turbo, (WIDTH - turbo.get_width() - 20, 52))

    def draw_menu(self):
        draw_gradient_bg(self.screen)
        t, pos = center_text(self.font_big, "Nahla vs l'aspirateur", 180, ACCENT)
        self.screen.blit(t, pos)
        lines = [
            "L'aspirateur rouge te traque dans le salon.",
            "Vide sa vie à coups de griffe.",
            "Meubles bloquent · croquettes dorées = soin.",
            "Griffe quand il te touche = CONTRE (recul + dégâts).",
            "",
            "ESPACE ou clic pour combattre",
        ]
        for i, line in enumerate(lines):
            s, p = center_text(self.font if i < 5 else self.font_big, line, 280 + i * 36)
            self.screen.blit(s, p)

    def draw_end(self, won):
        draw_gradient_bg(self.screen)
        msg = "Nahla a gagné. L'aspirateur est humilié." if won else "Peur max. Nahla fuit sous le lit."
        color = WIN_COLOR if won else DANGER
        t, pos = center_text(self.font_big, "Victoire !" if won else "Game Over", 220, color)
        self.screen.blit(t, pos)
        s, p = center_text(self.font, msg, 300)
        self.screen.blit(s, p)
        s2, p2 = center_text(self.font_small, "R pour rejouer · Échap pour quitter", 380)
        self.screen.blit(s2, p2)

    def draw_play(self):
        draw_gradient_bg(self.screen)
        couch = couch_rect()
        draw_couch(self.screen, couch, self.on_couch())
        draw_furniture(self.screen)
        now = pygame.time.get_ticks()
        draw_fur_patches(self.screen, self.living_fur(), now)
        if self.croquette:
            draw_croquette(self.screen, self.croquette["x"], self.croquette["y"], now * 0.006)
        draw_vacuum(
            self.screen,
            int(self.boss_x),
            int(self.boss_y),
            self.wobble,
            self.boss_phase2(),
            self.boss_eye_on(),
        )
        draw_nahla(
            self.screen,
            self.nahla_sprite,
            int(self.px),
            int(self.py),
            self.hiding,
            self.claw_flash,
        )
        self.draw_hud()
        if self.flemme < FLEMME_MIN_MOVE:
            warn, wp = center_text(self.font_small, "Trop fatiguée… repose-toi une seconde", 130, ACCENT)
            self.screen.blit(warn, wp)
        if self.phase2_banner_ms > 0:
            banner, bp = center_text(self.font_big, "TURBO ! L'aspirateur pète un câble !", 100, (255, 90, 70))
            self.screen.blit(banner, bp)
        if self.counter_banner_ms > 0:
            c, cp = center_text(self.font_big, "CONTRE !", 140, (255, 220, 100))
            self.screen.blit(c, cp)
        if self.pickup_banner_ms > 0:
            cr, crp = center_text(self.font, "Croquettes ! Peur ↓  Flemme ↑", 140, WIN_COLOR)
            self.screen.blit(cr, crp)

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
                    if event.key == pygame.K_r and self.state in (WIN, LOSE):
                        self.state = PLAYING
                        self.reset_run()
                    if event.key == pygame.K_SPACE:
                        if self.state == MENU:
                            self.state = PLAYING
                            self.reset_run()
                        elif self.state == PLAYING:
                            self.try_claw()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.state == MENU:
                        self.state = PLAYING
                        self.reset_run()
                    elif self.state == PLAYING:
                        self.try_claw()

            self.handle_input()
            self.update_boss(dt)
            self.update_player(dt)

            if self.state == MENU:
                self.draw_menu()
            elif self.state == PLAYING:
                self.draw_play()
            elif self.state == WIN:
                self.draw_play()
                self.draw_end(True)
            else:
                self.draw_play()
                self.draw_end(False)

            pygame.display.flip()


if __name__ == "__main__":
    Game().run()
