"""Nahla Pong — la croquette contre le monde."""

import math
import random
import sys
from pathlib import Path

import pygame

WIDTH, HEIGHT = 960, 640
FPS = 60
TITLE = "Nahla Pong"
WIN_SCORE = 7

ASSETS = Path(__file__).parent
NAHLA_HEAD = ASSETS / "nahla_head.png"

COUCH = (196, 168, 132)
COUCH_DARK = (168, 142, 108)
COUCH_LIGHT = (210, 188, 158)
TEXT = (55, 40, 28)
MUTED = (110, 90, 70)
ACCENT = (255, 210, 80)
CROQUETTE = (180, 120, 40)
CROQUETTE_LIGHT = (220, 170, 80)
OPPONENT = (90, 130, 170)
MALIK = (255, 180, 100)
DANGER = (200, 70, 70)
WIN_C = (80, 180, 100)

NAHLA_W, NAHLA_H = 108, 60
PADDLE_W, PADDLE_H = 130, 22
BALL_R = 13
BASE_SPEED = 5.5
MAX_SPEED = 11
PADDLE_SPEED = 9
OPPONENT_SPEED = 6
SERVE_MS = 900

DIFFICULTIES = {
    "facile": {
        "label": "Facile",
        "desc": "Aspirateur lent · Malik tranquille",
        "opponent_speed": 3.5,
        "opponent_slop": 18,
        "opponent_miss": 0.22,
        "malik_speed": 1.4,
        "malik_w": 58,
        "malik_h": 30,
        "base_speed": 4.5,
        "max_speed": 9,
        "speed_gain": 0.25,
        "color": WIN_C,
    },
    "normal": {
        "label": "Normal",
        "desc": "Équilibré · comme avant",
        "opponent_speed": 6,
        "opponent_slop": 8,
        "opponent_miss": 0.08,
        "malik_speed": 2.2,
        "malik_w": 72,
        "malik_h": 36,
        "base_speed": 5.5,
        "max_speed": 11,
        "speed_gain": 0.35,
        "color": ACCENT,
    },
    "enfer": {
        "label": "Enfer",
        "desc": "Aspirateur rapide · Malik en furie",
        "opponent_speed": 8.5,
        "opponent_slop": 3,
        "opponent_miss": 0.02,
        "malik_speed": 4.2,
        "malik_w": 96,
        "malik_h": 46,
        "base_speed": 6.8,
        "max_speed": 14,
        "speed_gain": 0.5,
        "color": DANGER,
    },
}

DIFF_KEYS = ["facile", "normal", "enfer"]

WIN_PHRASES = [
    "Nahla accepte ce point. À contrecœur.",
    "La croquette obéit à Nahla.",
    "Tu sers bien ton maître.",
]
LOSE_PHRASES = [
    "Nahla te juge.",
    "Pathétique. Elle s'attendait à mieux.",
    "La croquette t'a trahi.",
    "Malik aurait fait mieux. (mensonge)",
]
MALIK_PHRASES = [
    "Malik traverse le salon !!",
    "Malik bloque tout !!",
    "Attention Malik !!",
]


def load_nahla():
    if NAHLA_HEAD.exists():
        img = pygame.image.load(str(NAHLA_HEAD)).convert_alpha()
        return pygame.transform.smoothscale(img, (NAHLA_W, NAHLA_H))
    surf = pygame.Surface((NAHLA_W, NAHLA_H), pygame.SRCALPHA)
    pygame.draw.ellipse(surf, ACCENT, surf.get_rect())
    return surf


def clamp_speed(vx, vy, speed):
    mag = math.hypot(vx, vy) or 1
    vx = vx / mag * speed
    vy = vy / mag * speed
    return vx, vy


def reset_ball(toward_player=False, diff=None):
    diff = diff or DIFFICULTIES["normal"]
    angle = random.uniform(-0.6, 0.6)
    speed = diff["base_speed"]
    vy = speed if toward_player else -speed
    vx = math.sin(angle) * speed
    return {
        "x": WIDTH / 2,
        "y": HEIGHT / 2,
        "vx": vx,
        "vy": vy,
        "speed": speed,
    }


