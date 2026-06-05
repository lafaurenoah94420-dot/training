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


def make_level():
    """Plateformes : (x, y, w, h, nom). y = haut de la plateforme."""
    floor_y = HEIGHT - 80
    platforms = [
        (0, floor_y, LEVEL_WIDTH, 80, "sol"),
        (180, floor_y - 95, 200, 28, "canapé"),
        (480, floor_y - 175, 160, 24, "étagère"),
        (780, floor_y - 240, 120, 140, "frigo"),
        (1020, floor_y - 130, 180, 22, "table"),
        (1380, floor_y - 200, 150, 26, "radiateur"),
        (1680, floor_y - 160, 220, 30, "canapé"),
        (2050, floor_y - 220, 140, 24, "étagère"),
        (2320, floor_y - 100, 200, 28, "lit"),
    ]
    croquettes = [
        (260, floor_y - 130),
        (540, floor_y - 210),
        (840, floor_y - 270),
        (1110, floor_y - 165),
        (1450, floor_y - 235),
        (1780, floor_y - 195),
        (2120, floor_y - 255),
        (2410, floor_y - 135),
        (150, floor_y - 40),
        (2550, floor_y - 40),
    ]
    aspirateurs = [
        {"x": 650, "y": floor_y - 48, "left": 420, "right": 950},
        {"x": 1550, "y": floor_y - 48, "left": 1200, "right": 1900},
        {"x": 1180, "y": floor_y - 168, "left": 1040, "right": 1180, "speed": 2.2},
    ]
    goal_x = LEVEL_WIDTH - 120
    return platforms, croquettes, aspirateurs, goal_x, floor_y


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


def update_player(player, keys, platforms, floor_y, jump_pressed):
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
    if player.rect.right > LEVEL_WIDTH:
        player.rect.right = LEVEL_WIDTH
    if player.rect.bottom > floor_y + 200:
        player.hp = 0


def draw_room(surf, camera_x, floor_y):
    surf.fill(SKY)
    for i in range(0, LEVEL_WIDTH, 120):
        px = i - camera_x % 120
        pygame.draw.rect(surf, WALL, (px, 0, 60, floor_y - 20))

    floor_rect = pygame.Rect(-camera_x, floor_y, LEVEL_WIDTH, HEIGHT - floor_y)
    pygame.draw.rect(surf, FLOOR, floor_rect)
    pygame.draw.rect(surf, FLOOR_TOP, (-camera_x, floor_y, LEVEL_WIDTH, 8))

    # tapis
    pygame.draw.rect(surf, (92, 62, 52), (-camera_x + 40, floor_y + 12, LEVEL_WIDTH - 80, 36), border_radius=4)


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


