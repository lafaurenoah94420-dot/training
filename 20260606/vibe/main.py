"""Nahla vs le laser — chase & combo dans le salon (version complète)."""

import array
import json
import math
import random
import sys
from pathlib import Path

import pygame

WIDTH, HEIGHT = 960, 640
FPS = 60
TITLE = "Nahla vs le laser"

PLAY_TOP = 88
PLAY_BOTTOM = HEIGHT - 48
PLAY_LEFT = 48
PLAY_RIGHT = WIDTH - 48

PLAYER_BASE = 72
PLAYER_SPEED = 6.2
DASH_SPEED = 17
DASH_MS = 160
DASH_COOLDOWN_MS = 900
LASER_R = 14
COMBO_DECAY_MS = 450
MATCH_MS = 90000
LASER_BASE_SPEED = 5.5
LASER_MAX_SPEED = 11
SECOND_LASER_AT_MS = 30000
PURR_FREEZE_MS = 1000
PURR_COOLDOWN_MS = 6000
MALIK_INTERVAL_MS = 18000
COUCH_BONUS_SCORE = 3
TAUNT_EVERY = 8
CROQUETTE_R = 14
CROQUETTE_SPAWN_MS = 8000
CROQUETTE_SCORE = 30
CROQUETTE_DASH_REDUCE_MS = 600
SPLIT_COMBO_MIN = 30
SPLIT_HOLD_FRAMES = 70
BOSS_LAST_MS = 10000
BOSS_R = 38
BONUS_DURATION_MS = 5000
MINI_LASER_R = 9

BONUS_ZONES = [
    {"cx": 380, "cy": 360, "r": 48},
    {"cx": 620, "cy": 430, "r": 42},
    {"cx": 520, "cy": 280, "r": 38},
]

MENU = "menu"
PLAYING = "playing"
OVER = "over"

MODE_CHRONO = "chrono"
MODE_INFINI = "infini"

DIFF_NORMAL = "normal"
DIFF_HARD = "difficile"

DIFF_MULT = {
    DIFF_NORMAL: {"speed": 1.0, "spawn": 1.0},
    DIFF_HARD: {"speed": 1.35, "max": 1.2},
}

TEXT = (245, 238, 225)
ACCENT = (255, 150, 60)
LASER = (255, 40, 55)
LASER2 = (255, 100, 40)
LASER_GLOW = (255, 120, 130)
FLOOR = (62, 54, 46)
FLOOR_LIGHT = (78, 68, 58)
CARPET = (92, 62, 52)
WALL = (88, 76, 68)
SCRATCH = (120, 100, 85)
WIN_C = (100, 220, 140)
COUCH_COLOR = (120, 72, 88)
MALIK_COLOR = (255, 200, 140)
CROQUETTE_C = (255, 190, 60)
BONUS_ZONE_C = (255, 215, 80)
BOSS_C = (180, 50, 255)

COUCH_RECT = pygame.Rect(PLAY_LEFT + 30, PLAY_TOP + 40, 140, 50)

MOVE_LEFT = (pygame.K_LEFT, pygame.K_q, pygame.K_a)
MOVE_RIGHT = (pygame.K_RIGHT, pygame.K_d)
MOVE_UP = (pygame.K_UP, pygame.K_z, pygame.K_w)
MOVE_DOWN = (pygame.K_DOWN, pygame.K_s)

NAHLA_LINES = [
    "C'est MOI la chasseuse.",
    "Laser = ma proie.",
    "Griffe. Griffe. Griffe.",
    "Humains jaloux.",
    "Combo royal.",
    "Miaou de victoire.",
    "Le canapé c'est la vie.",
    "Malik dégage.",
]

ASSETS = Path(__file__).parent
NAHLA_HEAD = ASSETS / "nahla_head.png"
NAHLA_PHOTO = ASSETS / "WhatsApp Image 2026-04-24 at 00.18.56.jpeg"
HIGHSCORE_FILE = ASSETS / "highscore.json"
CROP = (0.24, 0.12, 0.52, 0.40)


def load_nahla_sprite(size):
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


def make_beep(freq, duration=0.08, volume=0.25):
    rate = 22050
    n = int(rate * duration)
    buf = array.array("h")
    amp = int(32767 * volume)
    for i in range(n):
        t = i / rate
        buf.append(int(amp * math.sin(2 * math.pi * freq * t)))
    return pygame.mixer.Sound(buffer=buf)


