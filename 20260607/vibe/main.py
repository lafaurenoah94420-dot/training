"""Nahla cache-cache — reste invisible dans le salon."""

import json
import math
import random
import sys
from pathlib import Path

import pygame

WIDTH, HEIGHT = 1280, 800
FPS = 60
TITLE = "Nahla cache-cache"

PLAY_TOP = 88
PLAY_BOTTOM = HEIGHT - 48
PLAY_LEFT = 48
PLAY_RIGHT = WIDTH - 48

PLAYER_R = 28
PLAYER_HIT_R = 14
PLAYER_SPEED = 5.0
GUARD_SPEED = 2.6
KAYS_SPEED = 2.2
INVESTIGATE_SPEED = 3.4
KAYS_CHASE_SPEED = 2.8
CHASE_MEMORY_MS = 2800
TURN_SPEED = 0.14
CHASE_STOP_DIST = 24
VISION_RANGE = 240
KAYS_VISION_RANGE = 200
MAMAN_VISION_RANGE = 260
VISION_ANGLE = math.radians(70)
NEAR_ANGLE = math.radians(95)
MATCH_MS = 90000
STRESS_MAX = 100
STRESS_RATE = 0.35
STRESS_HEAL = 0.2
SPOT_GRACE_MS = 400
CROQUETTE_R = 14
CROQUETTE_SPAWN_MS = 9000
CROQUETTE_STRESS = 22
GHOST_MS = 2000
BARK_MS = 2200
NAHLA_BARK_EVERY = 12.0
NEAR_BARK_COOLDOWN_MS = 5000
PROVOKE_COOLDOWN_MS = 8000
PROVOKE_CHASE_MS = 5000
PROVOKE_FX_MS = 700

MENU = "menu"
PLAYING = "playing"
OVER = "over"

TEXT = (245, 238, 225)
ACCENT = (255, 168, 72)
FLOOR = (58, 50, 44)
FLOOR_LIGHT = (78, 68, 58)
WALL = (88, 76, 68)
CARPET = (92, 62, 52)
VISION_C = (255, 220, 80, 55)
KAYS_VISION_C = (120, 180, 255, 50)
SPOTTED_C = (255, 70, 70)
SAFE_C = (100, 220, 140)
GUARD_C = (255, 200, 140)
KAYS_C = (140, 190, 255)
MAMAN_C = (220, 150, 200)
MAMAN_VISION_C = (255, 160, 220, 48)
OBSTACLE_C = (100, 58, 72)
OBSTACLE_TOP = (120, 72, 88)
CROQUETTE_C = (210, 140, 60)

MOVE_LEFT = (pygame.K_LEFT, pygame.K_q, pygame.K_a)
MOVE_RIGHT = (pygame.K_RIGHT, pygame.K_d)
MOVE_UP = (pygame.K_UP, pygame.K_z, pygame.K_w)
MOVE_DOWN = (pygame.K_DOWN, pygame.K_s)

OBSTACLES = [
    pygame.Rect(160, 200, 200, 90),
    pygame.Rect(500, 170, 120, 180),
    pygame.Rect(820, 260, 240, 70),
    pygame.Rect(265, 490, 185, 65),
    pygame.Rect(665, 465, 145, 115),
    pygame.Rect(960, 520, 200, 60),
    pygame.Rect(400, 580, 180, 55),
    pygame.Rect(100, 420, 110, 130),
    pygame.Rect(1050, 380, 130, 100),
]

# Malik = gauche · Maman = centre · Kays = droite
MALIK_PATROL = [
    (100, 160), (420, 160), (100, 380), (420, 380),
    (100, 620), (320, 640), (100, 720), (420, 720),
]
MAMAN_PATROL = [
    (480, 140), (740, 140), (540, 400), (740, 400),
    (640, 560), (540, 700), (740, 700), (640, 300),
]
KAYS_PATROL = [
    (860, 160), (1150, 160), (900, 240), (1150, 300),
    (860, 620), (1150, 620), (860, 720), (1150, 720),
]
PATROL_ARRIVE = 10

