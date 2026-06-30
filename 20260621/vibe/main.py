"""Nahla vs Zombies — tire des croquettes sur les zombies."""

import math
import random
import sys
from pathlib import Path

import pygame

# --- Fenêtre ---
WIDTH, HEIGHT = 1280, 720
FPS = 60
TITLE = "Nahla vs Zombies"

ASSETS = Path(__file__).parent
NAHLA_IMG = ASSETS / "nahla_head.png"

# --- États ---
MENU = "menu"
PLAYING = "playing"
OVER = "over"

# --- Couleurs ---
BG = (18, 22, 16)
FLOOR = (32, 42, 28)
TEXT = (245, 238, 225)
MUTED = (140, 150, 130)
ACCENT = (255, 168, 72)
DANGER = (200, 60, 60)
ZOMBIE = (80, 140, 70)
CROQUETTE = (210, 140, 50)

NAHLA_SPEED = 5.5
NAHLA_R = 36
BULLET_SPEED = 14
BULLET_R = 8
ZOMBIE_R = 22
ZOMBIE_SPEED = 1.8
SPAWN_MS = 1100
MAX_ZOMBIES = 65
SPAWN_BURST_WAVE = 3
LIVES_START = 3
HIT_COOLDOWN_MS = 1200
SHOOT_COOLDOWN_MS = 220
AIM_LINE_LEN = 100

# type → stats (r, hp, speed, couleur, score)
ZOMBIE_TYPES = {
    "lambda": {
        "name": "Lambda",
        "r": 20,
        "hp": 1,
        "speed": 1.7,
        "color": (80, 140, 70),
        "border": (40, 70, 35),
        "score": 10,
    },
    "sprinter": {
        "name": "Sprinter",
        "r": 15,
        "hp": 1,
        "speed": 3.4,
        "color": (160, 200, 60),
        "border": (90, 120, 30),
        "score": 20,
    },
    "tank": {
        "name": "Tank",
        "r": 34,
        "hp": 5,
        "speed": 0.9,
        "color": (45, 75, 40),
        "border": (25, 45, 22),
        "score": 40,
    },
    "fou": {
        "name": "Fou",
        "r": 18,
        "hp": 2,
        "speed": 2.6,
        "color": (130, 70, 150),
        "border": (80, 40, 100),
        "score": 25,
    },
    "geant": {
        "name": "Géant",
        "r": 42,
        "hp": 8,
        "speed": 0.7,
        "color": (60, 50, 90),
        "border": (35, 30, 55),
        "score": 80,
    },
}

MOVE_LEFT = (pygame.K_LEFT, pygame.K_q, pygame.K_a)
MOVE_RIGHT = (pygame.K_RIGHT, pygame.K_d)
MOVE_UP = (pygame.K_UP, pygame.K_z, pygame.K_w)
MOVE_DOWN = (pygame.K_DOWN, pygame.K_s)


def pressed(keys, key_group):
    return any(keys[k] for k in key_group)


def load_nahla():
    if NAHLA_IMG.exists():
        img = pygame.image.load(str(NAHLA_IMG)).convert_alpha()
        return pygame.transform.smoothscale(img, (NAHLA_R * 2, NAHLA_R * 2))
    surf = pygame.Surface((NAHLA_R * 2, NAHLA_R * 2), pygame.SRCALPHA)
    pygame.draw.circle(surf, ACCENT, (NAHLA_R, NAHLA_R), NAHLA_R)
    return surf


def pick_zombie_type(wave):
    pool = ["lambda", "lambda", "lambda"]
    if wave >= 2:
        pool += ["sprinter", "sprinter"]
    if wave >= 3:
        pool += ["tank", "fou"]
    if wave >= 5:
        pool += ["fou", "sprinter"]
    if wave >= 4:
        pool += ["geant"]
    if wave >= 10:
        pool += ["tank", "geant"]
    return random.choice(pool)