def load_sounds():
    try:
        pygame.mixer.init(frequency=22050, size=-16, channels=1, buffer=512)
        return {
            "scratch": make_beep(180, 0.05, 0.2),
            "combo": make_beep(440 + random.randint(0, 80), 0.06, 0.22),
            "meow": make_beep(320, 0.12, 0.28),
            "purr": make_beep(140, 0.2, 0.3),
            "malik": make_beep(90, 0.15, 0.35),
            "pickup": make_beep(520, 0.1, 0.3),
            "boss": make_beep(70, 0.25, 0.4),
        }
    except pygame.error:
        return {}


def load_highscore():
    if HIGHSCORE_FILE.exists():
        try:
            return json.loads(HIGHSCORE_FILE.read_text()).get("best", 0)
        except (json.JSONDecodeError, OSError):
            pass
    return 0


def save_highscore(score):
    try:
        HIGHSCORE_FILE.write_text(json.dumps({"best": score}))
    except OSError:
        pass


def key_down(keys, codes):
    return any(keys[k] for k in codes)


def clamp(val, lo, hi):
    return max(lo, min(hi, val))


def dist(ax, ay, bx, by):
    return math.hypot(ax - bx, ay - by)


def player_size(combo):
    if combo >= 40:
        return PLAYER_BASE + 45
    if combo >= 25:
        return PLAYER_BASE + 30
    if combo >= 10:
        return PLAYER_BASE + 15
    return PLAYER_BASE


def grade_for_score(score):
    if score >= 5000:
        return "Reine du salon"
    if score >= 2000:
        return "Prédatrice"
    if score >= 500:
        return "Chasseuse"
    return "Chaton"


def laser_radius(laser):
    return laser.get("radius", LASER_R)


def new_laser(speed_mult=1.0, radius=LASER_R, color=LASER, is_boss=False, is_mini=False):
    x = random.randint(PLAY_LEFT + 60, PLAY_RIGHT - 60)
    y = random.randint(PLAY_TOP + 60, PLAY_BOTTOM - 60)
    angle = random.uniform(0, math.tau)
    speed = LASER_BASE_SPEED * speed_mult
    return {
        "x": x,
        "y": y,
        "vx": math.cos(angle) * speed,
        "vy": math.sin(angle) * speed,
        "speed": speed,
        "trail": [],
        "color": color,
        "radius": radius,
        "is_boss": is_boss,
        "is_mini": is_mini,
        "splitted": False,
        "hold_frames": 0,
    }


def spawn_boss_laser(diff):
    laser = new_laser(DIFF_MULT[diff]["speed"] * 0.9, BOSS_R, BOSS_C, is_boss=True)
    laser["x"] = (PLAY_LEFT + PLAY_RIGHT) // 2
    laser["y"] = (PLAY_TOP + PLAY_BOTTOM) // 2
    laser["speed"] = LASER_BASE_SPEED * 1.1
    return laser


def spawn_croquette():
    return {
        "x": random.randint(PLAY_LEFT + 80, PLAY_RIGHT - 80),
        "y": random.randint(PLAY_TOP + 80, PLAY_BOTTOM - 80),
    }


def split_laser(game, laser, diff):
    if laser.get("splitted") or laser.get("is_boss") or laser.get("is_mini"):
        return
    laser["splitted"] = True
    ox, oy = laser["x"], laser["y"]
    if laser in game["lasers"]:
        game["lasers"].remove(laser)
    for dx, dy in [(-28, -18), (28, 18)]:
        mini = new_laser(DIFF_MULT[diff]["speed"] * 1.2, MINI_LASER_R, (255, 160, 90), is_mini=True)
        mini["x"] = ox + dx
        mini["y"] = oy + dy
        mini["splitted"] = True
        game["lasers"].append(mini)
    game["taunt"] = "SPLIT !!!"
    game["taunt_until"] = pygame.time.get_ticks() + 1500


def score_mult(game, now):
    if now < game.get("bonus_mult_until", 0):
        return 2
    return 1


