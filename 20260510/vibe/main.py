import array
import json
import math
import pygame
import random
import sys
from pathlib import Path

SCORES_FILE = Path(__file__).parent / "scores.json"
LEGACY_SCORE_FILE = Path(__file__).parent / "highscore.txt"

WIDTH = 800
HEIGHT = 600
TITLE = "Snake"
BG_COLOR = (8, 8, 12)
GRID_COLOR = (28, 32, 40)
BORDER_COLOR = (0, 140, 70)
CELL_SIZE = 20

MENU = "menu"
PLAYING = "playing"

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 44
BUTTON_COLOR = (40, 40, 48)
BUTTON_BORDER = (0, 200, 80)
BUTTON_HOVER = (58, 58, 68)
BUTTON_SELECTED = (30, 70, 45)
TEXT_COLOR = (255, 255, 255)
MUTED = (160, 165, 175)

GRID_W = WIDTH // CELL_SIZE
GRID_H = HEIGHT // CELL_SIZE

DIFFICULTIES = {
    "facile": {"label": "Facile", "base_ms": 165},
    "normal": {"label": "Normal", "base_ms": 120},
    "rapide": {"label": "Rapide", "base_ms": 82},
}

COUNTDOWN_STEP_MS = 850
SPEED_BONUS_EVERY = 5
SPEED_BONUS_MS = 7
MIN_MOVE_MS = 42


def make_tone(freq, duration_ms=90, volume=0.22):
    sample_rate = 22050
    n = int(sample_rate * duration_ms / 1000)
    buf = array.array("h")
    amp = int(32767 * volume)
    for i in range(n):
        t = i / sample_rate
        v = int(amp * math.sin(2 * math.pi * freq * t))
        buf.append(v)
        buf.append(v)
    return pygame.mixer.Sound(buffer=buf)


def load_top_scores():
    scores = []
    if SCORES_FILE.exists():
        try:
            raw = json.loads(SCORES_FILE.read_text())
            scores = sorted({int(s) for s in raw}, reverse=True)
        except (json.JSONDecodeError, TypeError, ValueError):
            pass
    elif LEGACY_SCORE_FILE.exists():
        try:
            legacy = int(LEGACY_SCORE_FILE.read_text().strip())
            if legacy > 0:
                scores = [legacy]
        except ValueError:
            pass
    return scores[:5]


def save_top_scores(scores):
    SCORES_FILE.write_text(json.dumps(scores[:5]))


def register_score(score):
    if score <= 0:
        return load_top_scores(), False
    scores = load_top_scores()
    was_record = not scores or score > scores[0]
    scores.append(score)
    scores = sorted(scores, reverse=True)[:5]
    save_top_scores(scores)
    return scores, was_record