ASSETS = Path(__file__).parent
NAHLA_HEAD = ASSETS / "nahla_head.png"
NAHLA_PHOTO = ASSETS / "WhatsApp Image 2026-04-24 at 00.18.56.jpeg"
HIGHSCORE_FILE = ASSETS / "hide_record.json"
CROP = (0.24, 0.12, 0.52, 0.40)

NAHLA_LINES = [
    "Ils me voient pas.",
    "Cachette parfaite.",
    "Mode fantôme.",
    "Les humains sont lents.",
    "Sieste en cours...",
]
MALIK_LINES = [
    "Nahla ?",
    "Je l'ai vue là...",
    "Elle est où ?",
]
MALIK_SPOT_LINES = [
    "Ah ! Là !",
    "Attrape-la !",
]
KAYS_LINES = [
    "T'as vu Nahla ?",
    "Elle gratte le canapé ?",
    "Hmm...",
]
KAYS_SPOT_LINES = [
    "Hé Malik !",
    "Là-bas !",
]
MAMAN_LINES = [
    "Nahla ! Descends !",
    "Je sais que tu es là.",
    "Pas de griffades...",
]
MAMAN_SPOT_LINES = [
    "Je t'ai vue !",
    "Attrapez-la !",
]
CROQUETTE_LINES = [
    "Croquette volée.",
    "Miam miam.",
    "Bonus.",
]
PROVOKE_LINES = [
    "MIAOUUU !",
    "Prrrrrt !",
    "Meow !",
]


def load_nahla(size):
    if NAHLA_HEAD.exists():
        img = pygame.image.load(str(NAHLA_HEAD)).convert_alpha()
    elif NAHLA_PHOTO.exists():
        full = pygame.image.load(str(NAHLA_PHOTO)).convert()
        w, h = full.get_size()
        cx, cy, cw, ch = CROP
        rect = pygame.Rect(int(w * cx), int(h * cy), int(w * cw), int(h * ch))
        img = full.subsurface(rect).copy()
    else:
        surf = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.ellipse(surf, ACCENT, surf.get_rect())
        return surf
    return pygame.transform.smoothscale(img, (size, size))


def load_record():
    if HIGHSCORE_FILE.exists():
        try:
            return json.loads(HIGHSCORE_FILE.read_text()).get("best_hidden", 0)
        except (json.JSONDecodeError, OSError):
            pass
    return 0.0


def save_record(seconds):
    try:
        HIGHSCORE_FILE.write_text(json.dumps({"best_hidden": round(seconds, 1)}))
    except OSError:
        pass


def key_down(keys, codes):
    return any(keys[k] for k in codes)


def dist(ax, ay, bx, by):
    return math.hypot(ax - bx, ay - by)


def normalize(dx, dy):
    mag = math.hypot(dx, dy) or 1
    return dx / mag, dy / mag


def circle_hits_rect(cx, cy, radius, rect):
    nx = max(rect.left, min(cx, rect.right))
    ny = max(rect.top, min(cy, rect.bottom))
    return dist(cx, cy, nx, ny) < radius


def player_blocked(x, y):
    for obs in OBSTACLES:
        if circle_hits_rect(x, y, PLAYER_HIT_R, obs):
            return True
    return (
        x < PLAY_LEFT + PLAYER_HIT_R
        or x > PLAY_RIGHT - PLAYER_HIT_R
        or y < PLAY_TOP + PLAYER_HIT_R
        or y > PLAY_BOTTOM - PLAYER_HIT_R
    )


def spawn_point_clear(x, y):
    if x < PLAY_LEFT + 30 or x > PLAY_RIGHT - 30 or y < PLAY_TOP + 30 or y > PLAY_BOTTOM - 30:
        return False
    for obs in OBSTACLES:
        if obs.inflate(24, 24).collidepoint(x, y):
            return False
    return True