def reset_match(mode, difficulty):
    mult = DIFF_MULT[difficulty]
    laser = new_laser(mult["speed"])
    laser2 = None
    now = pygame.time.get_ticks()
    match_end = now + MATCH_MS if mode == MODE_CHRONO else None
    return {
        "player": {
            "x": (PLAY_LEFT + PLAY_RIGHT) // 2,
            "y": (PLAY_BOTTOM + PLAY_TOP) // 2,
            "facing": 1,
            "last_dx": 1,
            "last_dy": 0,
        },
        "lasers": [laser],
        "laser2_spawned": False,
        "score": 0,
        "combo": 0,
        "best_combo": 0,
        "last_catch_ms": 0,
        "match_start": now,
        "match_end": match_end,
        "mode": mode,
        "difficulty": difficulty,
        "scratches": [],
        "taunt": "",
        "taunt_until": 0,
        "sprite": load_nahla_sprite(PLAYER_BASE),
        "dash_until": 0,
        "dash_dx": None,
        "dash_dy": None,
        "dash_cooldown_until": 0,
        "freeze_until": 0,
        "purr_cooldown_until": 0,
        "malik": None,
        "malik_next": now + MALIK_INTERVAL_MS,
        "on_couch": False,
        "grade": "",
        "croquettes": [],
        "croquette_next": now + CROQUETTE_SPAWN_MS,
        "bonus_mult_until": 0,
        "boss_phase": False,
        "in_bonus_zone": False,
    }


def update_laser(laser, elapsed_s, frozen, diff):
    if frozen:
        return
    mult = DIFF_MULT[diff]
    max_spd = LASER_MAX_SPEED * mult.get("max", 1.0)
    target = min(max_spd, laser["speed"] + elapsed_s * 0.02)
    laser["speed"] = target
    mag = math.hypot(laser["vx"], laser["vy"]) or 1
    laser["vx"] = laser["vx"] / mag * target
    laser["vy"] = laser["vy"] / mag * target
    laser["x"] += laser["vx"]
    laser["y"] += laser["vy"]
    laser["trail"].append((laser["x"], laser["y"]))
    if len(laser["trail"]) > 18:
        laser["trail"].pop(0)
    r = laser_radius(laser)
    if laser["x"] <= PLAY_LEFT + r:
        laser["x"] = PLAY_LEFT + r
        laser["vx"] = abs(laser["vx"])
    if laser["x"] >= PLAY_RIGHT - r:
        laser["x"] = PLAY_RIGHT - r
        laser["vx"] = -abs(laser["vx"])
    if laser["y"] <= PLAY_TOP + r:
        laser["y"] = PLAY_TOP + r
        laser["vy"] = abs(laser["vy"])
    if laser["y"] >= PLAY_BOTTOM - r:
        laser["y"] = PLAY_BOTTOM - r
        laser["vy"] = -abs(laser["vy"])


def flee_laser(laser, px, py):
    angle = math.atan2(laser["y"] - py, laser["x"] - px)
    laser["vx"] = math.cos(angle) * laser["speed"]
    laser["vy"] = math.sin(angle) * laser["speed"]


def add_scratch(scratches, x, y):
    scratches.append({"x": x, "y": y, "born": pygame.time.get_ticks()})
    if len(scratches) > 100:
        scratches.pop(0)


def spawn_malik(now):
    y = random.randint(PLAY_TOP + 50, PLAY_BOTTOM - 50)
    side = random.choice(["left", "right"])
    if side == "left":
        return {"x": PLAY_LEFT - 40, "y": y, "vx": 5.5, "until": now + 4000}
    return {"x": PLAY_RIGHT + 40, "y": y, "vx": -5.5, "until": now + 4000}


def on_couch(px, py):
    return COUCH_RECT.collidepoint(int(px), int(py))


