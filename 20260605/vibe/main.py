"""Nahla platformer — sauts de meuble en meuble."""

import random
import sys
from pathlib import Path

import pygame

# --- Écran & monde ---
WIDTH, HEIGHT = 1024, 576
LEVEL_WIDTH = 2800
FPS = 60
TITLE = "Nahla platformer"

GRAVITY = 0.55
JUMP_FORCE = -13.5
MOVE_SPEED = 5.5
MAX_FALL = 14

PLAYER_W, PLAYER_H = 52, 44
NAHLA_DISPLAY = 56

CROQUETTE_R = 10
CROQUETTE_POINTS = 1
MAX_HP = 3
INVINCIBLE_MS = 1200
ASPI_SPEED = 2.8
KNOCKBACK = 9

# --- Couleurs ---
SKY = (72, 88, 110)
WALL = (88, 76, 68)
FLOOR = (58, 50, 44)
FLOOR_TOP = (78, 68, 58)
TEXT = (245, 238, 225)
ACCENT = (255, 168, 72)
DANGER = (220, 70, 70)
WIN_C = (100, 220, 140)
CROQUETTE_C = (255, 190, 60)
ASPI_C = (90, 90, 100)
ASPI_PIPE = (60, 60, 70)

MENU = "menu"
PLAYING = "playing"
LEVEL_CLEAR = "level_clear"
WIN = "win"
LOSE = "lose"

# AZERTY ZQSD + flèches + alternatives QWERTY
MOVE_LEFT_KEYS = (pygame.K_LEFT, pygame.K_q, pygame.K_a)
MOVE_RIGHT_KEYS = (pygame.K_RIGHT, pygame.K_d)
JUMP_KEYS = (pygame.K_SPACE, pygame.K_UP, pygame.K_z, pygame.K_w)

ASSETS = Path(__file__).parent
NAHLA_HEAD = ASSETS / "nahla_head.png"
NAHLA_PHOTO = ASSETS / "WhatsApp Image 2026-04-24 at 00.18.56.jpeg"
CROP = (0.24, 0.12, 0.52, 0.40)

PLATFORM_COLORS = {
    "canapé": ((120, 72, 88), (100, 58, 72)),
    "étagère": ((95, 70, 48), (75, 55, 38)),
    "frigo": ((200, 210, 220), (170, 180, 190)),
    "table": ((110, 82, 58), (90, 66, 46)),
    "radiateur": ((150, 150, 155), (120, 120, 125)),
    "lit": ((100, 90, 130), (80, 72, 108)),
    "plan": ((180, 175, 168), (150, 145, 138)),
    "évier": ((160, 175, 190), (130, 145, 160)),
    "banc": ((90, 75, 60), (70, 58, 46)),
}


def load_nahla_sprite():
    if NAHLA_HEAD.exists():
        img = pygame.image.load(str(NAHLA_HEAD)).convert_alpha()
    elif NAHLA_PHOTO.exists():
        full = pygame.image.load(str(NAHLA_PHOTO)).convert()
        w, h = full.get_size()
        cx, cy, cw, ch = CROP
        rect = pygame.Rect(int(w * cx), int(h * cy), int(w * cw), int(h * ch))
        img = full.subsurface(rect).copy()
    else:
        surf = pygame.Surface((NAHLA_DISPLAY, NAHLA_DISPLAY), pygame.SRCALPHA)
        pygame.draw.ellipse(surf, ACCENT, surf.get_rect())
        return surf
    return pygame.transform.smoothscale(img, (NAHLA_DISPLAY, NAHLA_DISPLAY))


