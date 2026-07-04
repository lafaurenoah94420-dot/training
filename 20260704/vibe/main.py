"""Nahla Dodge — esquive ce qui tombe du ciel."""

import random
import sys
from pathlib import Path

import pygame

from sprites import OBJECT_SIZE, load_object_sprites

# --- Fenêtre ---
WIDTH, HEIGHT = 800, 600
FPS = 60
TITLE = "Nahla Dodge"

ASSETS = Path(__file__).parent
NAHLA_HEAD = ASSETS / "nahla_head.png"

# --- Couleurs ---
BG = (18, 18, 28)
BG_PANEL = (28, 28, 42)
TEXT = (240, 235, 220)
MUTED = (140, 135, 125)
ACCENT = (255, 200, 80)
DANGER = (220, 70, 70)
SELECTED = (255, 220, 120)

OBJECT_LABELS = [
    "brosse",
    "reveil",
    "seringue",
    "croquettes",
    "laser",
    "aspirateur",
    "shampoing",
    "cage",
    "collier",
]

NAHLA_SIZE = 64
SPAWN_MARGIN = 40
NAHLA_HITBOX_INSET = (20, 16)  # réduit la zone de collision de Nahla
OBJECT_HITBOX_INSET = 12       # réduit la zone de collision des objets
COLLISION_SUBSTEP = 8          # px max par pas de collision (évite le "tunnel")

LEVELS = [
    {
        "id": "chill",
        "name": "Chill",
        "tagline": "Nahla dort, rien ne presse",
        "base_speed": 2.0,
        "max_speed": 6.0,
        "accel_step": 180,
        "object_count": 5,
        "nahla_speed": 7,
        "color": (100, 190, 130),
    },
    {
        "id": "normal",
        "name": "Normal",
        "tagline": "Une journée classique",
        "base_speed": 3.0,
        "max_speed": 10.0,
        "accel_step": 100,
        "object_count": 8,
        "nahla_speed": 6,
        "color": (120, 170, 230),
    },
    {
        "id": "stress",
        "name": "Stress",
        "tagline": "Réveil à 6h + brosse + aspirateur",
        "base_speed": 4.5,
        "max_speed": 13.0,
        "accel_step": 70,
        "object_count": 10,
        "nahla_speed": 5,
        "color": (240, 170, 70),
    },
    {
        "id": "enfer",
        "name": "Enfer",
        "tagline": "Jour chez le véto, tout tombe",
        "base_speed": 6.0,
        "max_speed": 16.0,
        "accel_step": 45,
        "object_count": 12,
        "nahla_speed": 5,
        "color": (230, 80, 80),
    },
]


def load_nahla_sprite():
    if NAHLA_HEAD.exists():
        image = pygame.image.load(NAHLA_HEAD).convert_alpha()
        return pygame.transform.smoothscale(image, (NAHLA_SIZE, NAHLA_SIZE))
    surface = pygame.Surface((NAHLA_SIZE, NAHLA_SIZE), pygame.SRCALPHA)
    pygame.draw.ellipse(surface, (200, 160, 120), surface.get_rect())
    return surface


