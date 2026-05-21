import math
import pygame
import random
import sys
from pathlib import Path

WIDTH = 800
HEIGHT = 600
TITLE = "Nahla vs le laser"
BG_COLOR = (0, 0, 0)

MENU = "menu"
PLAYING = "playing"

BUTTON_WIDTH = 220
BUTTON_HEIGHT = 56
BUTTON_COLOR = (40, 35, 50)
BUTTON_BORDER = (255, 120, 40)
BUTTON_HOVER = (60, 50, 70)
TEXT_COLOR = (255, 255, 255)
ACCENT = (255, 140, 50)

PLAYER_SIZE = 82
MENU_PREVIEW_SIZE = 108
SPRITE_SOURCE_SIZE = 110
PLAYER_SPEED = 7
PLAYER_MARGIN_TOP = 60
PLAYER_MARGIN_BOTTOM = 40
PLAYER_MARGIN_SIDE = 20
PLAYER_HIT_INSET = 10

MAX_HP = 100
HP_BAR_WIDTH = 200
HP_BAR_HEIGHT = 22
HP_BAR_MARGIN = 16
HP_COLOR_HIGH = (60, 200, 90)
HP_COLOR_MID = (230, 170, 40)
HP_COLOR_LOW = (220, 55, 55)
HP_BG = (50, 30, 35)
HP_BORDER = (255, 120, 40)

LASER_WIDTH = 16
LASER_HEIGHT = 72
LASER_DAMAGE = 18
LASER_OFFSCREEN_MARGIN = 40

DIFF_BTN_WIDTH = 170
DIFF_BTN_HEIGHT = 44
BUTTON_SELECTED = (35, 45, 75)

DIFFICULTIES = {
    "normal": {
        "label": "Normal",
        "spawn_ms": 520,
        "speed": 7,
        "max_lasers": 22,
        "color": (255, 40, 50),
        "glow": (255, 100, 110),
    },
    "difficile": {
        "label": "Difficile",
        "spawn_ms": 360,
        "speed": 10,
        "max_lasers": 28,
        "color": (50, 110, 255),
        "glow": (100, 170, 255),
    },
}
SHIELD_DURATION_MS = 2000
SHIELD_RADIUS_EXTRA = 14

MEDKIT_SIZE = 34
MEDKIT_SPEED = 4
MEDKIT_HEAL = 30
MEDKIT_SPAWN_MS = 5000
MAX_MEDKITS = 2
MEDKIT_COLOR = (40, 180, 90)
MEDKIT_BORDER = (120, 255, 160)
MEDKIT_CROSS = (230, 255, 240)

ASSETS_DIR = Path(__file__).parent
NAHLA_PHOTO = ASSETS_DIR / "WhatsApp Image 2026-04-24 at 00.18.56.jpeg"
NAHLA_HEAD = ASSETS_DIR / "nahla_head.png"

CROP_LEFT = 0.24
CROP_TOP = 0.12
CROP_WIDTH = 0.52
CROP_HEIGHT = 0.40


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


def scale_nahla(source, size):
    if source.get_size() == (size, size):
        return source
    return pygame.transform.smoothscale(source, (size, size))


def difficulty_rects():
    gap = 20
    total_w = 2 * DIFF_BTN_WIDTH + gap
    start_x = (WIDTH - total_w) // 2
    y = 400
    return {
        "normal": pygame.Rect(start_x, y, DIFF_BTN_WIDTH, DIFF_BTN_HEIGHT),
        "difficile": pygame.Rect(start_x + DIFF_BTN_WIDTH + gap, y, DIFF_BTN_WIDTH, DIFF_BTN_HEIGHT),
    }


def play_button_rect():
    return pygame.Rect(
        (WIDTH - BUTTON_WIDTH) // 2,
        470,
        BUTTON_WIDTH,
        BUTTON_HEIGHT,
    )


def player_hitbox(player_x, player_y):
    inset = PLAYER_HIT_INSET
    return pygame.Rect(
        player_x + inset,
        player_y + inset,
        PLAYER_SIZE - inset * 2,
        PLAYER_SIZE - inset * 2,
    )