def bounce_off_paddle(ball, paddle, going_down, diff):
    rel = (ball["x"] - paddle.centerx) / (paddle.width / 2)
    rel = max(-1, min(1, rel))
    ball["speed"] = min(diff["max_speed"], ball["speed"] + diff["speed_gain"])
    angle = rel * 0.75
    vy_sign = 1 if going_down else -1
    ball["vx"] = math.sin(angle) * ball["speed"]
    ball["vy"] = vy_sign * math.cos(angle) * ball["speed"]
    if abs(ball["vy"]) < 2:
        ball["vy"] = vy_sign * 2


def spawn_particles(x, y, color, count=8):
    parts = []
    for _ in range(count):
        ang = random.uniform(0, math.pi * 2)
        spd = random.uniform(1.5, 4.5)
        parts.append({
            "x": x, "y": y,
            "vx": math.cos(ang) * spd,
            "vy": math.sin(ang) * spd,
            "life": random.randint(200, 450),
            "color": color,
            "r": random.randint(3, 6),
        })
    return parts


def draw_dotted_line(surface, y):
    for x in range(0, WIDTH, 24):
        pygame.draw.rect(surface, COUCH_DARK, (x, y - 2, 12, 4), border_radius=2)


def draw_menu(screen, font_big, font, font_small, selected):
    screen.fill(COUCH)
    title = font_big.render("Nahla Pong", True, TEXT)
    screen.blit(title, title.get_rect(center=(WIDTH // 2, 100)))
    sub = font.render("Choisis la difficulté", True, MUTED)
    screen.blit(sub, sub.get_rect(center=(WIDTH // 2, 155)))

    for i, key in enumerate(DIFF_KEYS):
        diff = DIFFICULTIES[key]
        y = 230 + i * 110
        box = pygame.Rect(WIDTH // 2 - 220, y, 440, 88)
        active = key == selected
        bg = COUCH_LIGHT if active else (180, 158, 128)
        pygame.draw.rect(screen, bg, box, border_radius=14)
        pygame.draw.rect(screen, diff["color"] if active else COUCH_DARK, box, 3, border_radius=14)
        num = font_small.render(f"{i + 1}", True, TEXT)
        screen.blit(num, (box.left + 16, box.top + 14))
        label = font.render(diff["label"], True, TEXT)
        screen.blit(label, (box.left + 44, box.top + 16))
        desc = font_small.render(diff["desc"], True, MUTED)
        screen.blit(desc, (box.left + 44, box.top + 50))

    hint = font_small.render("1 / 2 / 3 ou flèches + Entrée · Échap = quitter", True, MUTED)
    screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT - 40)))


def main():
    pygame.init()
    pygame.display.set_caption(TITLE)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font_big = pygame.font.SysFont("Arial", 48, bold=True)
    font = pygame.font.SysFont("Arial", 28)
    font_small = pygame.font.SysFont("Arial", 20)

    nahla_img = load_nahla()
    state = "menu"  # menu | play | win | lose
    diff_key = "normal"
    difficulty = DIFFICULTIES[diff_key]
    menu_index = 1

    def new_game(diff):
        mw, mh = diff["malik_w"], diff["malik_h"]
        return {
            "player": pygame.Rect(WIDTH // 2 - NAHLA_W // 2, HEIGHT - 78, NAHLA_W, NAHLA_H),
            "opponent": pygame.Rect(WIDTH // 2 - PADDLE_W // 2, 48, PADDLE_W, PADDLE_H),
            "malik": pygame.Rect(WIDTH // 2 - mw // 2, HEIGHT // 2 - mh // 2, mw, mh),
            "malik_dir": random.choice([-1, 1]),
            "ball": reset_ball(diff=diff),
            "score_player": 0,
            "score_opponent": 0,
            "rally": 0,
            "serve_timer": SERVE_MS,
            "phrase": "Renvoie la croquette.",
            "phrase_timer": 0,
            "particles": [],
            "trail": [],
            "hit_flash": 0,
            "shake": 0,
            "player_glow": 0,
        }

    g = new_game(difficulty)

    running = True
    while running:
        dt = clock.tick(FPS)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if state == "menu":
                        running = False
                    else:
                        state = "menu"
                elif state == "menu":
                    if event.key in (pygame.K_UP, pygame.K_w):
                        menu_index = (menu_index - 1) % 3
                    elif event.key in (pygame.K_DOWN, pygame.K_s):
                        menu_index = (menu_index + 1) % 3
                    elif event.key in (pygame.K_1, pygame.K_2, pygame.K_3):
                        menu_index = event.key - pygame.K_1
                    elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                        diff_key = DIFF_KEYS[menu_index]
                        difficulty = DIFFICULTIES[diff_key]
                        g = new_game(difficulty)
                        state = "play"
                elif event.key == pygame.K_r and state in ("win", "lose"):
                    g = new_game(difficulty)
                    state = "play"
                elif event.key == pygame.K_m and state in ("win", "lose", "play"):
                    state = "menu"

        if state == "menu":
            draw_menu(screen, font_big, font, font_small, DIFF_KEYS[menu_index])
            pygame.display.flip()
            continue

        if state == "play":
            if keys[pygame.K_LEFT] or keys[pygame.K_q] or keys[pygame.K_a]:
                g["player"].x -= PADDLE_SPEED
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                g["player"].x += PADDLE_SPEED
            g["player"].x = max(16, min(WIDTH - NAHLA_W - 16, g["player"].x))

            # Aspirateur — IA selon difficulté
            target = g["ball"]["x"] - PADDLE_W // 2
            slop = difficulty["opponent_slop"]
            if random.random() > difficulty["opponent_miss"]:
                if g["opponent"].x < target - slop:
                    g["opponent"].x += difficulty["opponent_speed"]
                elif g["opponent"].x > target + slop:
                    g["opponent"].x -= difficulty["opponent_speed"]
            g["opponent"].x = max(16, min(WIDTH - PADDLE_W - 16, g["opponent"].x))

            # Malik traverse le milieu
            g["malik"].x += g["malik_dir"] * difficulty["malik_speed"]
            if g["malik"].left <= 60 or g["malik"].right >= WIDTH - 60:
                g["malik_dir"] *= -1
            if random.random() < 0.003 * (1 + menu_index):
                g["phrase"] = random.choice(MALIK_PHRASES)
                g["phrase_timer"] = 1200

            if g["serve_timer"] > 0:
                g["serve_timer"] -= dt
            else:
                ball = g["ball"]
                ball["x"] += ball["vx"]
                ball["y"] += ball["vy"]

                if ball["x"] - BALL_R <= 0 or ball["x"] + BALL_R >= WIDTH:
                    ball["vx"] *= -1
                    ball["x"] = max(BALL_R, min(WIDTH - BALL_R, ball["x"]))
                    g["particles"] += spawn_particles(ball["x"], ball["y"], COUCH_DARK, 4)

                ball_rect = pygame.Rect(ball["x"] - BALL_R, ball["y"] - BALL_R, BALL_R * 2, BALL_R * 2)

                if ball_rect.colliderect(g["opponent"]) and ball["vy"] < 0:
                    bounce_off_paddle(ball, g["opponent"], going_down=True, diff=difficulty)
                    ball["y"] = g["opponent"].bottom + BALL_R + 1
                    g["rally"] += 1
                    g["particles"] += spawn_particles(ball["x"], ball["y"], OPPONENT, 10)
                    g["hit_flash"] = 120

                if ball_rect.colliderect(g["player"]) and ball["vy"] > 0:
                    bounce_off_paddle(ball, g["player"], going_down=False, diff=difficulty)
                    ball["y"] = g["player"].top - BALL_R - 1
                    g["rally"] += 1
                    g["particles"] += spawn_particles(ball["x"], ball["y"], ACCENT, 12)
                    g["player_glow"] = 180

                if ball_rect.colliderect(g["malik"]):
                    if ball["vx"] > 0:
                        ball["vx"] = -abs(ball["vx"])
                        ball["x"] = g["malik"].left - BALL_R - 1
                    else:
                        ball["vx"] = abs(ball["vx"])
                        ball["x"] = g["malik"].right + BALL_R + 1
                    ball["speed"] = min(difficulty["max_speed"], ball["speed"] + 0.5)
                    ball["vx"], ball["vy"] = clamp_speed(ball["vx"], ball["vy"], ball["speed"])
                    g["particles"] += spawn_particles(ball["x"], ball["y"], MALIK, 14)
                    g["phrase"] = "Malik a touché la croquette !!"
                    g["phrase_timer"] = 1400

                g["trail"].append((ball["x"], ball["y"], 180))
                if len(g["trail"]) > 14:
                    g["trail"].pop(0)

                if ball["y"] < -BALL_R:
                    g["score_player"] += 1
                    g["phrase"] = random.choice(WIN_PHRASES)
                    g["phrase_timer"] = 2000
                    g["ball"] = reset_ball(toward_player=False, diff=difficulty)
                    g["serve_timer"] = SERVE_MS
                    g["rally"] = 0
                    if g["score_player"] >= WIN_SCORE:
                        state = "win"
                elif ball["y"] > HEIGHT + BALL_R:
                    g["score_opponent"] += 1
                    g["phrase"] = random.choice(LOSE_PHRASES)
                    g["phrase_timer"] = 2000
                    g["ball"] = reset_ball(toward_player=True, diff=difficulty)
                    g["serve_timer"] = SERVE_MS
                    g["rally"] = 0
                    g["shake"] = 280
                    if g["score_opponent"] >= WIN_SCORE:
                        state = "lose"

        g["hit_flash"] = max(0, g["hit_flash"] - dt)
        g["player_glow"] = max(0, g["player_glow"] - dt)
        g["phrase_timer"] = max(0, g["phrase_timer"] - dt)
        g["shake"] = max(0, g["shake"] - dt)

        for p in g["particles"]:
            p["x"] += p["vx"]
            p["y"] += p["vy"]
            p["life"] -= dt
        g["particles"] = [p for p in g["particles"] if p["life"] > 0]

        for i, t in enumerate(g["trail"]):
            g["trail"][i] = (t[0], t[1], t[2] - dt * 0.4)
        g["trail"] = [t for t in g["trail"] if t[2] > 0]

        shake_x = random.randint(-4, 4) if g["shake"] > 0 else 0
        shake_y = random.randint(-3, 3) if g["shake"] > 0 else 0

        screen.fill(COUCH)

        # Tapis / ombre salon
        pygame.draw.rect(screen, COUCH_LIGHT, (40, 80, WIDTH - 80, HEIGHT - 160), border_radius=20)
        pygame.draw.rect(screen, COUCH_DARK, (40, 80, WIDTH - 80, HEIGHT - 160), 3, border_radius=20)

        draw_dotted_line(screen, HEIGHT // 2)

        # Trail croquette
        for i, (tx, ty, life) in enumerate(g["trail"]):
            alpha = int(80 * (life / 180) * (i + 1) / len(g["trail"]) if g["trail"] else 0)
            if alpha > 0:
                s = pygame.Surface((BALL_R * 2, BALL_R * 2), pygame.SRCALPHA)
                pygame.draw.circle(s, (*CROQUETTE, alpha), (BALL_R, BALL_R), BALL_R - 2)
                screen.blit(s, (int(tx) - BALL_R + shake_x, int(ty) - BALL_R + shake_y))

        # Malik obstacle
        malik_rect = g["malik"].move(shake_x, shake_y)
        pygame.draw.rect(screen, MALIK, malik_rect, border_radius=10)
        pygame.draw.rect(screen, (180, 100, 60), malik_rect, 2, border_radius=10)
        malik_label = font_small.render("Malik", True, TEXT)
        screen.blit(malik_label, malik_label.get_rect(center=malik_rect.center))

        # Adversaire = aspirateur
        opp = g["opponent"].move(shake_x, shake_y)
        pygame.draw.rect(screen, OPPONENT, opp, border_radius=10)
        pygame.draw.rect(screen, (60, 90, 120), opp, 2, border_radius=10)
        opp_label = font_small.render("Aspirateur", True, (240, 245, 250))
        screen.blit(opp_label, opp_label.get_rect(center=(opp.centerx, opp.centery)))

        # Nahla
        player = g["player"].move(shake_x, shake_y)
        if g["player_glow"] > 0:
            glow = player.inflate(20, 14)
            glow_s = pygame.Surface(glow.size, pygame.SRCALPHA)
            alpha = min(180, g["player_glow"])
            pygame.draw.ellipse(glow_s, (*ACCENT, alpha), glow_s.get_rect())
            screen.blit(glow_s, glow.topleft)
        screen.blit(nahla_img, player)

        # Balle
        if g["serve_timer"] <= 0 or state != "play":
            bx, by = int(g["ball"]["x"]) + shake_x, int(g["ball"]["y"]) + shake_y
            if g["hit_flash"] > 0:
                pygame.draw.circle(screen, ACCENT, (bx, by), BALL_R + 6)
            pygame.draw.circle(screen, CROQUETTE_LIGHT, (bx, by), BALL_R)
            pygame.draw.circle(screen, CROQUETTE, (bx, by), BALL_R - 3)
            pygame.draw.circle(screen, (90, 60, 20), (bx, by), BALL_R, 2)

        # Particules
        for p in g["particles"]:
            alpha = min(255, int(255 * p["life"] / 450))
            s = pygame.Surface((p["r"] * 2, p["r"] * 2), pygame.SRCALPHA)
            pygame.draw.circle(s, (*p["color"], alpha), (p["r"], p["r"]), p["r"])
            screen.blit(s, (int(p["x"]) - p["r"] + shake_x, int(p["y"]) - p["r"] + shake_y))

        # HUD
        score_surf = font_big.render(f"{g['score_player']}  —  {g['score_opponent']}", True, TEXT)
        screen.blit(score_surf, score_surf.get_rect(center=(WIDTH // 2 + shake_x, 32)))

        rally_txt = font_small.render(f"Échanges : {g['rally']}", True, MUTED)
        screen.blit(rally_txt, (24 + shake_x, 24))

        target = font_small.render(f"Premier à {WIN_SCORE}", True, MUTED)
        screen.blit(target, (WIDTH - target.get_width() - 24 + shake_x, 24))

        diff_badge = font_small.render(difficulty["label"], True, difficulty["color"])
        screen.blit(diff_badge, (WIDTH // 2 - diff_badge.get_width() // 2 + shake_x, 58))

        if g["phrase_timer"] > 0:
            phrase_surf = font.render(g["phrase"], True, TEXT)
            screen.blit(phrase_surf, phrase_surf.get_rect(center=(WIDTH // 2 + shake_x, HEIGHT - 52)))

        if g["serve_timer"] > 0 and state == "play":
            countdown = font.render("...", True, MUTED)
            screen.blit(countdown, countdown.get_rect(center=(WIDTH // 2 + shake_x, HEIGHT // 2)))

        hint = font_small.render("Q/D · R = rejouer · M = menu · Échap", True, MUTED)
        screen.blit(hint, hint.get_rect(center=(WIDTH // 2 + shake_x, HEIGHT - 16)))

        # Overlays
        if state == "win":
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 120))
            screen.blit(overlay, (0, 0))
            t1 = font_big.render("Nahla gagne.", True, WIN_C)
            t2 = font.render("La croquette te respecte. (un peu)", True, ACCENT)
            t3 = font_small.render("R = rejouer · M = menu", True, (220, 220, 220))
            screen.blit(t1, t1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30)))
            screen.blit(t2, t2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20)))
            screen.blit(t3, t3.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 65)))
        elif state == "lose":
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 140))
            screen.blit(overlay, (0, 0))
            t1 = font_big.render("Nahla te méprise.", True, DANGER)
            t2 = font.render("L'aspirateur a gagné. Honte.", True, ACCENT)
            t3 = font_small.render("R = rejouer · M = menu", True, (220, 220, 220))
            screen.blit(t1, t1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30)))
            screen.blit(t2, t2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20)))
            screen.blit(t3, t3.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 65)))

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
