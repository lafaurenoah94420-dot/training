"""Nahla Clicker — clique pour nourrir Nahla."""

import random
import sys
from pathlib import Path

import pygame

# --- Fenêtre ---
WIDTH, HEIGHT = 960, 640
FPS = 60
TITLE = "Nahla Clicker"

ASSETS = Path(__file__).parent
NAHLA_HEAD = ASSETS / "nahla_head.png"
NAHLA_PHOTO = ASSETS / "WhatsApp Image 2026-04-24 at 00.18.56.jpeg"
NAHLA_CROP = (0.18, 0.08, 0.64, 0.72)

# --- Couleurs ---
COUCH = (196, 168, 132)
COUCH_DARK = (168, 142, 108)
PANEL = (148, 124, 96)
PANEL_LIGHT = (176, 150, 118)
SELECTED = (255, 220, 120)
TORTIE_DARK = (58, 42, 36)
TEXT = (55, 40, 28)
MUTED = (110, 90, 70)
ACCENT = (255, 210, 80)
CROQUETTE = (180, 120, 40)
HUNGER_OK = (90, 180, 90)
HUNGER_WARN = (230, 180, 50)
HUNGER_LOW = (220, 80, 70)
RESET_BG = (120, 90, 70)
RESET_HOVER = (150, 115, 88)

NAHLA_BASE_SIZE = 70
GROW_EVERY = 10
GROW_AMOUNT = 8
PHRASE_EVERY = 15

HUNGER_MAX = 100
HUNGER_DRAIN = 5.5
HUNGER_LOW_THRESHOLD = 30
HUNGER_COMPLAIN_MS = 2200
BOUNCE_MS = 180

RESET_RECT = pygame.Rect(WIDTH - 132, 20, 100, 38)

LEVELS = [
    (0, "Chat normal"),
    (10, "Chat dodu"),
    (30, "Boule"),
    (60, "Rouleau de Nahla"),
    (100, "Menace planétaire"),
]

FOODS = [
    {"name": "Croquette", "points": 1, "growth": 1, "hunger": 14, "color": (180, 120, 40), "key": pygame.K_1},
    {"name": "Pâtée", "points": 3, "growth": 3, "hunger": 28, "color": (195, 130, 90), "key": pygame.K_2},
    {"name": "Thon", "points": 5, "growth": 6, "hunger": 45, "color": (120, 160, 190), "key": pygame.K_3},
    {"name": "Festin", "points": 10, "growth": 12, "hunger": 100, "color": (220, 180, 70), "key": pygame.K_4},
]

PHRASES = [
    "Nahla te ignore.",
    "Nahla juge ton existence.",
    "Nahla exige plus de croquettes.",
    "Nahla te considère comme un serveur.",
    "Nahla pense que tu peux faire mieux.",
    "Nahla soupire de mépris.",
    "Nahla voulait du thon, pas ça.",
    "Nahla te regarde comme un meuble.",
    "Nahla approche du statut boule.",
    "Nahla devient une menace géométrique.",
]

HUNGER_PHRASES = [
    "Nahla a FAIM.",
    "Nahla miaule de colère.",
    "Nahla te fixe avec haine — elle veut manger.",
    "Nahla commence à gratter le canapé.",
    "Nahla menace de te réveiller à 4h du mat.",
    "Nahla pense que tu l'as oubliée.",
    "Le ventre de Nahla fait un bruit de tonnerre.",
]