def level_salon(floor_y):
    width = 2800
    platforms = [
        (0, floor_y, width, 80, "sol"),
        (200, floor_y - 100, 170, 26, "canapé"),
        (520, floor_y - 185, 130, 22, "étagère"),
        (820, floor_y - 255, 110, 140, "frigo"),
        (1080, floor_y - 140, 150, 20, "table"),
        (1420, floor_y - 215, 130, 24, "radiateur"),
        (1720, floor_y - 175, 190, 28, "canapé"),
        (2120, floor_y - 240, 120, 22, "étagère"),
        (2380, floor_y - 105, 180, 26, "lit"),
    ]
    croquettes = [
        (280, floor_y - 135),
        (580, floor_y - 220),
        (880, floor_y - 290),
        (1160, floor_y - 175),
        (1500, floor_y - 250),
        (1840, floor_y - 210),
        (2200, floor_y - 275),
        (2480, floor_y - 140),
        (160, floor_y - 40),
        (2580, floor_y - 40),
    ]
    aspirateurs = [
        {"x": 650, "y": floor_y - 48, "left": 380, "right": 980, "speed": 3.4},
        {"x": 1350, "y": floor_y - 48, "left": 1050, "right": 1750, "speed": 3.5},
        {"x": 2050, "y": floor_y - 48, "left": 1780, "right": 2350, "speed": 3.3},
        {"x": 1180, "y": floor_y - 175, "left": 1080, "right": 1320, "speed": 2.9},
    ]
    return {
        "name": "Salon",
        "width": width,
        "min_croquettes": 7,
        "sky": (72, 88, 110),
        "wall": (88, 76, 68),
        "floor": FLOOR,
        "floor_top": FLOOR_TOP,
        "rug": (92, 62, 52),
        "platforms": platforms,
        "croquettes": croquettes,
        "aspirateurs": aspirateurs,
        "goal_x": width - 120,
        "floor_y": floor_y,
    }


def level_cuisine(floor_y):
    width = 3000
    platforms = [
        (0, floor_y, width, 80, "sol"),
        (140, floor_y - 95, 120, 24, "banc"),
        (400, floor_y - 168, 95, 20, "étagère"),
        (620, floor_y - 218, 80, 130, "frigo"),
        (780, floor_y - 125, 130, 22, "plan"),
        (1040, floor_y - 198, 85, 18, "étagère"),
        (1240, floor_y - 268, 110, 26, "plan"),
        (1480, floor_y - 172, 140, 20, "table"),
        (1760, floor_y - 238, 100, 22, "étagère"),
        (2000, floor_y - 152, 120, 24, "évier"),
        (2260, floor_y - 218, 150, 22, "table"),
        (2520, floor_y - 115, 180, 26, "lit"),
    ]
    croquettes = [
        (220, floor_y - 130),
        (450, floor_y - 205),
        (660, floor_y - 255),
        (860, floor_y - 160),
        (1120, floor_y - 235),
        (1320, floor_y - 305),
        (1580, floor_y - 205),
        (1840, floor_y - 270),
        (2080, floor_y - 185),
        (2380, floor_y - 255),
        (2680, floor_y - 150),
    ]
    aspirateurs = [
        {"x": 500, "y": floor_y - 48, "left": 280, "right": 720, "speed": 3.8},
        {"x": 1050, "y": floor_y - 48, "left": 820, "right": 1280, "speed": 4.0},
        {"x": 1700, "y": floor_y - 48, "left": 1450, "right": 2000, "speed": 4.0},
        {"x": 2300, "y": floor_y - 48, "left": 2050, "right": 2550, "speed": 3.9},
        {"x": 1320, "y": floor_y - 208, "left": 1240, "right": 1480, "speed": 3.5},
        {"x": 1880, "y": floor_y - 208, "left": 1760, "right": 2020, "speed": 3.6},
    ]
    return {
        "name": "Cuisine",
        "width": width,
        "min_croquettes": 8,
        "sky": (58, 72, 88),
        "wall": (76, 68, 62),
        "floor": (52, 48, 44),
        "floor_top": (72, 66, 58),
        "rug": (68, 58, 50),
        "platforms": platforms,
        "croquettes": croquettes,
        "aspirateurs": aspirateurs,
        "goal_x": width - 120,
        "floor_y": floor_y,
    }