def fall_speed_for_score(score, level):
    return min(level["max_speed"], level["base_speed"] + score // level["accel_step"])


def inset_rect(rect, x_inset, y_inset):
    """Hitbox plus petite que le sprite visible."""
    return rect.inflate(-x_inset * 2, -y_inset * 2)


def nahla_hitbox(nahla_rect):
    x_inset, y_inset = NAHLA_HITBOX_INSET
    return inset_rect(nahla_rect, x_inset, y_inset)


def object_hitbox(obj_rect):
    return inset_rect(obj_rect, OBJECT_HITBOX_INSET, OBJECT_HITBOX_INSET)


def object_hits_nahla(nahla_rect, obj):
    """Déplace l'objet par petits pas pour éviter de traverser Nahla sans détecter."""
    nahla_hb = nahla_hitbox(nahla_rect)
    remaining = obj["speed"]
    while remaining > 0:
        step = min(remaining, COLLISION_SUBSTEP)
        obj["rect"].y += step
        remaining -= step
        if nahla_hb.colliderect(object_hitbox(obj["rect"])):
            return True
    return False


def reset_game(level):
    nahla_x = WIDTH // 2 - NAHLA_SIZE // 2
    nahla_y = HEIGHT - NAHLA_SIZE - 30
    nahla_rect = pygame.Rect(nahla_x, nahla_y, NAHLA_SIZE, NAHLA_SIZE)

    objects = []
    for _ in range(level["object_count"]):
        objects.append(spawn_object(objects, level))

    return {
        "level": level,
        "nahla_rect": nahla_rect,
        "objects": objects,
        "score": 0,
        "game_over": False,
        "elapsed_ms": 0,
    }


def spawn_object(existing, level):
    used_x = [obj["rect"].centerx for obj in existing]
    for _ in range(20):
        x = random.randint(SPAWN_MARGIN, WIDTH - SPAWN_MARGIN - OBJECT_SIZE)
        if all(abs(x - other) > OBJECT_SIZE for other in used_x):
            break
    label = random.choice(OBJECT_LABELS)
    rect = pygame.Rect(x, random.randint(-HEIGHT, -OBJECT_SIZE), OBJECT_SIZE, OBJECT_SIZE)
    base = level["base_speed"]
    return {
        "rect": rect,
        "label": label,
        "speed": random.uniform(base, base + 1.5),
    }


def draw_object(screen, sprites, obj):
    screen.blit(sprites[obj["label"]], obj["rect"])


def draw_hud(screen, font, score, fall_speed, level_name):
    score_surf = font.render(f"Score : {score}", True, TEXT)
    speed_surf = font.render(f"Vitesse : {fall_speed:.1f}", True, MUTED)
    level_surf = font.render(f"Niveau : {level_name}", True, ACCENT)
    screen.blit(score_surf, (20, 16))
    screen.blit(speed_surf, (20, 44))
    screen.blit(level_surf, (WIDTH - level_surf.get_width() - 20, 16))


def draw_game_over(screen, big_font, small_font, score, level_name):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    screen.blit(overlay, (0, 0))

    title = big_font.render("GAME OVER", True, DANGER)
    detail = small_font.render(f"Score final : {score} ({level_name})", True, TEXT)
    replay = small_font.render("R — Rejouer ce niveau", True, ACCENT)
    menu = small_font.render("M — Retour au menu", True, TEXT)

    screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 56)))
    screen.blit(detail, detail.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 8)))
    screen.blit(replay, replay.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 32)))
    screen.blit(menu, menu.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 62)))