def draw_room(surf):
    surf.fill(WALL)
    floor = pygame.Rect(PLAY_LEFT, PLAY_TOP, PLAY_RIGHT - PLAY_LEFT, PLAY_BOTTOM - PLAY_TOP)
    pygame.draw.rect(surf, FLOOR, floor, border_radius=8)
    pygame.draw.rect(surf, FLOOR_LIGHT, floor, 3, border_radius=8)
    carpet = pygame.Rect(PLAY_LEFT + 24, PLAY_TOP + 24, PLAY_RIGHT - PLAY_LEFT - 48, PLAY_BOTTOM - PLAY_TOP - 48)
    pygame.draw.rect(surf, CARPET, carpet, border_radius=6)
    pygame.draw.rect(surf, (100, 58, 72), COUCH_RECT, border_radius=10)
    pygame.draw.rect(surf, COUCH_COLOR, (COUCH_RECT.x + 8, COUCH_RECT.y - 14, COUCH_RECT.w - 16, 18), border_radius=8)
    pygame.draw.rect(surf, (90, 66, 46), (PLAY_RIGHT - 170, PLAY_BOTTOM - 90, 120, 18), border_radius=4)
    # label canapé refuge
    font = pygame.font.SysFont("menlo,consolas,monospace", 14)
    lbl = font.render("refuge", True, (200, 180, 190))
    surf.blit(lbl, (COUCH_RECT.centerx - lbl.get_width() // 2, COUCH_RECT.y + 16))


def draw_bonus_zones(surf, pulse, active):
    for zone in BONUS_ZONES:
        cx, cy, r = zone["cx"], zone["cy"], zone["r"]
        glow = int(4 * math.sin(pulse))
        col = BONUS_ZONE_C if active else (90, 75, 50)
        pygame.draw.circle(surf, col, (cx, cy), r + glow, 2)
        if active:
            pygame.draw.circle(surf, (*BONUS_ZONE_C, 40), (cx, cy), r - 6, 1)


def draw_croquettes(surf, croquettes, pulse):
    for c in croquettes:
        x, y = int(c["x"]), int(c["y"])
        bob = int(3 * math.sin(pulse * 2))
        pygame.draw.circle(surf, (160, 110, 40), (x, y + bob + 2), CROQUETTE_R)
        pygame.draw.circle(surf, CROQUETTE_C, (x, y + bob), CROQUETTE_R - 2)


def draw_scratches(surf, scratches, now):
    for s in scratches:
        age = now - s["born"]
        if age > 4000:
            continue
        x, y = int(s["x"]), int(s["y"])
        for dx, dy in [(-8, -4), (0, 0), (8, 4)]:
            pygame.draw.line(surf, SCRATCH, (x + dx, y + dy), (x + dx + 14, y - dy - 10), 2)


def draw_trail(surf, laser):
    trail = laser["trail"]
    for i, (tx, ty) in enumerate(trail):
        alpha = int(180 * (i + 1) / len(trail)) if trail else 0
        r = max(2, laser_radius(laser) - (len(trail) - i) // 2)
        col = tuple(min(255, c + 30) for c in laser.get("color", LASER))
        pygame.draw.circle(surf, col, (int(tx), int(ty)), r)


def draw_laser(surf, laser, pulse, frozen):
    x, y = int(laser["x"]), int(laser["y"])
    col = laser.get("color", LASER)
    r = laser_radius(laser)
    glow = r + 6 + int(3 * math.sin(pulse))
    if laser.get("is_boss"):
        pygame.draw.circle(surf, (120, 40, 180), (x, y), glow + 10, 3)
    if frozen:
        pygame.draw.circle(surf, (140, 200, 255), (x, y), glow + 4)
    pygame.draw.circle(surf, LASER_GLOW, (x, y), glow)
    pygame.draw.circle(surf, col, (x, y), r)
    pygame.draw.circle(surf, (255, 220, 220), (x - r // 4, y - r // 4), max(3, r // 4))


def draw_malik(surf, malik, font):
    if not malik:
        return
    x, y = int(malik["x"]), int(malik["y"])
    pygame.draw.line(surf, MALIK_COLOR, (x - 18, y + 20), (x - 8, y - 18), 4)
    pygame.draw.line(surf, MALIK_COLOR, (x + 18, y + 20), (x + 8, y - 18), 4)
    pygame.draw.circle(surf, MALIK_COLOR, (x, y - 22), 12)
    t = font.render("MALIK", True, (255, 80, 80))
    surf.blit(t, (x - t.get_width() // 2, y - 48))


def draw_player(surf, game, combo, frozen_purr):
    p = game["player"]
    size = player_size(combo)
    if size != game["sprite"].get_width():
        game["sprite"] = load_nahla_sprite(size)
    img = game["sprite"]
    if p["facing"] < 0:
        img = pygame.transform.flip(img, True, False)
    px, py = int(p["x"] - size // 2), int(p["y"] - size // 2)
    if frozen_purr:
        pygame.draw.circle(surf, (140, 200, 255, 80), (int(p["x"]), int(p["y"])), size // 2 + 8, 3)
    surf.blit(img, (px, py))


def draw_combo_bar(surf, combo):
    bar_x, bar_y, bar_w, bar_h = 20, PLAY_TOP - 14, 200, 10
    fill = min(1.0, combo / 50)
    pygame.draw.rect(surf, (40, 35, 50), (bar_x, bar_y, bar_w, bar_h), border_radius=4)
    if fill > 0:
        pygame.draw.rect(surf, LASER, (bar_x, bar_y, int(bar_w * fill), bar_h), border_radius=4)
    pygame.draw.rect(surf, ACCENT, (bar_x, bar_y, bar_w, bar_h), 1, border_radius=4)


def draw_hud(surf, font, small, game, now, high_score):
    pygame.draw.rect(surf, (18, 16, 24), (0, 0, WIDTH, PLAY_TOP - 4))
    if game["mode"] == MODE_CHRONO and game["match_end"]:
        time_txt = f"Temps : {max(0, (game['match_end'] - now) // 1000)}s"
    else:
        elapsed = (now - game["match_start"]) // 1000
        time_txt = f"Temps : {elapsed}s ∞"
    surf.blit(font.render(f"Score : {game['score']}", True, ACCENT), (240, 18))
    surf.blit(font.render(f"Combo : x{game['combo']}", True, LASER), (400, 18))
    surf.blit(font.render(f"Record : {high_score}", True, TEXT), (580, 18))
    surf.blit(font.render(time_txt, True, TEXT), (WIDTH - 180, 18))
    draw_combo_bar(surf, game["combo"])
    if game["on_couch"]:
        surf.blit(small.render("Canapé — bonus repos (+score, pas de combo)", True, WIN_C), (20, 54))
    if now < game.get("bonus_mult_until", 0):
        surf.blit(small.render("ZONE x2 SCORE !!!", True, BONUS_ZONE_C), (360, 54))
    if game.get("boss_phase"):
        surf.blit(small.render("BOSS LASER — 10 dernières secondes", True, BOSS_C), (WIDTH // 2 - 130, 54))
    if now < game["dash_cooldown_until"]:
        cd = (game["dash_cooldown_until"] - now) // 1000 + 1
        surf.blit(small.render(f"Dash : {cd}s", True, TEXT), (WIDTH - 120, 54))
    if now < game["purr_cooldown_until"]:
        cd = (game["purr_cooldown_until"] - now) // 1000 + 1
        surf.blit(small.render(f"Ronron : {cd}s", True, (140, 200, 255)), (WIDTH - 250, 54))
    if now < game["taunt_until"] and game["taunt"]:
        t = font.render(game["taunt"], True, WIN_C)
        surf.blit(t, (WIDTH // 2 - t.get_width() // 2, 54))


def draw_overlay(surf, big, small, title, lines):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((8, 6, 14, 175))
    surf.blit(overlay, (0, 0))
    t = big.render(title, True, TEXT)
    surf.blit(t, (WIDTH // 2 - t.get_width() // 2, HEIGHT // 2 - 130))
    for i, line in enumerate(lines):
        s = small.render(line, True, TEXT)
        surf.blit(s, (WIDTH // 2 - s.get_width() // 2, HEIGHT // 2 - 50 + i * 30))


def draw_menu(surf, big, small, menu_diff, menu_mode, high_score):
    draw_overlay(
        surf, big, small, "Nahla vs le laser",
        [
            "Traque le laser — combo, griffures, canapé refuge",
            "ZQSD bouger · Espace dash · F ronron (fige 1s)",
            "",
            f"Difficulté : {'Normal' if menu_diff == DIFF_NORMAL else 'Difficile'}  (← →)",
            f"Mode : {'Chrono 90s' if menu_mode == MODE_CHRONO else 'Infini'}  (↑ ↓)",
            f"Meilleur score : {high_score}",
            "",
            "Entrée ou Espace — jouer",
        ],
    )


def process_laser_catch(game, laser, px, py, now, sounds, couch, diff):
    r = laser_radius(laser)
    catch_size = player_size(game["combo"]) // 2 + r
    if dist(px, py, laser["x"], laser["y"]) >= catch_size:
        laser["hold_frames"] = 0
        return False
    if couch:
        game["score"] += COUCH_BONUS_SCORE * score_mult(game, now)
        return True
    laser["hold_frames"] = laser.get("hold_frames", 0) + 1
    if game["combo"] > SPLIT_COMBO_MIN and laser["hold_frames"] >= SPLIT_HOLD_FRAMES:
        split_laser(game, laser, diff)
        return True
    game["combo"] += 1
    mult = score_mult(game, now)
    gain = game["combo"] * mult
    if laser.get("is_boss"):
        gain *= 3
    game["score"] += gain
    game["last_catch_ms"] = now
    game["best_combo"] = max(game["best_combo"], game["combo"])
    add_scratch(game["scratches"], laser["x"], laser["y"])
    if sounds.get("scratch"):
        sounds["scratch"].play()
    if game["combo"] % 5 == 0 and sounds.get("meow"):
        sounds["meow"].play()
    if game["combo"] % 10 == 0 and sounds.get("combo"):
        sounds["combo"].play()
    if game["combo"] % TAUNT_EVERY == 0:
        game["taunt"] = random.choice(NAHLA_LINES)
        game["taunt_until"] = now + 2200
    flee_laser(laser, px, py)
    return True


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("menlo,consolas,monospace", 22)
    small = pygame.font.SysFont("menlo,consolas,monospace", 16)
    big = pygame.font.SysFont("menlo,consolas,monospace", 44, bold=True)

    sounds = load_sounds()
    high_score = load_highscore()

    state = MENU
    menu_diff = DIFF_NORMAL
    menu_mode = MODE_CHRONO
    game = reset_match(menu_mode, menu_diff)
    t0 = pygame.time.get_ticks()

    running = True
    while running:
        now = pygame.time.get_ticks()
        clock.tick(FPS)
        pulse = (now - t0) / 120
        frozen = now < game.get("freeze_until", 0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if state == PLAYING and game["mode"] == MODE_INFINI:
                        state = OVER
                        game["grade"] = grade_for_score(game["score"])
                        if game["score"] > high_score:
                            high_score = game["score"]
                            save_highscore(high_score)
                    else:
                        running = False
                if state == MENU:
                    if event.key == pygame.K_LEFT:
                        menu_diff = DIFF_NORMAL
                    if event.key == pygame.K_RIGHT:
                        menu_diff = DIFF_HARD
                    if event.key == pygame.K_UP:
                        menu_mode = MODE_CHRONO
                    if event.key == pygame.K_DOWN:
                        menu_mode = MODE_INFINI
                    if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                        state = PLAYING
                        game = reset_match(menu_mode, menu_diff)
                if state == OVER and event.key in (pygame.K_RETURN, pygame.K_SPACE, pygame.K_r):
                    state = MENU
                if state == PLAYING:
                    if event.key == pygame.K_SPACE and now >= game["dash_cooldown_until"]:
                        p = game["player"]
                        mag = math.hypot(p["last_dx"], p["last_dy"]) or 1
                        game["dash_dx"] = p["last_dx"] / mag
                        game["dash_dy"] = p["last_dy"] / mag
                        game["dash_until"] = now + DASH_MS
                        game["dash_cooldown_until"] = now + DASH_COOLDOWN_MS
                    if event.key == pygame.K_f and now >= game["purr_cooldown_until"]:
                        game["freeze_until"] = now + PURR_FREEZE_MS
                        game["purr_cooldown_until"] = now + PURR_COOLDOWN_MS
                        if sounds.get("purr"):
                            sounds["purr"].play()

        keys = pygame.key.get_pressed()

        if state == PLAYING:
            p = game["player"]
            speed = DASH_SPEED if now < game.get("dash_until", 0) else PLAYER_SPEED
            dx = dy = 0
            if key_down(keys, MOVE_LEFT):
                dx -= 1
                p["facing"] = -1
            if key_down(keys, MOVE_RIGHT):
                dx += 1
                p["facing"] = 1
            if key_down(keys, MOVE_UP):
                dy -= 1
            if key_down(keys, MOVE_DOWN):
                dy += 1
            if now < game.get("dash_until", 0) and game.get("dash_dx") is not None:
                p["x"] += game["dash_dx"] * speed
                p["y"] += game["dash_dy"] * speed
            elif dx or dy:
                mag = math.hypot(dx, dy) or 1
                p["last_dx"], p["last_dy"] = dx, dy
                p["x"] += dx / mag * speed
                p["y"] += dy / mag * speed
            p["x"] = clamp(p["x"], PLAY_LEFT + 30, PLAY_RIGHT - 30)
            p["y"] = clamp(p["y"], PLAY_TOP + 30, PLAY_BOTTOM - 30)

            game["on_couch"] = on_couch(p["x"], p["y"])
            elapsed = (now - game["match_start"]) / 1000

            in_bonus = False
            for zone in BONUS_ZONES:
                if dist(p["x"], p["y"], zone["cx"], zone["cy"]) < zone["r"]:
                    in_bonus = True
                    if not game["in_bonus_zone"]:
                        game["bonus_mult_until"] = now + BONUS_DURATION_MS
                    break
            game["in_bonus_zone"] = in_bonus

            if (
                game["mode"] == MODE_CHRONO
                and game["match_end"]
                and not game["boss_phase"]
                and game["match_end"] - now <= BOSS_LAST_MS
            ):
                game["boss_phase"] = True
                game["lasers"] = [spawn_boss_laser(game["difficulty"])]
                game["taunt"] = "BOSS LASER — tiens bon !"
                game["taunt_until"] = now + 2500
                if sounds.get("boss"):
                    sounds["boss"].play()

            if now >= game["croquette_next"] and len(game["croquettes"]) < 4:
                game["croquettes"].append(spawn_croquette())
                game["croquette_next"] = now + CROQUETTE_SPAWN_MS

            for croq in game["croquettes"][:]:
                if dist(p["x"], p["y"], croq["x"], croq["y"]) < CROQUETTE_R + player_size(game["combo"]) // 3:
                    game["croquettes"].remove(croq)
                    game["score"] += CROQUETTE_SCORE * score_mult(game, now)
                    game["dash_cooldown_until"] = max(
                        now, game["dash_cooldown_until"] - CROQUETTE_DASH_REDUCE_MS
                    )
                    if sounds.get("pickup"):
                        sounds["pickup"].play()

            if not game["laser2_spawned"] and not game["boss_phase"] and elapsed * 1000 >= SECOND_LASER_AT_MS:
                l2 = new_laser(DIFF_MULT[game["difficulty"]]["speed"])
                l2["color"] = LASER2
                game["lasers"].append(l2)
                game["laser2_spawned"] = True

            if now >= game["malik_next"]:
                game["malik"] = spawn_malik(now)
                game["malik_next"] = now + MALIK_INTERVAL_MS + random.randint(-4000, 4000)

            malik = game["malik"]
            if malik and now < malik["until"]:
                malik["x"] += malik["vx"]
                for laser in game["lasers"]:
                    if abs(laser["x"] - malik["x"]) < 80 and abs(laser["y"] - malik["y"]) < 60:
                        flee_laser(laser, malik["x"], malik["y"])
                        laser["speed"] *= 1.15
            elif malik:
                game["malik"] = None

            for laser in game["lasers"]:
                update_laser(laser, elapsed, frozen, game["difficulty"])

            caught_any = False
            for laser in game["lasers"][:]:
                if process_laser_catch(
                    game, laser, p["x"], p["y"], now, sounds, game["on_couch"], game["difficulty"]
                ):
                    caught_any = True
            if caught_any:
                game["last_catch_ms"] = now
            elif now - game["last_catch_ms"] > COMBO_DECAY_MS:
                game["combo"] = 0

            if game["mode"] == MODE_CHRONO and game["match_end"] and now >= game["match_end"]:
                state = OVER
                game["grade"] = grade_for_score(game["score"])
                if game["score"] > high_score:
                    high_score = game["score"]
                    save_highscore(high_score)

        draw_room(screen)
        if state != MENU:
            draw_bonus_zones(screen, pulse, now < game.get("bonus_mult_until", 0))
            draw_croquettes(screen, game.get("croquettes", []), pulse)
        draw_scratches(screen, game["scratches"], now)
        if state != MENU:
            for laser in game["lasers"]:
                draw_trail(screen, laser)
                draw_laser(screen, laser, pulse, frozen)
            draw_malik(screen, game.get("malik"), small)
            draw_player(screen, game, game["combo"], frozen)
        draw_hud(screen, font, small, game, now, high_score)

        if state == MENU:
            draw_menu(screen, big, small, menu_diff, menu_mode, high_score)
        elif state == OVER:
            draw_overlay(
                screen, big, small, "Sieste méritée",
                [
                    f"Grade : {game.get('grade', grade_for_score(game['score']))}",
                    f"Score final : {game['score']}",
                    f"Meilleur combo : x{game['best_combo']}",
                    f"Record : {high_score}",
                    "R ou Entrée — menu",
                ],
            )

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