def spawn_zombie(wave):
    side = random.choice(["top", "bottom", "left", "right"])
    if side == "top":
        x, y = random.randint(40, WIDTH - 40), -30
    elif side == "bottom":
        x, y = random.randint(40, WIDTH - 40), HEIGHT + 30
    elif side == "left":
        x, y = -30, random.randint(40, HEIGHT - 40)
    else:
        x, y = WIDTH + 30, random.randint(40, HEIGHT - 40)

    ztype = pick_zombie_type(wave)
    stats = ZOMBIE_TYPES[ztype]
    wave_bonus = wave * 0.08
    hp = stats["hp"] + (wave // 4 if ztype != "lambda" else 0)

    return {
        "type": ztype,
        "x": float(x),
        "y": float(y),
        "r": stats["r"],
        "speed": stats["speed"] + wave_bonus,
        "hp": hp,
        "max_hp": hp,
        "score": stats["score"],
        "color": stats["color"],
        "border": stats["border"],
        "name": stats["name"],
        "wobble": random.uniform(0, math.pi * 2),
    }


def dist(ax, ay, bx, by):
    return math.hypot(ax - bx, ay - by)


def reset_game():
    return {
        "nahla_x": WIDTH / 2,
        "nahla_y": HEIGHT / 2,
        "bullets": [],
        "zombies": [],
        "score": 0,
        "wave": 1,
        "kills_this_wave": 0,
        "kills_needed": 10,
        "lives": LIVES_START,
        "spawn_timer": 0,
        "hit_timer": 0,
        "shoot_cooldown": 0,
        "state": PLAYING,
    }


def aim_vector(game, target_x, target_y):
    """Direction normalisée de Nahla vers la cible (souris)."""
    dx = target_x - game["nahla_x"]
    dy = target_y - game["nahla_y"]
    length = math.hypot(dx, dy)
    if length < 8:
        return 0.0, -1.0
    return dx / length, dy / length


def shoot_toward(game, target_x, target_y):
    if game["shoot_cooldown"] > 0:
        return False
    ux, uy = aim_vector(game, target_x, target_y)
    spawn_dist = NAHLA_R + 10
    game["bullets"].append({
        "x": game["nahla_x"] + ux * spawn_dist,
        "y": game["nahla_y"] + uy * spawn_dist,
        "vx": ux * BULLET_SPEED,
        "vy": uy * BULLET_SPEED,
    })
    game["shoot_cooldown"] = SHOOT_COOLDOWN_MS
    return True


def draw_crosshair(screen, mx, my):
    size = 14
    color = ACCENT
    pygame.draw.line(screen, color, (mx - size, my), (mx + size, my), 2)
    pygame.draw.line(screen, color, (mx, my - size), (mx, my + size), 2)
    pygame.draw.circle(screen, color, (mx, my), 6, 2)


def draw_aim_line(screen, game, mx, my):
    ux, uy = aim_vector(game, mx, my)
    start_x = game["nahla_x"] + ux * (NAHLA_R + 6)
    start_y = game["nahla_y"] + uy * (NAHLA_R + 6)
    end_x = start_x + ux * AIM_LINE_LEN
    end_y = start_y + uy * AIM_LINE_LEN
    pygame.draw.line(screen, (180, 120, 50), (start_x, start_y), (end_x, end_y), 2)
    pygame.draw.circle(screen, CROQUETTE, (int(end_x), int(end_y)), 5)


def update(game, keys, dt):
    if game["state"] != PLAYING:
        return

    speed = NAHLA_SPEED
    if pressed(keys, MOVE_LEFT):
        game["nahla_x"] -= speed
    if pressed(keys, MOVE_RIGHT):
        game["nahla_x"] += speed
    if pressed(keys, MOVE_UP):
        game["nahla_y"] -= speed
    if pressed(keys, MOVE_DOWN):
        game["nahla_y"] += speed

    game["nahla_x"] = max(NAHLA_R, min(WIDTH - NAHLA_R, game["nahla_x"]))
    game["nahla_y"] = max(NAHLA_R, min(HEIGHT - NAHLA_R, game["nahla_y"]))

    if game["shoot_cooldown"] > 0:
        game["shoot_cooldown"] -= dt
    if game["hit_timer"] > 0:
        game["hit_timer"] -= dt

    game["spawn_timer"] += dt
    spawn_interval = max(350, SPAWN_MS - game["wave"] * 70)
    if game["spawn_timer"] >= spawn_interval and len(game["zombies"]) < MAX_ZOMBIES:
        game["spawn_timer"] = 0
        game["zombies"].append(spawn_zombie(game["wave"]))
        # À partir de la vague 3, parfois 2 zombies d'un coup
        if game["wave"] >= SPAWN_BURST_WAVE and len(game["zombies"]) < MAX_ZOMBIES:
            if random.random() < 0.35 + game["wave"] * 0.03:
                game["zombies"].append(spawn_zombie(game["wave"]))

    for z in game["zombies"]:
        dx = game["nahla_x"] - z["x"]
        dy = game["nahla_y"] - z["y"]
        d = math.hypot(dx, dy) or 1
        move_speed = z["speed"]
        # Les Fous zigzaguent un peu
        if z["type"] == "fou":
            z["wobble"] += 0.12
            move_speed *= 1 + 0.25 * math.sin(z["wobble"])
        z["x"] += dx / d * move_speed
        z["y"] += dy / d * move_speed

    for b in game["bullets"]:
        b["x"] += b["vx"]
        b["y"] += b["vy"]
    game["bullets"] = [
        b for b in game["bullets"]
        if -20 < b["x"] < WIDTH + 20 and -20 < b["y"] < HEIGHT + 20
    ]

    for z in game["zombies"][:]:
        for b in game["bullets"][:]:
            if dist(z["x"], z["y"], b["x"], b["y"]) < z["r"] + BULLET_R:
                z["hp"] -= 1
                game["bullets"].remove(b)
                if z["hp"] <= 0:
                    game["zombies"].remove(z)
                    game["score"] += z["score"]
                    game["kills_this_wave"] += 1
                break

    if game["hit_timer"] <= 0:
        for z in game["zombies"]:
            if dist(z["x"], z["y"], game["nahla_x"], game["nahla_y"]) < z["r"] + NAHLA_R - 10:
                damage = 2 if z["type"] in ("tank", "geant") else 1
                game["lives"] -= damage
                game["hit_timer"] = HIT_COOLDOWN_MS
                if game["lives"] <= 0:
                    game["state"] = OVER
                break

    if game["kills_this_wave"] >= game["kills_needed"]:
        game["wave"] += 1
        game["kills_this_wave"] = 0
        game["kills_needed"] = 10 + game["wave"] * 3
        game["zombies"].clear()


def draw_floor(screen):
    screen.fill(BG)
    for y in range(0, HEIGHT, 64):
        for x in range(0, WIDTH, 64):
            c = FLOOR if (x // 64 + y // 64) % 2 == 0 else (28, 36, 24)
            pygame.draw.rect(screen, c, (x, y, 64, 64))


def draw_hud(screen, font, game):
    lines = [
        f"Score : {game['score']}",
        f"Vague : {game['wave']}",
        f"Vies : {'♥' * game['lives']}",
        f"Zombies : {len(game['zombies'])}",
    ]
    for i, line in enumerate(lines):
        surf = font.render(line, True, TEXT)
        screen.blit(surf, (16, 12 + i * 28))


def draw_zombie(screen, z, font_small):
    x, y = int(z["x"]), int(z["y"])
    r = z["r"]
    pygame.draw.circle(screen, z["color"], (x, y), r)
    pygame.draw.circle(screen, z["border"], (x, y), r, 3)

    eye_off = max(4, r // 3)
    eye_r = max(3, r // 6)
    pygame.draw.circle(screen, DANGER, (x - eye_off, y - eye_r), eye_r)
    pygame.draw.circle(screen, DANGER, (x + eye_off, y - eye_r), eye_r)

    # Sprinter = yeux plus grands
    if z["type"] == "sprinter":
        pygame.draw.circle(screen, (255, 255, 100), (x - eye_off, y - eye_r), eye_r + 1)
        pygame.draw.circle(screen, (255, 255, 100), (x + eye_off, y - eye_r), eye_r + 1)

    # Barre de vie si plus d'1 pv
    if z["max_hp"] > 1:
        bar_w = r * 2
        ratio = z["hp"] / z["max_hp"]
        bx = x - r
        by = y - r - 10
        pygame.draw.rect(screen, (40, 40, 40), (bx, by, bar_w, 6), border_radius=2)
        pygame.draw.rect(screen, DANGER, (bx, by, int(bar_w * ratio), 6), border_radius=2)

    # Nom au-dessus des gros types
    if z["type"] in ("tank", "geant", "fou"):
        label = font_small.render(z["name"], True, TEXT)
        screen.blit(label, label.get_rect(center=(x, y - r - 18)))


def draw_game(screen, nahla_img, font, big_font, game):
    draw_floor(screen)
    font_small = pygame.font.SysFont("arial", 14, bold=True)

    for z in game["zombies"]:
        draw_zombie(screen, z, font_small)

    for b in game["bullets"]:
        pygame.draw.circle(screen, CROQUETTE, (int(b["x"]), int(b["y"])), BULLET_R)

    nx, ny = int(game["nahla_x"]), int(game["nahla_y"])
    mx, my = pygame.mouse.get_pos()
    draw_aim_line(screen, game, mx, my)

    rect = nahla_img.get_rect(center=(nx, ny))
    if game["hit_timer"] > 0 and (game["hit_timer"] // 100) % 2 == 0:
        tint = nahla_img.copy()
        tint.fill((255, 80, 80, 120), special_flags=pygame.BLEND_RGBA_MULT)
        screen.blit(tint, rect)
    else:
        screen.blit(nahla_img, rect)

    draw_hud(screen, font, game)

    progress = game["kills_this_wave"] / game["kills_needed"]
    bar_w = 200
    pygame.draw.rect(screen, (40, 40, 40), (WIDTH - bar_w - 20, 16, bar_w, 14), border_radius=4)
    pygame.draw.rect(
        screen, ACCENT,
        (WIDTH - bar_w - 20, 16, int(bar_w * progress), 14),
        border_radius=4,
    )
    lbl = font.render("Vague suivante", True, MUTED)
    screen.blit(lbl, (WIDTH - bar_w - 20, 34))

    draw_crosshair(screen, mx, my)


def draw_menu(screen, big_font, font):
    draw_floor(screen)
    title = big_font.render("Nahla vs Zombies", True, ACCENT)
    sub = font.render("Les zombies veulent tes croquettes. Tue-les.", True, TEXT)
    hint = font.render("ESPACE ou clic — jouer", True, MUTED)
    ctrl = font.render("ZQSD — bouger · Souris — viser · Clic / Espace — tirer", True, MUTED)
    types = font.render("Zombies : Lambda · Sprinter · Tank · Fou · Géant", True, MUTED)
    screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60)))
    screen.blit(sub, sub.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
    screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50)))
    screen.blit(ctrl, ctrl.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 85)))
    screen.blit(types, types.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 115)))