def nahla_size(growth_points: int) -> int:
    return NAHLA_BASE_SIZE + (growth_points // GROW_EVERY) * GROW_AMOUNT


def nahla_level(growth_points: int) -> str:
    title = LEVELS[0][1]
    for threshold, name in LEVELS:
        if growth_points >= threshold:
            title = name
    return title


def hunger_color(ratio: float) -> tuple[int, int, int]:
    if ratio <= 0.3:
        return HUNGER_LOW
    if ratio <= 0.6:
        return HUNGER_WARN
    return HUNGER_OK


def load_nahla_image() -> pygame.Surface:
    if NAHLA_PHOTO.exists():
        full = pygame.image.load(str(NAHLA_PHOTO)).convert()
        w, h = full.get_size()
        cx, cy, cw, ch = NAHLA_CROP
        rect = pygame.Rect(int(w * cx), int(h * cy), int(w * cw), int(h * ch))
        return full.subsurface(rect).copy()
    if NAHLA_HEAD.exists():
        return pygame.image.load(str(NAHLA_HEAD)).convert_alpha()
    surf = pygame.Surface((140, 140), pygame.SRCALPHA)
    pygame.draw.ellipse(surf, ACCENT, surf.get_rect())
    return surf


def nahla_sprite(base: pygame.Surface, size: int, anim_scale: float = 1.0) -> pygame.Surface:
    w, h = base.get_size()
    max_side = size * 2 * anim_scale
    scale = min(max_side / w, max_side / h)
    new_w = max(1, int(w * scale))
    new_h = max(1, int(h * scale))
    return pygame.transform.smoothscale(base, (new_w, new_h))


def nahla_rect_at(center_x: int, center_y: int, sprite: pygame.Surface) -> pygame.Rect:
    return sprite.get_rect(center=(center_x, center_y))


def food_button_rects() -> list[pygame.Rect]:
    gap = 12
    btn_w = (WIDTH - 80 - gap * (len(FOODS) - 1)) // len(FOODS)
    btn_h = 72
    y = HEIGHT - 108
    rects = []
    x = 40
    for _ in FOODS:
        rects.append(pygame.Rect(x, y, btn_w, btn_h))
        x += btn_w + gap
    return rects


def draw_hunger_bar(
    surface: pygame.Surface,
    hunger: float,
    font_small: pygame.font.Font,
) -> None:
    bar_x, bar_y, bar_w, bar_h = 32, 132, 220, 18
    ratio = max(0.0, min(1.0, hunger / HUNGER_MAX))
    label = font_small.render("Faim", True, TEXT)
    surface.blit(label, (bar_x, bar_y - 22))
    pygame.draw.rect(surface, COUCH_DARK, (bar_x, bar_y, bar_w, bar_h), border_radius=9)
    fill_w = max(0, int(bar_w * ratio))
    if fill_w > 0:
        pygame.draw.rect(surface, hunger_color(ratio), (bar_x, bar_y, fill_w, bar_h), border_radius=9)
    pygame.draw.rect(surface, TORTIE_DARK, (bar_x, bar_y, bar_w, bar_h), 2, border_radius=9)


def draw_reset_button(surface: pygame.Surface, font_small: pygame.font.Font, hovered: bool) -> None:
    bg = RESET_HOVER if hovered else RESET_BG
    pygame.draw.rect(surface, bg, RESET_RECT, border_radius=10)
    pygame.draw.rect(surface, TORTIE_DARK, RESET_RECT, 2, border_radius=10)
    text = font_small.render("Reset", True, TEXT)
    text_rect = text.get_rect(center=RESET_RECT.center)
    surface.blit(text, text_rect)


def draw_food_icon(surface: pygame.Surface, rect: pygame.Rect, color: tuple[int, int, int]) -> None:
    cx, cy = rect.center
    pygame.draw.circle(surface, color, (cx, cy - 4), 14)
    pygame.draw.circle(surface, (90, 60, 20), (cx, cy - 4), 14, 2)


def draw_food_buttons(
    surface: pygame.Surface,
    rects: list[pygame.Rect],
    selected: int,
    font: pygame.font.Font,
    font_small: pygame.font.Font,
) -> None:
    pygame.draw.rect(surface, PANEL, (32, HEIGHT - 120, WIDTH - 64, 96), border_radius=16)
    for i, (food, rect) in enumerate(zip(FOODS, rects)):
        bg = SELECTED if i == selected else PANEL_LIGHT
        pygame.draw.rect(surface, bg, rect, border_radius=12)
        pygame.draw.rect(surface, TORTIE_DARK, rect, 2, border_radius=12)
        draw_food_icon(surface, rect, food["color"])
        name = font_small.render(food["name"], True, TEXT)
        name_rect = name.get_rect(centerx=rect.centerx, top=rect.top + 8)
        surface.blit(name, name_rect)
        info = font_small.render(f'+{food["points"]} | x{food["growth"]}', True, MUTED)
        info_rect = info.get_rect(centerx=rect.centerx, bottom=rect.bottom - 8)
        surface.blit(info, info_rect)
        key = font.render(str(i + 1), True, TEXT)
        surface.blit(key, (rect.right - 22, rect.top + 6))


def feed_nahla(food: dict, mx: int, my: int, popups: list[dict]) -> tuple[int, int, float]:
    popups.append(
        {
            "x": mx,
            "y": my,
            "life": 700,
            "text": f'+{food["points"]}',
            "color": food["color"],
        }
    )
    return food["points"], food["growth"], food["hunger"]


def reset_game() -> dict:
    return {
        "score": 0,
        "growth_points": 0,
        "hunger": float(HUNGER_MAX),
        "selected_food": 0,
        "phrase": "Choisis une nourriture, puis clique sur Nahla.",
        "popups": [],
        "feed_anim": 0.0,
        "hunger_timer": 0,
    }


def main() -> None:
    pygame.init()
    pygame.display.set_caption(TITLE)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font_big = pygame.font.SysFont("Arial", 42, bold=True)
    font = pygame.font.SysFont("Arial", 28)
    font_small = pygame.font.SysFont("Arial", 22)

    state = reset_game()
    center_x, center_y = WIDTH // 2, HEIGHT // 2 - 10
    food_rects = food_button_rects()
    nahla_base = load_nahla_image()

    running = True
    while running:
        dt = clock.tick(FPS)
        mx, my = pygame.mouse.get_pos()
        reset_hovered = RESET_RECT.collidepoint(mx, my)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    state = reset_game()
                else:
                    for i, food in enumerate(FOODS):
                        if event.key == food["key"]:
                            state["selected_food"] = i
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if RESET_RECT.collidepoint(event.pos):
                    state = reset_game()
                    continue

                clicked_food = next(
                    (i for i, rect in enumerate(food_rects) if rect.collidepoint(event.pos)),
                    None,
                )
                if clicked_food is not None:
                    state["selected_food"] = clicked_food
                else:
                    size = nahla_size(state["growth_points"])
                    anim_scale = 1.0 + 0.2 * state["feed_anim"]
                    nahla_img = nahla_sprite(nahla_base, size, anim_scale)
                    y_offset = int(-14 * state["feed_anim"])
                    nahla_hitbox = nahla_rect_at(center_x, center_y + y_offset, nahla_img)
                    if nahla_hitbox.collidepoint(event.pos):
                        food = FOODS[state["selected_food"]]
                        pts, grow, restore = feed_nahla(food, event.pos[0], event.pos[1], state["popups"])
                        state["score"] += pts
                        state["growth_points"] += grow
                        state["hunger"] = min(HUNGER_MAX, state["hunger"] + restore)
                        state["feed_anim"] = 1.0
                        if state["score"] % PHRASE_EVERY == 0:
                            state["phrase"] = random.choice(PHRASES)

        state["hunger"] = max(0.0, state["hunger"] - HUNGER_DRAIN * dt / 1000)
        state["feed_anim"] = max(0.0, state["feed_anim"] - dt / BOUNCE_MS)

        if state["hunger"] < HUNGER_LOW_THRESHOLD:
            state["hunger_timer"] += dt
            if state["hunger_timer"] >= HUNGER_COMPLAIN_MS:
                state["phrase"] = random.choice(HUNGER_PHRASES)
                state["hunger_timer"] = 0
        else:
            state["hunger_timer"] = 0

        size = nahla_size(state["growth_points"])
        anim_scale = 1.0 + 0.2 * state["feed_anim"]
        y_offset = int(-14 * state["feed_anim"])
        nahla_img = nahla_sprite(nahla_base, size, anim_scale)
        nahla_hitbox = nahla_rect_at(center_x, center_y + y_offset, nahla_img)

        for popup in state["popups"]:
            popup["life"] -= dt
            popup["y"] -= dt * 0.05
        state["popups"] = [p for p in state["popups"] if p["life"] > 0]

        screen.fill(COUCH)
        screen.blit(nahla_img, nahla_hitbox)

        title = font_big.render(f"Croquettes : {state['score']}", True, TEXT)
        screen.blit(title, (32, 24))

        level_name = nahla_level(state["growth_points"])
        level_text = font.render(f"Niveau : {level_name}", True, ACCENT)
        screen.blit(level_text, (32, 72))

        growth_text = font_small.render(f"Croissance : {state['growth_points']}", True, MUTED)
        screen.blit(growth_text, (32, 104))

        draw_hunger_bar(screen, state["hunger"], font_small)
        draw_reset_button(screen, font_small, reset_hovered)

        selected = FOODS[state["selected_food"]]
        hint = font_small.render(
            f"1-4 nourriture | Clic Nahla = {selected['name']} | R = reset | Echap = quitter",
            True,
            MUTED,
        )
        screen.blit(hint, (280, 132))

        phrase_surf = font.render(state["phrase"], True, TEXT)
        phrase_rect = phrase_surf.get_rect(center=(WIDTH // 2, HEIGHT - 138))
        screen.blit(phrase_surf, phrase_rect)

        draw_food_buttons(screen, food_rects, state["selected_food"], font, font_small)

        for popup in state["popups"]:
            alpha = min(255, int(255 * popup["life"] / 700))
            color = popup.get("color", CROQUETTE)
            temp = pygame.Surface((24, 24), pygame.SRCALPHA)
            pygame.draw.circle(temp, (*color, alpha), (12, 12), 10)
            surface_pos = (int(popup["x"]) - 12, int(popup["y"]) - 12)
            screen.blit(temp, surface_pos)
            plus = font_small.render(popup["text"], True, ACCENT)
            plus.set_alpha(alpha)
            screen.blit(plus, (popup["x"] + 14, popup["y"] - 10))

        if nahla_hitbox.collidepoint(mx, my):
            pygame.draw.rect(screen, ACCENT, nahla_hitbox.inflate(24, 24), 3, border_radius=12)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