class Particle:
    __slots__ = ("x", "y", "vx", "vy", "life", "color")

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.vx = random.uniform(-3.5, 3.5)
        self.vy = random.uniform(-3.5, 3.5)
        self.life = 22
        self.color = color

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.life -= 1

    def draw(self, screen):
        alpha = max(0, min(255, self.life * 12))
        size = max(2, self.life // 3)
        surf = pygame.Surface((size * 2, size * 2), pygame.SRCALPHA)
        c = (*self.color[:3], alpha)
        pygame.draw.circle(surf, c, (size, size), size)
        screen.blit(surf, (int(self.x), int(self.y)))


class SnakeGame:
    def __init__(self, difficulty, wrap_walls):
        self.difficulty = difficulty
        self.wrap_walls = wrap_walls
        self.sounds = {}
        self.reset()

    def set_sounds(self, eat_snd, power_snd, over_snd):
        self.sounds = {"eat": eat_snd, "power": power_snd, "over": over_snd}

    def reset(self):
        cx, cy = GRID_W // 2, GRID_H // 2
        self.snake = [(cx, cy), (cx - 1, cy), (cx - 2, cy)]
        self.direction = (1, 0)
        self.next_direction = (1, 0)
        self.score = 0
        self.game_over = False
        self.paused = False
        self.high_score_handled = False
        self.new_record = False
        self.last_move = pygame.time.get_ticks()
        self.slow_until = 0
        self.particles = []
        self.eat_flash = 0
        self._spawn_food()

    def _empty_cell(self):
        while True:
            pos = (random.randint(0, GRID_W - 1), random.randint(0, GRID_H - 1))
            if pos not in self.snake:
                return pos

    def _spawn_food(self):
        self.apple = self._empty_cell()
        roll = random.random()
        if roll < 0.08:
            self.food_type = "golden"
        elif roll < 0.14:
            self.food_type = "slow"
        else:
            self.food_type = "normal"

    def move_interval_ms(self):
        base = DIFFICULTIES[self.difficulty]["base_ms"]
        bonus = (self.score // SPEED_BONUS_EVERY) * SPEED_BONUS_MS
        ms = max(MIN_MOVE_MS, base - bonus)
        if pygame.time.get_ticks() < self.slow_until:
            ms = int(ms * 1.75)
        return ms

    def set_direction(self, dx, dy):
        cur_dx, cur_dy = self.direction
        if (dx, dy) == (-cur_dx, -cur_dy):
            return
        self.next_direction = (dx, dy)

    def toggle_pause(self):
        if not self.game_over:
            self.paused = not self.paused

    def _play(self, name):
        snd = self.sounds.get(name)
        if snd:
            snd.play()

    def _spawn_particles(self, gx, gy, color, count=14):
        px = gx * CELL_SIZE + CELL_SIZE // 2
        py = gy * CELL_SIZE + CELL_SIZE // 2
        for _ in range(count):
            self.particles.append(Particle(px, py, color))

    def update(self, can_move):
        if self.game_over or self.paused or not can_move:
            return

        now = pygame.time.get_ticks()
        if now - self.last_move < self.move_interval_ms():
            return
        self.last_move = now

        self.direction = self.next_direction
        dx, dy = self.direction
        head_x, head_y = self.snake[0]
        nx, ny = head_x + dx, head_y + dy

        if self.wrap_walls:
            nx %= GRID_W
            ny %= GRID_H
            new_head = (nx, ny)
        else:
            new_head = (nx, ny)
            if not (0 <= nx < GRID_W and 0 <= ny < GRID_H):
                self.game_over = True
                self._play("over")
                return

        if new_head in self.snake:
            self.game_over = True
            self._play("over")
            return

        self.snake.insert(0, new_head)
        ate = new_head == self.apple

        if ate:
            self.eat_flash = 8
            if self.food_type == "golden":
                self.score += 2
                self._spawn_particles(self.apple[0], self.apple[1], (255, 210, 40))
                self._play("power")
            elif self.food_type == "slow":
                self.score += 1
                self.slow_until = now + 5000
                self._spawn_particles(self.apple[0], self.apple[1], (80, 160, 255))
                self._play("power")
            else:
                self.score += 1
                self._spawn_particles(self.apple[0], self.apple[1], (220, 50, 50))
                self._play("eat")
            self._spawn_food()
        else:
            self.snake.pop()

        for p in self.particles:
            p.update()
        self.particles = [p for p in self.particles if p.life > 0]

    def draw(self, screen, font_ui, font_big, top_scores, countdown_text=None):
        screen.fill(BG_COLOR)

        play_rect = pygame.Rect(0, 0, WIDTH, HEIGHT)
        pygame.draw.rect(screen, BORDER_COLOR, play_rect, width=3)

        for x in range(GRID_W + 1):
            pygame.draw.line(
                screen, GRID_COLOR, (x * CELL_SIZE, 0), (x * CELL_SIZE, HEIGHT)
            )
        for y in range(GRID_H + 1):
            pygame.draw.line(
                screen, GRID_COLOR, (0, y * CELL_SIZE), (WIDTH, y * CELL_SIZE)
            )

        ax, ay = self.apple
        apple_rect = pygame.Rect(ax * CELL_SIZE, ay * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        if self.food_type == "golden":
            pygame.draw.rect(screen, (255, 200, 30), apple_rect, border_radius=4)
            pygame.draw.rect(screen, (255, 240, 120), apple_rect, width=2, border_radius=4)
        elif self.food_type == "slow":
            pygame.draw.rect(screen, (50, 120, 255), apple_rect, border_radius=4)
            pygame.draw.rect(screen, (140, 200, 255), apple_rect, width=2, border_radius=4)
        else:
            pygame.draw.rect(screen, (210, 35, 45), apple_rect, border_radius=3)

        last = len(self.snake) - 1
        for i, (sx, sy) in enumerate(self.snake):
            rect = pygame.Rect(sx * CELL_SIZE, sy * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if i == 0:
                color = (80, 255, 150)
            elif i == last:
                color = (0, 110, 55)
            else:
                color = (0, 200, 90)
            pygame.draw.rect(screen, color, rect.inflate(-2, -2), border_radius=3)

        for p in self.particles:
            p.draw(screen)

        if self.eat_flash > 0:
            flash = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            flash.fill((255, 255, 255, min(50, self.eat_flash * 8)))
            screen.blit(flash, (0, 0))
            self.eat_flash -= 1

        mode = "Sans murs" if self.wrap_walls else "Murs"
        diff = DIFFICULTIES[self.difficulty]["label"]
        hud = font_ui.render(
            f"Score : {self.score}   |   {diff}   |   {mode}", True, TEXT_COLOR
        )
        screen.blit(hud, (12, 10))

        if top_scores:
            rec = font_ui.render(f"Top : {top_scores[0]}", True, MUTED)
            screen.blit(rec, rec.get_rect(topright=(WIDTH - 12, 10)))

        if self.slow_until > pygame.time.get_ticks():
            slow = font_ui.render("Ralenti !", True, (120, 180, 255))
            screen.blit(slow, (12, 42))

        legend = font_ui.render(
            "P = pause   |   Dorée x2   |   Bleue = ralenti", True, MUTED
        )
        screen.blit(legend, legend.get_rect(midbottom=(WIDTH // 2, HEIGHT - 8)))

        if countdown_text:
            cd = font_big.render(countdown_text, True, (0, 255, 130))
            screen.blit(cd, cd.get_rect(center=(WIDTH // 2, HEIGHT // 2)))

        if self.paused and not self.game_over:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 170))
            screen.blit(overlay, (0, 0))
            pause = font_big.render("Pause", True, TEXT_COLOR)
            screen.blit(pause, pause.get_rect(center=(WIDTH // 2, HEIGHT // 2)))

        if self.game_over:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 165))
            screen.blit(overlay, (0, 0))

            go = font_big.render("Game Over", True, (255, 80, 80))
            screen.blit(go, go.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 55)))

            final = font_ui.render(f"Score final : {self.score}", True, TEXT_COLOR)
            screen.blit(final, final.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 10)))

            if self.new_record:
                record = font_ui.render("Nouveau record !", True, (255, 220, 0))
                screen.blit(record, record.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 22)))

            hint = font_ui.render("R = rejouer   |   Échap = menu", True, TEXT_COLOR)
            screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 58)))