class GameState:
    def __init__(self, difficulty="normal"):
        self.difficulty = difficulty
        self.settings = DIFFICULTIES[difficulty]
        self.reset()

    def reset(self):
        self.player_x, self.player_y = reset_player()
        self.hp = MAX_HP
        self.lasers = []
        self.medkits = []
        self.game_over = False
        now = pygame.time.get_ticks()
        self.start_ticks = now
        self.last_spawn = now
        self.last_medkit_spawn = now
        self.shield_until = 0
        self.final_score = 0

    def shield_active(self, now=None):
        if now is None:
            now = pygame.time.get_ticks()
        return now < self.shield_until

    def score_seconds(self):
        if self.game_over:
            return self.final_score
        return (pygame.time.get_ticks() - self.start_ticks) // 1000

    def spawn_laser(self):
        cfg = self.settings
        if len(self.lasers) >= cfg["max_lasers"]:
            return

        speed = cfg["speed"]
        side = random.choice(("down", "up", "left", "right"))
        if side == "down":
            x = random.randint(20, WIDTH - LASER_WIDTH - 20)
            rect = pygame.Rect(x, -LASER_HEIGHT, LASER_WIDTH, LASER_HEIGHT)
            vx, vy = 0, speed
        elif side == "up":
            x = random.randint(20, WIDTH - LASER_WIDTH - 20)
            rect = pygame.Rect(x, HEIGHT + 5, LASER_WIDTH, LASER_HEIGHT)
            vx, vy = 0, -speed
        elif side == "left":
            y = random.randint(40, HEIGHT - LASER_WIDTH - 40)
            rect = pygame.Rect(WIDTH + 5, y, LASER_HEIGHT, LASER_WIDTH)
            vx, vy = -speed, 0
        else:
            y = random.randint(40, HEIGHT - LASER_WIDTH - 40)
            rect = pygame.Rect(-LASER_HEIGHT - 5, y, LASER_HEIGHT, LASER_WIDTH)
            vx, vy = speed, 0

        self.lasers.append({"rect": rect, "vx": vx, "vy": vy})

    @staticmethod
    def _laser_on_screen(laser):
        r = laser["rect"]
        vx, vy = laser["vx"], laser["vy"]
        m = LASER_OFFSCREEN_MARGIN
        if vx > 0 and r.left > WIDTH + m:
            return False
        if vx < 0 and r.right < -m:
            return False
        if vy > 0 and r.top > HEIGHT + m:
            return False
        if vy < 0 and r.bottom < -m:
            return False
        return True

    def spawn_medkit(self):
        if len(self.medkits) >= MAX_MEDKITS:
            return
        x = random.randint(30, WIDTH - MEDKIT_SIZE - 30)
        rect = pygame.Rect(x, -MEDKIT_SIZE, MEDKIT_SIZE, MEDKIT_SIZE)
        self.medkits.append(rect)

    def update(self, keys):
        if self.game_over:
            return

        now = pygame.time.get_ticks()
        if now - self.last_spawn >= self.settings["spawn_ms"]:
            self.spawn_laser()
            self.last_spawn = now

        if now - self.last_medkit_spawn >= MEDKIT_SPAWN_MS and self.hp < MAX_HP:
            self.spawn_medkit()
            self.last_medkit_spawn = now

        for laser in self.lasers:
            laser["rect"].x += laser["vx"]
            laser["rect"].y += laser["vy"]

        for medkit in self.medkits:
            medkit.y += MEDKIT_SPEED

        self.lasers = [lz for lz in self.lasers if self._laser_on_screen(lz)]
        self.medkits = [mk for mk in self.medkits if mk.top < HEIGHT + 20]

        self.player_x, self.player_y = update_player(keys, self.player_x, self.player_y)
        hitbox = player_hitbox(self.player_x, self.player_y)

        for medkit in self.medkits[:]:
            if hitbox.colliderect(medkit):
                self.hp = min(MAX_HP, self.hp + MEDKIT_HEAL)
                self.medkits.remove(medkit)

        for laser in self.lasers[:]:
            if hitbox.colliderect(laser["rect"]):
                self.lasers.remove(laser)
                if not self.shield_active(now):
                    self.hp -= LASER_DAMAGE
                    self.shield_until = now + SHIELD_DURATION_MS
                break

        if self.hp <= 0:
            self.hp = 0
            if not self.game_over:
                self.final_score = self.score_seconds()
            self.game_over = True