def random_croquette_pos():
    for _ in range(40):
        x = random.randint(PLAY_LEFT + 40, PLAY_RIGHT - 40)
        y = random.randint(PLAY_TOP + 40, PLAY_BOTTOM - 40)
        if spawn_point_clear(x, y):
            return x, y
    return 640, 500


GUARD_BARKS = {
    "malik": (MALIK_LINES, MALIK_SPOT_LINES),
    "kays": (KAYS_LINES, KAYS_SPOT_LINES),
    "maman": (MAMAN_LINES, MAMAN_SPOT_LINES),
}


def make_guard(gid, label, color, vision_color, patrol, speed, chase_speed, vision_range):
    return {
        "id": gid,
        "label": label,
        "color": color,
        "vision_color": vision_color,
        "x": patrol[0][0],
        "y": patrol[0][1],
        "patrol_points": patrol,
        "patrol_idx": 1,
        "angle": 0.0,
        "mode": "patrol",
        "last_seen": None,
        "last_seen_at": 0,
        "vision_range": vision_range,
        "speed": speed,
        "chase_speed": chase_speed,
        "near_bark_until": 0,
    }


def make_malik():
    return make_guard(
        "malik", "MALIK", GUARD_C, VISION_C,
        MALIK_PATROL, GUARD_SPEED, INVESTIGATE_SPEED, VISION_RANGE,
    )


def make_maman():
    return make_guard(
        "maman", "MAMAN", MAMAN_C, MAMAN_VISION_C,
        MAMAN_PATROL, 2.0, 2.6, MAMAN_VISION_RANGE,
    )


def make_kays():
    return make_guard(
        "kays", "KAYS", KAYS_C, KAYS_VISION_C,
        KAYS_PATROL, KAYS_SPEED, KAYS_CHASE_SPEED, KAYS_VISION_RANGE,
    )