def play_button_rect():
    return pygame.Rect((WIDTH - BUTTON_WIDTH) // 2, 430, BUTTON_WIDTH, BUTTON_HEIGHT)


def difficulty_rects():
    labels = ["facile", "normal", "rapide"]
    gap = 12
    total_w = 3 * BUTTON_WIDTH + 2 * gap
    start_x = (WIDTH - total_w) // 2
    rects = {}
    for i, key in enumerate(labels):
        x = start_x + i * (BUTTON_WIDTH + gap)
        rects[key] = pygame.Rect(x, 300, BUTTON_WIDTH, BUTTON_HEIGHT)
    return rects


def walls_toggle_rect():
    return pygame.Rect((WIDTH - 280) // 2, 370, 280, BUTTON_HEIGHT)


def handle_direction_keys(game, key):
    if key in (pygame.K_UP, pygame.K_w):
        game.set_direction(0, -1)
    elif key in (pygame.K_DOWN, pygame.K_s):
        game.set_direction(0, 1)
    elif key in (pygame.K_LEFT, pygame.K_a):
        game.set_direction(-1, 0)
    elif key in (pygame.K_RIGHT, pygame.K_d):
        game.set_direction(1, 0)


def draw_menu(screen, fonts, hover_play, selected_diff, wrap_walls, top_scores):
    font_title, font_button, font_ui = fonts
    screen.fill(BG_COLOR)

    title = font_title.render("Snake", True, (0, 220, 100))
    screen.blit(title, title.get_rect(center=(WIDTH // 2, 70)))

    hint = font_ui.render("Flèches ou ZQSD / WASD en jeu", True, MUTED)
    screen.blit(hint, hint.get_rect(center=(WIDTH // 2, 130)))

    diff_label = font_ui.render("Difficulté", True, TEXT_COLOR)
    screen.blit(diff_label, diff_label.get_rect(center=(WIDTH // 2, 265)))

    for key, rect in difficulty_rects().items():
        selected = key == selected_diff
        hovered = rect.collidepoint(pygame.mouse.get_pos())
        if selected:
            color = BUTTON_SELECTED
        elif hovered:
            color = BUTTON_HOVER
        else:
            color = BUTTON_COLOR
        pygame.draw.rect(screen, color, rect, border_radius=8)
        border = BUTTON_BORDER if selected else (70, 70, 80)
        pygame.draw.rect(screen, border, rect, width=2, border_radius=8)
        label = font_button.render(DIFFICULTIES[key]["label"], True, TEXT_COLOR)
        screen.blit(label, label.get_rect(center=rect.center))

    wrect = walls_toggle_rect()
    whover = wrect.collidepoint(pygame.mouse.get_pos())
    wcolor = BUTTON_HOVER if whover else BUTTON_COLOR
    pygame.draw.rect(screen, wcolor, wrect, border_radius=8)
    pygame.draw.rect(screen, BUTTON_BORDER if wrap_walls else (70, 70, 80), wrect, width=2, border_radius=8)
    wlabel = "Mode : Sans murs ✓" if wrap_walls else "Mode : Murs (clic pour sans murs)"
    wtext = font_button.render(wlabel, True, TEXT_COLOR)
    screen.blit(wtext, wtext.get_rect(center=wrect.center))

    rect = play_button_rect()
    color = BUTTON_HOVER if hover_play else BUTTON_COLOR
    pygame.draw.rect(screen, color, rect, border_radius=8)
    pygame.draw.rect(screen, BUTTON_BORDER, rect, width=3, border_radius=8)
    label = font_button.render("Jouer", True, TEXT_COLOR)
    screen.blit(label, label.get_rect(center=rect.center))

    if top_scores:
        y = 500
        header = font_ui.render("Top 5 scores", True, (0, 200, 100))
        screen.blit(header, header.get_rect(center=(WIDTH // 2, y)))
        for i, sc in enumerate(top_scores[:5], start=1):
            line = font_ui.render(f"{i}. {sc}", True, MUTED)
            screen.blit(line, line.get_rect(center=(WIDTH // 2, y + 28 + i * 22)))


def countdown_label(countdown_end):
    left = countdown_end - pygame.time.get_ticks()
    if left > COUNTDOWN_STEP_MS * 3:
        return "3"
    if left > COUNTDOWN_STEP_MS * 2:
        return "2"
    if left > COUNTDOWN_STEP_MS:
        return "1"
    if left > 0:
        return "GO !"
    return None


def start_playing(game, difficulty, wrap_walls, sounds):
    g = SnakeGame(difficulty, wrap_walls)
    g.set_sounds(*sounds)
    end = pygame.time.get_ticks() + COUNTDOWN_STEP_MS * 4 + 200
    return g, end


def main():
    pygame.init()
    pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    font_title = pygame.font.SysFont(None, 80)
    font_button = pygame.font.SysFont(None, 34)
    font_ui = pygame.font.SysFont(None, 28)
    font_big = pygame.font.SysFont(None, 72)
    fonts_menu = (font_title, font_button, font_ui)

    sounds = (
        make_tone(520, 70),
        make_tone(780, 110),
        make_tone(180, 280, volume=0.28),
    )

    state = MENU
    selected_diff = "normal"
    wrap_walls = False
    top_scores = load_top_scores()
    game = None
    countdown_end = 0
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

                elif state == MENU:
                    if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                        game, countdown_end = start_playing(
                            game, selected_diff, wrap_walls, sounds
                        )
                        state = PLAYING

                elif state == PLAYING and game:
                    if event.key == pygame.K_p:
                        game.toggle_pause()
                    elif event.key == pygame.K_r and game.game_over:
                        game.reset()
                        countdown_end = pygame.time.get_ticks() + COUNTDOWN_STEP_MS * 4 + 200
                    else:
                        handle_direction_keys(game, event.key)

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if state == MENU:
                    if play_button_rect().collidepoint(event.pos):
                        game, countdown_end = start_playing(
                            game, selected_diff, wrap_walls, sounds
                        )
                        state = PLAYING
                    elif walls_toggle_rect().collidepoint(event.pos):
                        wrap_walls = not wrap_walls
                    else:
                        for key, rect in difficulty_rects().items():
                            if rect.collidepoint(event.pos):
                                selected_diff = key
                                break

        if state == MENU:
            hover_play = play_button_rect().collidepoint(mouse_pos)
            draw_menu(
                screen,
                fonts_menu,
                hover_play,
                selected_diff,
                wrap_walls,
                top_scores,
            )
        elif game:
            cd = countdown_label(countdown_end)
            can_move = cd is None
            game.update(can_move)
            if game.game_over and not game.high_score_handled:
                game.high_score_handled = True
                top_scores, game.new_record = register_score(game.score)
            game.draw(screen, font_ui, font_big, top_scores, cd)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