def draw_menu(
    screen,
    font_title,
    font_button,
    font_hint,
    nahla_preview,
    hover_play,
    selected_diff,
    mouse_pos,
):
    screen.fill(BG_COLOR)

    title = font_title.render("Nahla vs le laser", True, ACCENT)
    screen.blit(title, title.get_rect(center=(WIDTH // 2, 100)))

    preview_rect = nahla_preview.get_rect(center=(WIDTH // 2, 250))
    screen.blit(nahla_preview, preview_rect)

    diff_label = font_hint.render("Difficulté", True, TEXT_COLOR)
    screen.blit(diff_label, diff_label.get_rect(center=(WIDTH // 2, 370)))

    for key, rect in difficulty_rects().items():
        cfg = DIFFICULTIES[key]
        selected = key == selected_diff
        hovered = rect.collidepoint(mouse_pos)
        if selected:
            color = BUTTON_SELECTED
        elif hovered:
            color = BUTTON_HOVER
        else:
            color = BUTTON_COLOR
        pygame.draw.rect(screen, color, rect, border_radius=8)
        border = BUTTON_BORDER if selected else (70, 70, 80)
        if key == "difficile" and selected:
            border = cfg["color"]
        pygame.draw.rect(screen, border, rect, width=2, border_radius=8)
        label = font_button.render(cfg["label"], True, TEXT_COLOR)
        screen.blit(label, label.get_rect(center=rect.center))

    rect = play_button_rect()
    color = BUTTON_HOVER if hover_play else BUTTON_COLOR
    pygame.draw.rect(screen, color, rect, border_radius=8)
    pygame.draw.rect(screen, BUTTON_BORDER, rect, width=3, border_radius=8)

    label = font_button.render("Jouer", True, TEXT_COLOR)
    screen.blit(label, label.get_rect(center=rect.center))

    hint = font_hint.render("Clic, Entrée ou Espace", True, (140, 140, 150))
    screen.blit(hint, hint.get_rect(center=(WIDTH // 2, rect.bottom + 24)))


def draw_lasers(screen, lasers, settings):
    color = settings["color"]
    glow = settings["glow"]
    for laser in lasers:
        beam = laser["rect"]
        glow_rect = beam.inflate(8, 4)
        pygame.draw.rect(screen, glow, glow_rect, border_radius=4)
        pygame.draw.rect(screen, color, beam, border_radius=3)


def draw_medkits(screen, medkits):
    for kit in medkits:
        pygame.draw.rect(screen, MEDKIT_BORDER, kit.inflate(6, 6), border_radius=6)
        pygame.draw.rect(screen, MEDKIT_COLOR, kit, border_radius=5)
        cx, cy = kit.center
        arm = MEDKIT_SIZE // 2 - 6
        pygame.draw.rect(
            screen,
            MEDKIT_CROSS,
            (cx - 3, cy - arm, 6, arm * 2),
            border_radius=2,
        )
        pygame.draw.rect(
            screen,
            MEDKIT_CROSS,
            (cx - arm, cy - 3, arm * 2, 6),
            border_radius=2,
        )


def settings_mode_color(game):
    if game.difficulty == "difficile":
        return DIFFICULTIES["difficile"]["color"]
    return (160, 160, 170)


def hp_bar_color(hp):
    if hp > 60:
        return HP_COLOR_HIGH
    if hp > 30:
        return HP_COLOR_MID
    return HP_COLOR_LOW


def draw_shield(screen, player_x, player_y, now, shield_until):
    if now >= shield_until:
        return

    pulse = math.sin(now / 70) * 4
    radius = PLAYER_SIZE // 2 + SHIELD_RADIUS_EXTRA + int(pulse)
    cx = player_x + PLAYER_SIZE // 2
    cy = player_y + PLAYER_SIZE // 2
    size = radius * 2 + 24
    surf = pygame.Surface((size, size), pygame.SRCALPHA)
    center = (size // 2, size // 2)
    pygame.draw.circle(surf, (50, 130, 255, 75), center, radius)
    pygame.draw.circle(surf, (140, 210, 255, 130), center, radius, width=4)
    pygame.draw.circle(surf, (220, 240, 255, 180), center, radius - 6, width=2)
    screen.blit(surf, (cx - size // 2, cy - size // 2))


def draw_health_bar(screen, hp, font_ui):
    x = WIDTH - HP_BAR_WIDTH - HP_BAR_MARGIN
    y = HP_BAR_MARGIN
    frame = pygame.Rect(x, y, HP_BAR_WIDTH, HP_BAR_HEIGHT)

    pygame.draw.rect(screen, HP_BG, frame, border_radius=6)
    pygame.draw.rect(screen, HP_BORDER, frame, width=2, border_radius=6)

    fill_w = int(HP_BAR_WIDTH * max(0, min(hp, MAX_HP)) / MAX_HP)
    if fill_w > 0:
        fill = pygame.Rect(x + 2, y + 2, max(0, fill_w - 4), HP_BAR_HEIGHT - 4)
        pygame.draw.rect(screen, hp_bar_color(hp), fill, border_radius=4)

    label = font_ui.render(f"Vie {hp}/{MAX_HP}", True, TEXT_COLOR)
    label_rect = label.get_rect(midright=(frame.right, frame.bottom + 14))
    screen.blit(label, label_rect)


def draw_game(screen, nahla, game, font_hint, font_ui, font_big):
    screen.fill(BG_COLOR)
    draw_lasers(screen, game.lasers, game.settings)

    mode = font_ui.render(game.settings["label"], True, settings_mode_color(game))
    screen.blit(mode, (WIDTH - mode.get_width() - 14, 50))
    draw_medkits(screen, game.medkits)
    now = pygame.time.get_ticks()
    if game.shield_active(now):
        draw_shield(screen, game.player_x, game.player_y, now, game.shield_until)
    screen.blit(nahla, (game.player_x, game.player_y))
    draw_health_bar(screen, game.hp, font_ui)

    score_text = font_ui.render(f"Temps {game.score_seconds()} s", True, (160, 160, 170))
    screen.blit(score_text, (12, 12))

    hint = font_hint.render(
        "Flèches / ZQSD — bouclier 2 s après un hit — Échap = menu",
        True,
        (100, 100, 110),
    )
    screen.blit(hint, (12, 36))

    if game.game_over:
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 170))
        screen.blit(overlay, (0, 0))

        go = font_big.render("Game Over", True, (255, 70, 70))
        screen.blit(go, go.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50)))

        final = font_ui.render(
            f"Survie : {game.score_seconds()} s — R = rejouer",
            True,
            TEXT_COLOR,
        )
        screen.blit(final, final.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 5)))


def update_player(keys, player_x, player_y):
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x += PLAYER_SPEED
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_y -= PLAYER_SPEED
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_y += PLAYER_SPEED

    player_x = max(PLAYER_MARGIN_SIDE, min(WIDTH - PLAYER_SIZE - PLAYER_MARGIN_SIDE, player_x))
    player_y = max(
        PLAYER_MARGIN_TOP,
        min(HEIGHT - PLAYER_SIZE - PLAYER_MARGIN_BOTTOM, player_y),
    )
    return player_x, player_y


def reset_player():
    x = (WIDTH - PLAYER_SIZE) // 2
    y = HEIGHT - PLAYER_SIZE - PLAYER_MARGIN_BOTTOM
    return x, y


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    font_title = pygame.font.SysFont(None, 64)
    font_button = pygame.font.SysFont(None, 40)
    font_hint = pygame.font.SysFont(None, 26)
    font_ui = pygame.font.SysFont(None, 24)
    font_big = pygame.font.SysFont(None, 56)

    nahla_source = load_nahla_source()
    nahla = scale_nahla(nahla_source, PLAYER_SIZE)
    menu_preview = scale_nahla(nahla_source, MENU_PREVIEW_SIZE)

    state = MENU
    selected_difficulty = "normal"
    game = None
    running = True

    while running:
        hover_play = False
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if state == PLAYING:
                        state = MENU
                        game = None
                    else:
                        running = False
                elif state == MENU and event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    game = GameState(selected_difficulty)
                    state = PLAYING
                elif state == PLAYING and game and game.game_over and event.key == pygame.K_r:
                    game.reset()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if state == MENU:
                    if play_button_rect().collidepoint(event.pos):
                        game = GameState(selected_difficulty)
                        state = PLAYING
                    else:
                        for key, rect in difficulty_rects().items():
                            if rect.collidepoint(event.pos):
                                selected_difficulty = key
                                break

        if state == MENU:
            if play_button_rect().collidepoint(mouse_pos):
                hover_play = True
            draw_menu(
                screen,
                font_title,
                font_button,
                font_hint,
                menu_preview,
                hover_play,
                selected_difficulty,
                mouse_pos,
            )
        elif game:
            keys = pygame.key.get_pressed()
            game.update(keys)
            draw_game(screen, nahla, game, font_hint, font_ui, font_big)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