def draw_player(surf, player, camera_x, now):
    sx = player.rect.centerx - camera_x
    sy = player.rect.centery
    blink = now < player.invincible_until and (now // 80) % 2 == 0
    if not blink:
        img = player.sprite
        if player.facing < 0:
            img = pygame.transform.flip(img, True, False)
        surf.blit(img, (sx - NAHLA_DISPLAY // 2, sy - NAHLA_DISPLAY // 2 + 4))


def draw_hud(surf, font, score, total, hp, goal_hint):
    pygame.draw.rect(surf, (20, 18, 28, 180), (12, 12, 280, 72), border_radius=10)
    surf.blit(font.render(f"Croquettes : {score}/{total}", True, ACCENT), (24, 22))
    hearts = "♥ " * hp + "♡ " * (MAX_HP - hp)
    surf.blit(font.render(hearts.strip(), True, DANGER), (24, 48))
    if goal_hint:
        hint = font.render("→ Va jusqu'au lit !", True, TEXT)
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


def reset_game():
    platforms, croquettes, aspirateurs, goal_x, floor_y = make_level()
    player = Player(floor_y)
    collected = [False] * len(croquettes)
    for asp in aspirateurs:
        asp["dir"] = 1
        asp.setdefault("speed", ASPI_SPEED)
    return platforms, croquettes, aspirateurs, goal_x, floor_y, player, collected, 0


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("menlo,consolas,monospace", 22)
    big_font = pygame.font.SysFont("menlo,consolas,monospace", 42, bold=True)
    small_font = pygame.font.SysFont("menlo,consolas,monospace", 20)

    state = MENU
    platforms, croquettes, aspirateurs, goal_x, floor_y, player, collected, score = reset_game()
    camera_x = 0
    t0 = pygame.time.get_ticks()

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
                    platforms, croquettes, aspirateurs, goal_x, floor_y, player, collected, score = reset_game()
                if state in (WIN, LOSE) and event.key == pygame.K_r:
                    state = PLAYING
                    platforms, croquettes, aspirateurs, goal_x, floor_y, player, collected, score = reset_game()
                if state == PLAYING and event.key in JUMP_KEYS:
                    jump_pressed = True

        keys = pygame.key.get_pressed()
        if state == MENU and (keys[pygame.K_RETURN] or keys[pygame.K_SPACE]):
            state = PLAYING
            platforms, croquettes, aspirateurs, goal_x, floor_y, player, collected, score = reset_game()

        if state == PLAYING:
            update_player(player, keys, platforms, floor_y, jump_pressed)

            hitbox = pygame.Rect(player.rect.x + 8, player.rect.y + 8, PLAYER_W - 16, PLAYER_H - 12)
            for i, pos in enumerate(croquettes):
                if not collected[i]:
                    crect = pygame.Rect(pos[0] - CROQUETTE_R, pos[1] - CROQUETTE_R, CROQUETTE_R * 2, CROQUETTE_R * 2)
                    if hitbox.colliderect(crect):
                        collected[i] = True
                        score += CROQUETTE_POINTS

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

            if player.rect.right >= goal_x and score >= len(croquettes) // 2:
                state = WIN
            elif player.rect.right >= goal_x and score < len(croquettes) // 2:
                pass  # besoin de plus de croquettes — hint via HUD

            if player.hp <= 0:
                state = LOSE

            target_cam = player.rect.centerx - WIDTH // 2
            camera_x += (target_cam - camera_x) * 0.12
            camera_x = max(0, min(camera_x, LEVEL_WIDTH - WIDTH))

        # --- Dessin ---
        draw_room(screen, int(camera_x), floor_y)
        for plat in platforms:
            draw_platform(screen, plat, int(camera_x))
        for i, pos in enumerate(croquettes):
            draw_croquette(screen, pos, int(camera_x), collected[i], (now - t0) / 50)
        for asp in aspirateurs:
            draw_aspirateur(screen, asp, int(camera_x))

        if state != MENU:
            draw_player(screen, player, int(camera_x), now)

        # porte / lit objectif
        gx = goal_x - int(camera_x)
        pygame.draw.rect(screen, WIN_C, (gx, floor_y - 120, 40, 120), border_radius=4)
        pygame.draw.rect(screen, (140, 100, 180), (gx + 50, floor_y - 100, 160, 28), border_radius=6)

        goal_hint = state == PLAYING and player.rect.right < goal_x - 100
        draw_hud(screen, font, score, len(croquettes), player.hp, goal_hint)

        if state == MENU:
            draw_center_msg(
                screen, big_font, small_font, "Nahla platformer",
                ["Q/D ou flèches — gauche/droite", "Z ou Espace — sauter", "Croquettes + lit = victoire", "Entrée ou Espace — jouer"],
            )
        elif state == WIN:
            draw_center_msg(
                screen, big_font, small_font, "Sieste méritée !",
                [f"Score : {score}/{len(croquettes)} croquettes", "R — rejouer · Échap — quitter"],
            )
        elif state == LOSE:
            draw_center_msg(
                screen, big_font, small_font, "Aspirateur gagne...",
                ["Nahla furieuse.", "R ou Entrée — rejouer"],
            )

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