def level_couloir(floor_y):
    width = 3400
    platforms = [
        (0, floor_y, width, 80, "sol"),
        (120, floor_y - 78, 75, 20, "radiateur"),
        (320, floor_y - 152, 65, 18, "étagère"),
        (510, floor_y - 228, 60, 16, "table"),
        (720, floor_y - 142, 85, 20, "banc"),
        (940, floor_y - 218, 65, 18, "étagère"),
        (1150, floor_y - 292, 75, 16, "table"),
        (1380, floor_y - 195, 95, 20, "radiateur"),
        (1620, floor_y - 268, 65, 16, "étagère"),
        (1860, floor_y - 172, 110, 22, "canapé"),
        (2120, floor_y - 248, 70, 18, "table"),
        (2340, floor_y - 318, 75, 16, "étagère"),
        (2560, floor_y - 205, 100, 20, "banc"),
        (2780, floor_y - 278, 65, 16, "table"),
        (2980, floor_y - 160, 140, 24, "canapé"),
        (3180, floor_y - 105, 200, 26, "lit"),
    ]
    croquettes = [
        (160, floor_y - 110),
        (360, floor_y - 185),
        (550, floor_y - 260),
        (770, floor_y - 175),
        (990, floor_y - 250),
        (1180, floor_y - 325),
        (1450, floor_y - 230),
        (1700, floor_y - 300),
        (1940, floor_y - 205),
        (2200, floor_y - 280),
        (2420, floor_y - 350),
        (2640, floor_y - 240),
        (2860, floor_y - 310),
        (3060, floor_y - 195),
        (3280, floor_y - 140),
    ]
    aspirateurs = [
        {"x": 400, "y": floor_y - 48, "left": 180, "right": 620, "speed": 4.2},
        {"x": 850, "y": floor_y - 48, "left": 650, "right": 1050, "speed": 4.4},
        {"x": 1300, "y": floor_y - 48, "left": 1080, "right": 1550, "speed": 4.5},
        {"x": 1750, "y": floor_y - 48, "left": 1500, "right": 2000, "speed": 4.6},
        {"x": 1120, "y": floor_y - 228, "left": 1060, "right": 1280, "speed": 4.0},
        {"x": 1580, "y": floor_y - 228, "left": 1520, "right": 1740, "speed": 4.1},
        {"x": 2280, "y": floor_y - 48, "left": 2000, "right": 2550, "speed": 4.8},
        {"x": 2680, "y": floor_y - 258, "left": 2560, "right": 2820, "speed": 4.3},
    ]
    return {
        "name": "Couloir",
        "width": width,
        "min_croquettes": 12,
        "sky": (48, 52, 68),
        "wall": (62, 58, 72),
        "floor": (46, 42, 50),
        "floor_top": (66, 60, 68),
        "rug": (58, 52, 60),
        "platforms": platforms,
        "croquettes": croquettes,
        "aspirateurs": aspirateurs,
        "goal_x": width - 120,
        "floor_y": floor_y,
    }


LEVELS = [level_salon, level_cuisine, level_couloir, None]  # boss filled below