def line_intersects_rect(x1, y1, x2, y2, rect):
    steps = int(dist(x1, y1, x2, y2) // 8) + 1
    for i in range(steps + 1):
        t = i / max(steps, 1)
        px = x1 + (x2 - x1) * t
        py = y1 + (y2 - y1) * t
        if rect.collidepoint(px, py):
            return True
    return False


def has_line_of_sight(gx, gy, px, py):
    for obs in OBSTACLES:
        if line_intersects_rect(gx, gy, px, py, obs):
            return False
    return True


def in_vision_cone(guard, px, py):
    gx, gy = guard["x"], guard["y"]
    vrange = guard.get("vision_range", VISION_RANGE)
    d = dist(gx, gy, px, py)
    if d > vrange or d < 8:
        return False
    angle_to_player = math.atan2(py - gy, px - gx)
    diff = abs((angle_to_player - guard["angle"] + math.pi) % (2 * math.pi) - math.pi)
    if diff > VISION_ANGLE:
        return False
    return has_line_of_sight(gx, gy, px, py)


def near_vision(guard, px, py):
    """Dans le cône élargi mais pas vraiment vue (bloquée ou limite)."""
    gx, gy = guard["x"], guard["y"]
    vrange = guard.get("vision_range", VISION_RANGE)
    d = dist(gx, gy, px, py)
    if d > vrange * 1.05 or d < 20:
        return False
    angle_to_player = math.atan2(py - gy, px - gx)
    diff = abs((angle_to_player - guard["angle"] + math.pi) % (2 * math.pi) - math.pi)
    return diff <= NEAR_ANGLE and not in_vision_cone(guard, px, py)


def reset_match():
    now = pygame.time.get_ticks()
    return {
        "player": {"x": WIDTH // 2, "y": PLAY_BOTTOM - 80, "sprite": load_nahla(56)},
        "guards": [make_malik(), make_maman(), make_kays()],
        "hidden_time": 0.0,
        "stress": 0.0,
        "spotted": False,
        "spot_since": 0,
        "seen_raw": False,
        "match_start": now,
        "match_end": now + MATCH_MS,
        "bark": "",
        "bark_until": 0,
        "bark_color": ACCENT,
        "last_nahla_bark": 0.0,
        "croquette": None,
        "next_croquette": now + 4000,
        "ghost_until": 0,
        "provoke_ready": 0,
        "provoke_fx_until": 0,
    }


def nearest_patrol_idx(guard):
    best_i, best_d = 0, float("inf")
    for i, (px, py) in enumerate(guard["patrol_points"]):
        d = dist(guard["x"], guard["y"], px, py)
        if d < best_d:
            best_d, best_i = d, i
    return best_i


def turn_toward(guard, target_angle):
    diff = (target_angle - guard["angle"] + math.pi) % (2 * math.pi) - math.pi
    if abs(diff) <= TURN_SPEED:
        guard["angle"] = target_angle
    elif diff > 0:
        guard["angle"] += TURN_SPEED
    else:
        guard["angle"] -= TURN_SPEED


def move_guard_toward(guard, tx, ty, speed):
    dx, dy = tx - guard["x"], ty - guard["y"]
    d = math.hypot(dx, dy)
    if d <= PATROL_ARRIVE:
        guard["x"], guard["y"] = tx, ty
        if d > 0.5:
            turn_toward(guard, math.atan2(dy, dx))
        return True
    nx, ny = normalize(dx, dy)
    guard["x"] += nx * speed
    guard["y"] += ny * speed
    turn_toward(guard, math.atan2(ny, nx))
    return False


def chase_toward(guard, tx, ty, speed):
    """Poursuite sans snap ni retour patrouille — rotation progressive."""
    dx, dy = tx - guard["x"], ty - guard["y"]
    d = math.hypot(dx, dy)
    target_angle = math.atan2(dy, dx) if d > 0.5 else guard["angle"]
    turn_toward(guard, target_angle)
    if d <= CHASE_STOP_DIST:
        return
    nx, ny = normalize(dx, dy)
    guard["x"] += nx * speed
    guard["y"] += ny * speed


def update_patrol(guard):
    tx, ty = guard["patrol_points"][guard["patrol_idx"]]
    if move_guard_toward(guard, tx, ty, guard["speed"]):
        guard["patrol_idx"] = (guard["patrol_idx"] + 1) % len(guard["patrol_points"])


def update_guard_ai(guard, px, py, seen, now):
    if seen:
        guard["last_seen"] = (px, py)
        guard["last_seen_at"] = now
        guard["mode"] = "chase"

    if guard["mode"] == "chase" and guard["last_seen"]:
        provoked = now < guard.get("provoked_until", 0)
        still_chasing = seen or provoked or (now - guard["last_seen_at"] < CHASE_MEMORY_MS)
        if still_chasing:
            chase_toward(guard, guard["last_seen"][0], guard["last_seen"][1], guard["chase_speed"])
            return
        guard["mode"] = "patrol"

    update_patrol(guard)


def show_bark(game, text, color, now):
    game["bark"] = text
    game["bark_until"] = now + BARK_MS
    game["bark_color"] = color


def provoke_guards(game, px, py, now):
    if now < game["provoke_ready"]:
        return False
    game["provoke_ready"] = now + PROVOKE_COOLDOWN_MS
    game["provoke_fx_until"] = now + PROVOKE_FX_MS
    for guard in game["guards"]:
        guard["last_seen"] = (px, py)
        guard["last_seen_at"] = now
        guard["provoked_until"] = now + PROVOKE_CHASE_MS
        guard["mode"] = "chase"
    show_bark(game, random.choice(PROVOKE_LINES), ACCENT, now)
    return True


def spawn_croquette(game, now):
    x, y = random_croquette_pos()
    game["croquette"] = {"x": x, "y": y}
    game["next_croquette"] = now + CROQUETTE_SPAWN_MS


def draw_room(surf):
    surf.fill(WALL)
    floor = pygame.Rect(PLAY_LEFT, PLAY_TOP, PLAY_RIGHT - PLAY_LEFT, PLAY_BOTTOM - PLAY_TOP)
    pygame.draw.rect(surf, FLOOR, floor, border_radius=8)
    pygame.draw.rect(surf, FLOOR_LIGHT, floor, 3, border_radius=8)
    carpet = pygame.Rect(PLAY_LEFT + 20, PLAY_TOP + 20, PLAY_RIGHT - PLAY_LEFT - 40, PLAY_BOTTOM - PLAY_TOP - 40)
    pygame.draw.rect(surf, CARPET, carpet, border_radius=6)
    for obs in OBSTACLES:
        pygame.draw.rect(surf, OBSTACLE_C, obs, border_radius=8)
        top = pygame.Rect(obs.x + 6, obs.y - 12, obs.w - 12, 14)
        pygame.draw.rect(surf, OBSTACLE_TOP, top, border_radius=6)


def draw_vision(surf, guard, spotted):
    gx, gy = int(guard["x"]), int(guard["y"])
    angle = guard["angle"]
    vrange = guard.get("vision_range", VISION_RANGE)
    left = angle - VISION_ANGLE
    right = angle + VISION_ANGLE
    p1 = (gx, gy)
    p2 = (gx + math.cos(left) * vrange, gy + math.sin(left) * vrange)
    p3 = (gx + math.cos(right) * vrange, gy + math.sin(right) * vrange)
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    if spotted:
        col = (255, 90, 90, 70)
    else:
        col = guard.get("vision_color", VISION_C)
    pygame.draw.polygon(overlay, col, [p1, p2, p3])
    surf.blit(overlay, (0, 0))


def draw_guard(surf, guard, font):
    x, y = int(guard["x"]), int(guard["y"])
    col = guard["color"]
    pygame.draw.line(surf, col, (x - 16, y + 18), (x - 6, y - 16), 4)
    pygame.draw.line(surf, col, (x + 16, y + 18), (x + 6, y - 16), 4)
    pygame.draw.circle(surf, col, (x, y - 18), 11)
    if guard["mode"] == "chase":
        pygame.draw.circle(surf, (255, 120, 80), (x, y - 18), 14, 2)
    lbl = font.render(guard["label"], True, col)
    surf.blit(lbl, (x - lbl.get_width() // 2, y - 42))


def draw_player(surf, player, spotted, ghost):
    x, y = int(player["x"]), int(player["y"])
    if ghost:
        pygame.draw.circle(surf, (180, 220, 255), (x, y), PLAYER_R + 5, 2)
    elif spotted:
        pygame.draw.circle(surf, SPOTTED_C, (x, y), PLAYER_R + 6, 3)
    else:
        pygame.draw.circle(surf, SAFE_C, (x, y), PLAYER_R + 4, 2)
    sprite = player["sprite"].copy()
    if ghost:
        sprite.set_alpha(140)
    surf.blit(sprite, (x - 28, y - 28))


def draw_croquette(surf, croq):
    x, y = int(croq["x"]), int(croq["y"])
    pygame.draw.circle(surf, CROQUETTE_C, (x, y), CROQUETTE_R)
    pygame.draw.circle(surf, (240, 200, 120), (x - 3, y - 3), 4)


def draw_hud(surf, font, small, game, now, record):
    pygame.draw.rect(surf, (18, 16, 24), (0, 0, WIDTH, PLAY_TOP - 4))
    time_left = max(0, (game["match_end"] - now) // 1000)
    surf.blit(font.render(f"Cachée : {game['hidden_time']:.1f}s", True, SAFE_C), (16, 18))
    surf.blit(font.render(f"Record : {record:.1f}s", True, TEXT), (260, 18))
    surf.blit(font.render(f"Temps : {time_left}s", True, TEXT), (WIDTH - 150, 18))
    ghost = now < game["ghost_until"]
    status = "FANTÔME" if ghost else ("VU !!!" if game["spotted"] else "Invisible")
    col = (180, 220, 255) if ghost else (SPOTTED_C if game["spotted"] else SAFE_C)
    surf.blit(font.render(status, True, col), (WIDTH // 2 - 60, 18))
    bar_x, bar_y, bar_w = 16, 52, 220
    pygame.draw.rect(surf, (50, 30, 35), (bar_x, bar_y, bar_w, 14), border_radius=4)
    fill = int(bar_w * game["stress"] / STRESS_MAX)
    pygame.draw.rect(surf, SPOTTED_C, (bar_x, bar_y, fill, 14), border_radius=4)
    surf.blit(small.render("Stress", True, TEXT), (bar_x + bar_w + 8, 50))
    provoke_left = max(0, (game["provoke_ready"] - now) // 1000)
    if provoke_left:
        prov_txt = small.render(f"F provoquer ({provoke_left}s)", True, (120, 120, 130))
    else:
        prov_txt = small.render("F — provoquer", True, ACCENT)
    surf.blit(prov_txt, (WIDTH - prov_txt.get_width() - 16, 50))
    if now < game["bark_until"]:
        t = font.render(game["bark"], True, game["bark_color"])
        surf.blit(t, (WIDTH // 2 - t.get_width() // 2, 72))


def draw_provoke_fx(surf, game, now):
    if now >= game["provoke_fx_until"]:
        return
    p = game["player"]
    x, y = int(p["x"]), int(p["y"])
    elapsed = game["provoke_fx_until"] - now
    t = 1 - elapsed / PROVOKE_FX_MS
    radius = int(25 + t * 100)
    alpha = max(0, int(200 * (1 - t)))
    ring = pygame.Surface((radius * 2 + 4, radius * 2 + 4), pygame.SRCALPHA)
    pygame.draw.circle(ring, (255, 180, 80, alpha), (radius + 2, radius + 2), radius, 4)
    surf.blit(ring, (x - radius - 2, y - radius - 2))


def draw_overlay(surf, big, small, title, lines):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((8, 6, 14, 175))
    surf.blit(overlay, (0, 0))
    t = big.render(title, True, TEXT)
    surf.blit(t, (WIDTH // 2 - t.get_width() // 2, HEIGHT // 2 - 110))
    for i, line in enumerate(lines):
        s = small.render(line, True, TEXT)
        surf.blit(s, (WIDTH // 2 - s.get_width() // 2, HEIGHT // 2 - 40 + i * 30))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("menlo,consolas,monospace", 22)
    small = pygame.font.SysFont("menlo,consolas,monospace", 16)
    big = pygame.font.SysFont("menlo,consolas,monospace", 44, bold=True)

    record = load_record()
    state = MENU
    game = None

    running = True
    while running:
        now = pygame.time.get_ticks()
        dt = clock.tick(FPS) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if state in (MENU, OVER) and event.key in (pygame.K_RETURN, pygame.K_SPACE, pygame.K_r):
                    state = PLAYING
                    game = reset_match()
                if state == PLAYING and event.key == pygame.K_f and game:
                    provoke_guards(game, game["player"]["x"], game["player"]["y"], now)

        keys = pygame.key.get_pressed()
        if state == MENU and (keys[pygame.K_RETURN] or keys[pygame.K_SPACE]):
            state = PLAYING
            game = reset_match()

        if state == PLAYING:
            p = game["player"]
            ghost = now < game["ghost_until"]

            dx = dy = 0
            if key_down(keys, MOVE_LEFT):
                dx -= 1
            if key_down(keys, MOVE_RIGHT):
                dx += 1
            if key_down(keys, MOVE_UP):
                dy -= 1
            if key_down(keys, MOVE_DOWN):
                dy += 1
            if dx or dy:
                nx, ny = normalize(dx, dy)
                nx_pos = p["x"] + nx * PLAYER_SPEED
                ny_pos = p["y"] + ny * PLAYER_SPEED
                if not player_blocked(nx_pos, p["y"]):
                    p["x"] = nx_pos
                if not player_blocked(p["x"], ny_pos):
                    p["y"] = ny_pos

            for guard in game["guards"]:
                seen = False if ghost else in_vision_cone(guard, p["x"], p["y"])
                update_guard_ai(guard, p["x"], p["y"], seen, now)

            seen_raw = False
            if not ghost:
                for guard in game["guards"]:
                    if in_vision_cone(guard, p["x"], p["y"]):
                        seen_raw = True
                        if not game["spotted"] and now >= game.get("last_spot_bark", 0):
                            near_lines, spot_lines = GUARD_BARKS[guard["id"]]
                            show_bark(game, random.choice(spot_lines), guard["color"], now)
                            game["last_spot_bark"] = now + 3000
                        break

            game["seen_raw"] = seen_raw
            if seen_raw:
                if game["spot_since"] == 0:
                    game["spot_since"] = now
                elif now - game["spot_since"] > SPOT_GRACE_MS:
                    game["spotted"] = True
            else:
                game["spotted"] = False
                game["spot_since"] = 0

            if not ghost:
                for guard in game["guards"]:
                    if near_vision(guard, p["x"], p["y"]) and now > guard["near_bark_until"]:
                        near_lines, _ = GUARD_BARKS[guard["id"]]
                        show_bark(game, random.choice(near_lines), guard["color"], now)
                        guard["near_bark_until"] = now + NEAR_BARK_COOLDOWN_MS
                        break

            if game["spotted"]:
                game["stress"] = min(STRESS_MAX, game["stress"] + STRESS_RATE * dt * 60)
            else:
                game["hidden_time"] += dt
                game["stress"] = max(0, game["stress"] - STRESS_HEAL * dt * 60)
                if game["hidden_time"] - game["last_nahla_bark"] >= NAHLA_BARK_EVERY:
                    show_bark(game, random.choice(NAHLA_LINES), ACCENT, now)
                    game["last_nahla_bark"] = game["hidden_time"]

            if game["croquette"] is None and now >= game["next_croquette"]:
                spawn_croquette(game, now)
            elif game["croquette"]:
                c = game["croquette"]
                if dist(p["x"], p["y"], c["x"], c["y"]) < PLAYER_R + CROQUETTE_R:
                    game["stress"] = max(0, game["stress"] - CROQUETTE_STRESS)
                    game["ghost_until"] = now + GHOST_MS
                    game["croquette"] = None
                    game["next_croquette"] = now + CROQUETTE_SPAWN_MS
                    show_bark(game, random.choice(CROQUETTE_LINES), ACCENT, now)

            if game["stress"] >= STRESS_MAX:
                state = OVER
                if game["hidden_time"] > record:
                    record = game["hidden_time"]
                    save_record(record)
            elif now >= game["match_end"]:
                state = OVER
                if game["hidden_time"] > record:
                    record = game["hidden_time"]
                    save_record(record)

        draw_room(screen)
        if state == PLAYING:
            for guard in game["guards"]:
                draw_vision(screen, guard, game["spotted"] and not now < game["ghost_until"])
            for guard in game["guards"]:
                draw_guard(screen, guard, small)
            if game["croquette"]:
                draw_croquette(screen, game["croquette"])
            draw_player(screen, game["player"], game["spotted"], now < game["ghost_until"])
            draw_provoke_fx(screen, game, now)
            draw_hud(screen, font, small, game, now, record)

        if state == MENU:
            draw_overlay(
                screen, big, small, "Nahla cache-cache",
                [
                    "Évite Malik, Maman et Kays — cache-toi derrière les meubles",
                    "Malik enquête là où il t'a vue",
                    "Croquettes = stress - + mode fantôme",
                    "F — miauler pour provoquer les humains",
                    "ZQSD / flèches — bouger",
                    "Entrée ou Espace — jouer",
                ],
            )
        elif state == OVER:
            won = game["stress"] < STRESS_MAX
            title = "Sieste méritée !" if won else "Repérée..."
            draw_overlay(
                screen, big, small, title,
                [
                    f"Temps cachée : {game['hidden_time']:.1f}s",
                    f"Record : {record:.1f}s",
                    "R ou Entrée — rejouer",
                ],
            )

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