def level_button_rect(index):
    return pygame.Rect(WIDTH // 2 - 220, 170 + index * 92, 440, 72)


def draw_menu(screen, fonts, nahla_sprite, menu_index):
    title_font, item_font, hint_font = fonts

    screen.fill(BG)

    title = title_font.render("Nahla Dodge", True, ACCENT)
    subtitle = hint_font.render("Choisis ton niveau de souffrance", True, MUTED)
    screen.blit(title, title.get_rect(center=(WIDTH // 2, 70)))
    screen.blit(subtitle, subtitle.get_rect(center=(WIDTH // 2, 118)))

    nahla_rect = nahla_sprite.get_rect(center=(WIDTH // 2, 145))
    screen.blit(nahla_sprite, (WIDTH - 110, 40))

    for index, level in enumerate(LEVELS):
        rect = level_button_rect(index)
        selected = index == menu_index
        fill = level["color"] if selected else BG_PANEL
        border = SELECTED if selected else (60, 60, 80)

        pygame.draw.rect(screen, fill, rect, border_radius=12)
        pygame.draw.rect(screen, border, rect, 3 if selected else 2, border_radius=12)

        name_color = (20, 20, 28) if selected else TEXT
        name = item_font.render(level["name"], True, name_color)
        tag = hint_font.render(level["tagline"], True, name_color if selected else MUTED)
        stats = hint_font.render(
            f"{level['object_count']} objets · vitesse max {level['max_speed']:.0f}",
            True,
            name_color if selected else MUTED,
        )

        screen.blit(name, (rect.x + 18, rect.y + 10))
        screen.blit(tag, (rect.x + 18, rect.y + 34))
        screen.blit(stats, (rect.x + 18, rect.y + 52))

    hint = hint_font.render("↑ ↓ ou Z/S choisir   Entrée jouer   Échap quitter", True, MUTED)
    screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT - 28)))


def handle_menu_click(pos):
    for index, _ in enumerate(LEVELS):
        if level_button_rect(index).collidepoint(pos):
            return index
    return None


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()
    title_font = pygame.font.SysFont(None, 72)
    item_font = pygame.font.SysFont(None, 36)
    hint_font = pygame.font.SysFont(None, 24)
    big_font = pygame.font.SysFont(None, 64)
    nahla_sprite = load_nahla_sprite()
    object_sprites = load_object_sprites()

    mode = "menu"
    menu_index = 1
    state = None

    running = True
    while running:
        dt = clock.tick(FPS)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if mode == "menu":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key in (pygame.K_UP, pygame.K_w, pygame.K_z):
                        menu_index = (menu_index - 1) % len(LEVELS)
                    if event.key in (pygame.K_DOWN, pygame.K_s):
                        menu_index = (menu_index + 1) % len(LEVELS)
                    if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                        state = reset_game(LEVELS[menu_index])
                        mode = "playing"
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    clicked = handle_menu_click(event.pos)
                    if clicked is not None:
                        menu_index = clicked
                        state = reset_game(LEVELS[menu_index])
                        mode = "playing"

            elif mode == "playing":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        mode = "menu"
                        state = None
                    if event.key == pygame.K_r and state["game_over"]:
                        state = reset_game(state["level"])
                    if event.key == pygame.K_m and state["game_over"]:
                        mode = "menu"
                        state = None

        if mode == "menu":
            draw_menu(screen, (title_font, item_font, hint_font), nahla_sprite, menu_index)

        elif mode == "playing" and state is not None:
            level = state["level"]

            if not state["game_over"]:
                move = 0
                # Flèches + WASD (QWERTY) + ZQSD (AZERTY)
                if keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_q]:
                    move -= level["nahla_speed"]
                if keys[pygame.K_RIGHT] or keys[pygame.K_d] or keys[pygame.K_s]:
                    move += level["nahla_speed"]

                state["nahla_rect"].x += move
                state["nahla_rect"].x = max(0, min(WIDTH - NAHLA_SIZE, state["nahla_rect"].x))

                state["elapsed_ms"] += dt
                state["score"] = state["elapsed_ms"] // 100
                fall_speed = fall_speed_for_score(state["score"], level)

                for obj in state["objects"]:
                    obj["speed"] = max(obj["speed"], fall_speed)

                    if object_hits_nahla(state["nahla_rect"], obj):
                        state["game_over"] = True
                        break

                    if obj["rect"].top > HEIGHT:
                        others = [other for other in state["objects"] if other is not obj]
                        new_obj = spawn_object(others, level)
                        obj["rect"] = new_obj["rect"]
                        obj["label"] = new_obj["label"]
                        obj["speed"] = random.uniform(fall_speed, fall_speed + 1.5)

            screen.fill(BG)
            for obj in state["objects"]:
                draw_object(screen, object_sprites, obj)

            screen.blit(nahla_sprite, state["nahla_rect"])
            draw_hud(
                screen,
                hint_font,
                state["score"],
                fall_speed_for_score(state["score"], level),
                level["name"],
            )

            if state["game_over"]:
                draw_game_over(screen, big_font, hint_font, state["score"], level["name"])

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