def level_boss(floor_y):
    width = WIDTH
    platforms = [
        (0, floor_y, width, 80, "sol"),
        (100, floor_y - 105, 170, 26, "canapé"),
        (width // 2 - 110, floor_y - 175, 220, 28, "table"),
        (width - 300, floor_y - 95, 150, 24, "étagère"),
    ]
    croquettes = [
        (180, floor_y - 140),
        (width // 2, floor_y - 210),
        (width - 220, floor_y - 130),
    ]
    return {
        "name": "Boss — Méga aspirateur",
        "width": width,
        "min_croquettes": 0,
        "is_boss": True,
        "sky": (32, 28, 42),
        "wall": (48, 42, 58),
        "floor": (40, 36, 48),
        "floor_top": (62, 54, 68),
        "rug": (50, 44, 56),
        "platforms": platforms,
        "croquettes": croquettes,
        "aspirateurs": [],
        "goal_x": width + 999,
        "floor_y": floor_y,
        "boss_template": {
            "x": width // 2 + 60,
            "y": floor_y - 10,
            "w": 180,
            "h": 145,
            "hp": 8,
            "max_hp": 8,
            "dir": -1,
            "speed": 1.9,
            "left": 340,
            "right": width - 260,
            "stomp_immune_until": 0,
        },
    }


LEVELS[3] = level_boss


def load_level(level_index):
    floor_y = HEIGHT - 80
    data = LEVELS[level_index](floor_y)
    aspirateurs = []
    for asp in data["aspirateurs"]:
        copy = dict(asp)
        copy["dir"] = 1
        aspirateurs.append(copy)
    collected = [False] * len(data["croquettes"])
    boss = None
    if data.get("is_boss"):
        boss = dict(data["boss_template"])
    return data, aspirateurs, collected, boss


class Player:
    def __init__(self, floor_y):
        self.rect = pygame.Rect(80, floor_y - PLAYER_H - 5, PLAYER_W, PLAYER_H)
        self.vel_x = 0.0
        self.vel_y = 0.0
        self.on_ground = True
        self.facing = 1
        self.hp = MAX_HP
        self.invincible_until = 0
        self.sprite = load_nahla_sprite()

    def reset(self, floor_y):
        self.rect.topleft = (80, floor_y - PLAYER_H - 5)
        self.vel_x = 0.0
        self.vel_y = 0.0
        self.on_ground = True
        self.hp = MAX_HP
        self.invincible_until = 0


def rects_overlap(a, b):
    return a.colliderect(b)


def resolve_platform(player, plat_rect):
    """Collision AABB simple — atterrissage / tête / côtés."""
    if not player.rect.colliderect(plat_rect):
        return

    overlap_left = player.rect.right - plat_rect.left
    overlap_right = plat_rect.right - player.rect.left
    overlap_top = player.rect.bottom - plat_rect.top
    overlap_bottom = plat_rect.bottom - player.rect.top

    min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)

    if min_overlap == overlap_top and player.vel_y >= 0:
        player.rect.bottom = plat_rect.top
        player.vel_y = 0
        player.on_ground = True
    elif min_overlap == overlap_bottom and player.vel_y < 0:
        player.rect.top = plat_rect.bottom
        player.vel_y = 0
    elif min_overlap == overlap_left:
        player.rect.right = plat_rect.left
        player.vel_x = 0
    elif min_overlap == overlap_right:
        player.rect.left = plat_rect.right
        player.vel_x = 0


def key_down(keys, key_codes):
    return any(keys[k] for k in key_codes)


def update_player(player, keys, platforms, floor_y, level_width, jump_pressed):
    was_on_ground = player.on_ground
    player.on_ground = False

    move = 0
    if key_down(keys, MOVE_LEFT_KEYS):
        move -= 1
    if key_down(keys, MOVE_RIGHT_KEYS):
        move += 1

    player.vel_x = move * MOVE_SPEED
    if move != 0:
        player.facing = move

    wants_jump = jump_pressed or key_down(keys, JUMP_KEYS)
    if wants_jump and was_on_ground:
        player.vel_y = JUMP_FORCE

    player.vel_y += GRAVITY
    if player.vel_y > MAX_FALL:
        player.vel_y = MAX_FALL

    player.rect.x += int(player.vel_x)
    for plat in platforms:
        pr = pygame.Rect(plat[0], plat[1], plat[2], plat[3])
        resolve_platform(player, pr)

    player.rect.y += int(player.vel_y)
    for plat in platforms:
        pr = pygame.Rect(plat[0], plat[1], plat[2], plat[3])
        resolve_platform(player, pr)

    if player.rect.left < 0:
        player.rect.left = 0
    if player.rect.right > level_width:
        player.rect.right = level_width
    if player.rect.bottom > floor_y + 200:
        player.hp = 0


def draw_room(surf, camera_x, level):
    floor_y = level["floor_y"]
    level_width = level["width"]
    surf.fill(level["sky"])
    for i in range(0, level_width, 120):
        px = i - camera_x % 120
        pygame.draw.rect(surf, level["wall"], (px, 0, 60, floor_y - 20))

    floor_rect = pygame.Rect(-camera_x, floor_y, level_width, HEIGHT - floor_y)
    pygame.draw.rect(surf, level["floor"], floor_rect)
    pygame.draw.rect(surf, level["floor_top"], (-camera_x, floor_y, level_width, 8))

    pygame.draw.rect(surf, level["rug"], (-camera_x + 40, floor_y + 12, level_width - 80, 36), border_radius=4)


def draw_platform(surf, plat, camera_x):
    x, y, w, h, name = plat
    sx = x - camera_x
    if name == "sol":
        return
    if name == "frigo":
        body = pygame.Rect(sx, y, w, h)
        pygame.draw.rect(surf, PLATFORM_COLORS[name][0], body, border_radius=6)
        pygame.draw.line(surf, (140, 150, 160), (sx + w // 2, y + 8), (sx + w // 2, y + h - 8), 2)
        return
    colors = PLATFORM_COLORS.get(name, ((100, 100, 100), (80, 80, 80)))
    pygame.draw.rect(surf, colors[1], (sx, y + h - 8, w, 8), border_radius=3)
    pygame.draw.rect(surf, colors[0], (sx, y, w, h - 8), border_radius=6)
    if name == "canapé":
        pygame.draw.rect(surf, colors[0], (sx + 8, y - 14, w - 16, 18), border_radius=8)


def draw_croquette(surf, pos, camera_x, collected, t):
    if collected:
        return
    cx, cy = pos[0] - camera_x, pos[1]
    pulse = int(3 * abs(pygame.math.Vector2(1, 0).rotate(t * 4).x))
    pygame.draw.circle(surf, (200, 140, 40), (cx, cy + 2), CROQUETTE_R + pulse // 2)
    pygame.draw.circle(surf, CROQUETTE_C, (cx, cy), CROQUETTE_R + pulse // 2)


def draw_aspirateur(surf, asp, camera_x):
    x = int(asp["x"] - camera_x)
    y = int(asp["y"])
    body = pygame.Rect(x - 28, y - 32, 56, 40)
    pygame.draw.rect(surf, ASPI_C, body, border_radius=8)
    pygame.draw.rect(surf, ASPI_PIPE, (x + 18, y - 48, 14, 20), border_radius=4)
    pygame.draw.circle(surf, DANGER, (x - 12, y - 12), 6)
    pygame.draw.circle(surf, DANGER, (x + 12, y - 12), 6)


def draw_giant_boss(surf, boss, camera_x, now):
    x = int(boss["x"] - camera_x)
    y = int(boss["y"])
    w, h = boss["w"], boss["h"]
    pulse = abs(pygame.math.Vector2(1, 0).rotate(now / 12).x)

    shadow = pygame.Rect(x - w // 2 + 8, y - h + 12, w, h - 10)
    pygame.draw.ellipse(surf, (20, 18, 28), shadow)

    body = pygame.Rect(x - w // 2, y - h, w, h - 30)
    pygame.draw.rect(surf, (70, 70, 82), body, border_radius=22)
    pygame.draw.rect(surf, (50, 50, 60), (x - w // 2 + 12, y - h + 20, w - 24, h - 55), border_radius=14)

    pipe = pygame.Rect(x + w // 4 - 20, y - h - 55, 36, 70)
    pygame.draw.rect(surf, ASPI_PIPE, pipe, border_radius=10)
    pygame.draw.rect(surf, (40, 40, 48), (x + w // 4 - 8, y - h - 75, 14, 24), border_radius=6)

    eye_glow = int(180 + 60 * pulse)
    pygame.draw.circle(surf, (eye_glow, 40, 40), (x - 38, y - h + 42), 16)
    pygame.draw.circle(surf, (eye_glow, 40, 40), (x + 38, y - h + 42), 16)
    pygame.draw.circle(surf, (255, 80, 80), (x - 38, y - h + 42), 8)
    pygame.draw.circle(surf, (255, 80, 80), (x + 38, y - h + 42), 8)

    pygame.draw.rect(surf, DANGER, (x - w // 2 + 20, y - 28, w - 40, 18), border_radius=6)

    bar_w = w + 40
    bx = x - bar_w // 2
    by = y - h - 90
    pygame.draw.rect(surf, (30, 28, 38), (bx, by, bar_w, 14), border_radius=6)
    ratio = boss["hp"] / boss["max_hp"]
    pygame.draw.rect(surf, DANGER, (bx + 2, by + 2, int((bar_w - 4) * ratio), 10), border_radius=4)


def boss_rects(boss):
    x, y, w, h = boss["x"], boss["y"], boss["w"], boss["h"]
    body = pygame.Rect(x - w // 2 + 20, y - h + 40, w - 40, h - 55)
    stomp_zone = pygame.Rect(x - w // 2 + 10, y - h - 5, w - 20, 50)
    head_platform = pygame.Rect(x - 72, y - h - 6, 144, 14)
    return body, stomp_zone, head_platform


def boss_head_platform(boss):
  x, y, w, h = boss["x"], boss["y"], boss["w"], boss["h"]
  return (x - 72, y - h - 6, 144, 14, "table")


def move_boss(boss):
    rage = 1 + (boss["max_hp"] - boss["hp"]) * 0.12
    speed = boss["speed"] * rage
    boss["x"] += boss["dir"] * speed
    if boss["x"] <= boss["left"]:
        boss["x"] = boss["left"]
        boss["dir"] = 1
    if boss["x"] >= boss["right"]:
        boss["x"] = boss["right"]
        boss["dir"] = -1


def update_boss(boss, player, now, jump_pressed=False):
    hitbox = pygame.Rect(player.rect.x + 8, player.rect.y + 8, PLAYER_W - 16, PLAYER_H - 12)
    body, stomp_zone, _ = boss_rects(boss)
    on_head = hitbox.colliderect(stomp_zone)
    can_stomp = now >= boss["stomp_immune_until"]

    # Dégâts : saute sur la tête OU Espace en étant sur la tête
    if on_head and can_stomp and (player.vel_y > 0 or jump_pressed):
        boss["hp"] -= 1
        boss["stomp_immune_until"] = now + 500
        player.vel_y = JUMP_FORCE * 0.85
        player.on_ground = False
        player.invincible_until = now + 450
        return boss["hp"] <= 0

    if now >= player.invincible_until and hitbox.colliderect(body):
        player.hp -= 1
        player.invincible_until = now + INVINCIBLE_MS
        player.vel_y = JUMP_FORCE * 0.35
        player.vel_x = (1 if player.rect.centerx < boss["x"] else -1) * KNOCKBACK

    return False


def draw_player(surf, player, camera_x, now):
    sx = player.rect.centerx - camera_x
    sy = player.rect.centery
    blink = now < player.invincible_until and (now // 80) % 2 == 0
    if not blink:
        img = player.sprite
        if player.facing < 0:
            img = pygame.transform.flip(img, True, False)
        surf.blit(img, (sx - NAHLA_DISPLAY // 2, sy - NAHLA_DISPLAY // 2 + 4))


def draw_hud(surf, font, score, total, hp, goal_hint, level_index, level_name, min_needed, boss=None):
    pygame.draw.rect(surf, (20, 18, 28, 180), (12, 12, 360, 96), border_radius=10)
    surf.blit(font.render(f"Niveau {level_index + 1}/{len(LEVELS)} — {level_name}", True, TEXT), (24, 18))
    if boss is not None:
        surf.blit(font.render(f"Boss : {boss['hp']}/{boss['max_hp']} PV", True, DANGER), (24, 44))
        surf.blit(font.render("Saute sur sa tête ou Espace !", True, ACCENT), (24, 70))
    else:
        surf.blit(font.render(f"Croquettes : {score}/{total} (min {min_needed})", True, ACCENT), (24, 44))
        hearts = "♥ " * hp + "♡ " * (MAX_HP - hp)
        surf.blit(font.render(hearts.strip(), True, DANGER), (24, 70))
    if boss is not None and hp < MAX_HP:
        hearts = "♥ " * hp + "♡ " * (MAX_HP - hp)
        surf.blit(font.render(hearts.strip(), True, DANGER), (260, 44))
    if goal_hint:
        hint = font.render("→ Va jusqu'au lit !", True, TEXT)
        surf.blit(hint, (WIDTH - hint.get_width() - 20, 20))
    if boss is not None:
        hint = font.render("Écrase le Méga aspirateur !", True, TEXT)
        surf.blit(hint, (WIDTH - hint.get_width() - 20, 20))


def draw_center_msg(surf, big_font, small_font, title, lines):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((10, 8, 16, 170))
    surf.blit(overlay, (0, 0))
    t = big_font.render(title, True, TEXT)
    surf.blit(t, (WIDTH // 2 - t.get_width() // 2, HEIGHT // 2 - 80))
    for i, line in enumerate(lines):
        s = small_font.render(line, True, TEXT)
        surf.blit(s, (WIDTH // 2 - s.get_width() // 2, HEIGHT // 2 - 20 + i * 32))


def reset_game(level_index=0, keep_hp=None):
    level, aspirateurs, collected, boss = load_level(level_index)
    player = Player(level["floor_y"])
    if keep_hp is not None:
        player.hp = min(keep_hp, MAX_HP)
    return level, aspirateurs, collected, boss, player, level_index, 0


def start_level(level_index, keep_hp=None):
    level, aspirateurs, collected, boss, player, _, _ = reset_game(level_index, keep_hp=keep_hp)
    return level, aspirateurs, collected, boss, player, level_index, 0


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("menlo,consolas,monospace", 22)
    big_font = pygame.font.SysFont("menlo,consolas,monospace", 42, bold=True)
    small_font = pygame.font.SysFont("menlo,consolas,monospace", 20)

    state = MENU
    level, aspirateurs, collected, boss, player, level_index, score = reset_game(0)
    camera_x = 0
    t0 = pygame.time.get_ticks()
    total_croquettes = 0
    is_boss_level = False

    running = True
    while running:
        now = pygame.time.get_ticks()
        clock.tick(FPS)
        jump_pressed = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if state in (MENU, WIN, LOSE) and event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    state = PLAYING
                    level, aspirateurs, collected, boss, player, level_index, score = reset_game(0)
                    total_croquettes = 0
                if state in (WIN, LOSE) and event.key == pygame.K_r:
                    state = PLAYING
                    level, aspirateurs, collected, boss, player, level_index, score = reset_game(0)
                    total_croquettes = 0
                if state == LEVEL_CLEAR and event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    level, aspirateurs, collected, boss, player, level_index, score = start_level(
                        level_index, keep_hp=player.hp
                    )
                    state = PLAYING
                    camera_x = 0
                if state == PLAYING and event.key in JUMP_KEYS:
                    jump_pressed = True

        keys = pygame.key.get_pressed()
        if state == MENU and (keys[pygame.K_RETURN] or keys[pygame.K_SPACE]):
            state = PLAYING
            level, aspirateurs, collected, boss, player, level_index, score = reset_game(0)
            total_croquettes = 0

        platforms = level["platforms"]
        croquettes = level["croquettes"]
        goal_x = level["goal_x"]
        floor_y = level["floor_y"]
        level_width = level["width"]
        min_needed = level.get("min_croquettes", len(croquettes) // 2 + 1)
        is_boss_level = level.get("is_boss", False)

        if state == PLAYING:
            if is_boss_level and boss is not None:
                move_boss(boss)

            physics_platforms = list(platforms)
            if is_boss_level and boss is not None:
                physics_platforms.append(boss_head_platform(boss))

            update_player(player, keys, physics_platforms, floor_y, level_width, jump_pressed)

            hitbox = pygame.Rect(player.rect.x + 8, player.rect.y + 8, PLAYER_W - 16, PLAYER_H - 12)
            for i, pos in enumerate(croquettes):
                if not collected[i]:
                    crect = pygame.Rect(pos[0] - CROQUETTE_R, pos[1] - CROQUETTE_R, CROQUETTE_R * 2, CROQUETTE_R * 2)
                    if hitbox.colliderect(crect):
                        collected[i] = True
                        score += CROQUETTE_POINTS
                        if is_boss_level and boss is not None and boss["hp"] > 0:
                            boss["hp"] = max(0, boss["hp"] - 2)

            if is_boss_level and boss is not None:
                boss_defeated = update_boss(boss, player, now, jump_pressed=jump_pressed)
                if boss_defeated:
                    state = WIN
                if player.hp <= 0:
                    state = LOSE
            else:
                for asp in aspirateurs:
                    asp["x"] += asp["dir"] * asp["speed"]
                    if asp["x"] <= asp["left"]:
                        asp["x"] = asp["left"]
                        asp["dir"] = 1
                    if asp["x"] >= asp["right"]:
                        asp["x"] = asp["right"]
                        asp["dir"] = -1
                    arect = pygame.Rect(asp["x"] - 26, asp["y"] - 30, 52, 38)
                    if now >= player.invincible_until and hitbox.colliderect(arect):
                        player.hp -= 1
                        player.invincible_until = now + INVINCIBLE_MS
                        player.vel_y = JUMP_FORCE * 0.45
                        player.vel_x = -asp["dir"] * KNOCKBACK
                        if player.hp <= 0:
                            state = LOSE

                if player.rect.right >= goal_x and score >= min_needed:
                    total_croquettes += score
                    if level_index >= len(LEVELS) - 1:
                        state = WIN
                    else:
                        level_index += 1
                        state = LEVEL_CLEAR
                elif player.rect.right >= goal_x and score < min_needed:
                    pass

                if player.hp <= 0:
                    state = LOSE

            if is_boss_level:
                camera_x = 0
            else:
                target_cam = player.rect.centerx - WIDTH // 2
                camera_x += (target_cam - camera_x) * 0.12
                camera_x = max(0, min(camera_x, level_width - WIDTH))

        # --- Dessin ---
        draw_room(screen, int(camera_x), level)
        for plat in platforms:
            draw_platform(screen, plat, int(camera_x))
        if is_boss_level and boss is not None:
            draw_platform(screen, boss_head_platform(boss), int(camera_x))
        for i, pos in enumerate(croquettes):
            draw_croquette(screen, pos, int(camera_x), collected[i], (now - t0) / 50)
        for asp in aspirateurs:
            draw_aspirateur(screen, asp, int(camera_x))
        if boss is not None:
            draw_giant_boss(screen, boss, int(camera_x), now)

        if state != MENU:
            draw_player(screen, player, int(camera_x), now)

        if not is_boss_level:
            gx = goal_x - int(camera_x)
            pygame.draw.rect(screen, WIN_C, (gx, floor_y - 120, 40, 120), border_radius=4)
            pygame.draw.rect(screen, (140, 100, 180), (gx + 50, floor_y - 100, 160, 28), border_radius=6)

        goal_hint = state == PLAYING and not is_boss_level and player.rect.right < goal_x - 100
        draw_hud(screen, font, score, len(croquettes), player.hp, goal_hint, level_index, level["name"], min_needed, boss)

        if state == MENU:
            draw_center_msg(
                screen, big_font, small_font, "Nahla platformer",
                [
                    "4 niveaux — Boss : Méga aspirateur",
                    "Q/D ou flèches — bouger · Z ou Espace — sauter",
                    "Croquettes + lit · Boss : saute sur sa tête",
                    "Entrée ou Espace — jouer",
                ],
            )
        elif state == LEVEL_CLEAR:
            next_name = LEVELS[level_index](floor_y)["name"]
            draw_center_msg(
                screen, big_font, small_font, f"{level['name']} terminé !",
                [
                    f"Croquettes : {score}/{len(croquettes)} (il en fallait {min_needed})",
                    f"Prochain : {next_name} (plus dur)",
                    "Espace — continuer",
                ],
            )
        elif state == WIN:
            draw_center_msg(
                screen, big_font, small_font, "Nahla règne sur l'appart !",
                [
                    f"Total croquettes : {total_croquettes}",
                    "Le Méga aspirateur est détruit. Sieste méritée.",
                    "R — rejouer · Échap — quitter",
                ],
            )
        elif state == LOSE:
            draw_center_msg(
                screen, big_font, small_font, "Aspirateur gagne...",
                [f"Perdu au niveau {level_index + 1} — {level['name']}", "R ou Entrée — recommencer"],
            )

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