def draw_over(screen, big_font, font, game):
    draw_game(screen, nahla_img_cache, font, big_font, game)
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    screen.blit(overlay, (0, 0))
    title = big_font.render("Nahla a été débordée", True, DANGER)
    score = font.render(f"Score final : {game['score']} — Vague {game['wave']}", True, TEXT)
    hint = font.render("R — rejouer · ESC — menu", True, MUTED)
    screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30)))
    screen.blit(score, score.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20)))
    screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60)))


nahla_img_cache = None


def main():
    global nahla_img_cache
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("arial", 22)
    big_font = pygame.font.SysFont("arial", 48, bold=True)
    nahla_img_cache = load_nahla()

    game = {"state": MENU}
    pygame.mouse.set_visible(True)

    running = True
    while running:
        dt = clock.tick(FPS)
        keys = pygame.key.get_pressed()
        mouse_buttons = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game["state"] = MENU
                    pygame.mouse.set_visible(True)
                elif event.key == pygame.K_SPACE:
                    if game["state"] == MENU:
                        game = reset_game()
                        pygame.mouse.set_visible(False)
                    elif game["state"] == PLAYING:
                        mx, my = pygame.mouse.get_pos()
                        shoot_toward(game, mx, my)
                    elif game["state"] == OVER:
                        game = reset_game()
                        pygame.mouse.set_visible(False)
                elif event.key == pygame.K_r and game.get("state") == OVER:
                    game = reset_game()
                    pygame.mouse.set_visible(False)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if game["state"] == MENU:
                    game = reset_game()
                    pygame.mouse.set_visible(False)

        if game["state"] == PLAYING:
            mx, my = pygame.mouse.get_pos()
            fire = keys[pygame.K_SPACE] or mouse_buttons[0]
            if fire:
                shoot_toward(game, mx, my)
            update(game, keys, dt)

        if game["state"] == MENU:
            draw_menu(screen, big_font, font)
        elif game["state"] == PLAYING:
            draw_game(screen, nahla_img_cache, font, big_font, game)
        elif game["state"] == OVER:
            draw_over(screen, big_font, font, game)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
