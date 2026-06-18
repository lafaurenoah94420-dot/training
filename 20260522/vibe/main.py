"""
HOI4 — Mini bataille de chars (vibe 2026-05-22)
Carte vue du dessus, divisions, offensive automatique.
"""

import math
import random
import sys

import pygame

CELL = 20
COLS = 50
ROWS = 30
MAP_H = ROWS * CELL
HUD_H = 56
WIDTH = COLS * CELL
HEIGHT = MAP_H + HUD_H
FRONT_COL = COLS // 2
PLAYER_HQ_GX = 5
ENEMY_HQ_GX = COLS - 6
HQ_GY = ROWS // 2

MUD = 0
MUD_DARK = 1
CRATER = 2
TRENCH = 3
ROAD = 4
SCORCHED = 5
RUIN = 6
SHELL_WATER = 7

TERRAIN_COLORS = {
    MUD: (72, 58, 42),
    MUD_DARK: (58, 46, 34),
    CRATER: (42, 38, 32),
    TRENCH: (38, 32, 28),
    ROAD: (90, 82, 68),
    SCORCHED: (52, 44, 36),
    RUIN: (65, 55, 48),
    SHELL_WATER: (48, 52, 58),
}

COLOR_BG = (18, 20, 16)
COLOR_HUD = (18, 22, 18)
COLOR_FRONT = (120, 100, 70)

TEAM_PLAYER = "player"
TEAM_ENEMY = "enemy"
MAX_PLAYER_DIVISIONS = 34
DIVISION_STRENGTH = 10
BLOCKED_TERRAIN = {SHELL_WATER}
TRENCH_DAMAGE_DIV = 2
TRENCH_PLACE_BONUS = 2
NEIGHBORS = ((1, 0), (-1, 0), (0, 1), (0, -1))
DIAGONAL = ((1, 1), (1, -1), (-1, 1), (-1, -1))
ALL_DIRS = NEIGHBORS + DIAGONAL
BATTLE_TICK_INTERVAL = 16
PHASE_PREP = "prep"
PHASE_BATTLE = "battle"
PHASE_END = "end"
SCENARIO_OFFENSIVE = "offensive"
SCENARIO_DEFENSIVE = "defensive"

WEAPON_RIFLE = "fusil"
WEAPON_MG = "mitrailleuse"
WEAPON_CANNON = "canon"

WEAPON_DAMAGE = {
    WEAPON_RIFLE: 4,
    WEAPON_MG: 6,
    WEAPON_CANNON: 8,
}

WEAPON_RANGE = {
    WEAPON_RIFLE: 3,
    WEAPON_MG: 4,
    WEAPON_CANNON: 6,
}
TRENCH_RANGE_BONUS = 3

# Nations en guerre (1914-1916) — drapeaux dessinés dans le menu
COUNTRY_FRANCE = "france"
COUNTRY_UK = "uk"
COUNTRY_BELGIUM = "belgium"
COUNTRY_SERBIA = "serbia"
COUNTRY_RUSSIA = "russia"
COUNTRY_ITALY = "italy"
COUNTRY_ROMANIA = "romania"
COUNTRY_GERMANY = "germany"
COUNTRY_AUSTRIA = "austria"
COUNTRY_OTTOMAN = "ottoman"

COUNTRIES = {
    COUNTRY_FRANCE: {
        "name": "France",
        "year": "1914",
        "fill": (55, 95, 165),
        "border": (140, 190, 255),
    },
    COUNTRY_UK: {
        "name": "Royaume-Uni",
        "year": "1914",
        "fill": (45, 55, 120),
        "border": (200, 180, 120),
    },
    COUNTRY_BELGIUM: {
        "name": "Belgique",
        "year": "1914",
        "fill": (180, 50, 45),
        "border": (240, 200, 60),
    },
    COUNTRY_SERBIA: {
        "name": "Serbie",
        "year": "1914",
        "fill": (160, 45, 50),
        "border": (90, 130, 200),
    },
    COUNTRY_RUSSIA: {
        "name": "Russie",
        "year": "1914",
        "fill": (90, 110, 170),
        "border": (220, 210, 200),
    },
    COUNTRY_ITALY: {
        "name": "Italie",
        "year": "1915",
        "fill": (55, 130, 75),
        "border": (240, 240, 235),
    },
    COUNTRY_ROMANIA: {
        "name": "Roumanie",
        "year": "1916",
        "fill": (45, 75, 150),
        "border": (220, 190, 50),
    },
    COUNTRY_GERMANY: {
        "name": "Allemagne",
        "year": "1914",
        "fill": (55, 55, 60),
        "border": (200, 200, 205),
    },
    COUNTRY_AUSTRIA: {
        "name": "Autriche-Hongrie",
        "year": "1914",
        "fill": (150, 45, 45),
        "border": (240, 230, 220),
    },
    COUNTRY_OTTOMAN: {
        "name": "Empire ottoman",
        "year": "1914",
        "fill": (165, 35, 35),
        "border": (240, 220, 160),
    },
}

COUNTRY_MENU_ORDER = [
    COUNTRY_FRANCE,
    COUNTRY_UK,
    COUNTRY_BELGIUM,
    COUNTRY_SERBIA,
    COUNTRY_RUSSIA,
    COUNTRY_ITALY,
    COUNTRY_ROMANIA,
    COUNTRY_GERMANY,
    COUNTRY_AUSTRIA,
    COUNTRY_OTTOMAN,
]


def generate_battlefield():
    """Champ de bataille : boue, tranchees, cratères, route, zone no man's land."""
    random.seed(1944)
    grid = [[MUD for _ in range(COLS)] for _ in range(ROWS)]

        for y in range(ROWS):
            for x in range(COLS):
            if x < FRONT_COL - 3:
                grid[y][x] = MUD if random.random() < 0.7 else MUD_DARK
            elif x > FRONT_COL + 3:
                grid[y][x] = SCORCHED if random.random() < 0.65 else MUD_DARK
    else:
                grid[y][x] = MUD_DARK if random.random() < 0.5 else SCORCHED

    for _ in range(85):
        x = random.randint(2, COLS - 3)
        y = random.randint(2, ROWS - 3)
        grid[y][x] = CRATER
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < COLS and 0 <= ny < ROWS and random.random() < 0.4:
                grid[ny][nx] = CRATER

    for _ in range(12):
        x = random.randint(4, COLS - 5)
        y = random.randint(4, ROWS - 5)
        grid[y][x] = SHELL_WATER

    carve_trench_network(grid)

        for x in range(COLS):
        mid = ROWS // 2 + int(3 * (x / COLS - 0.5))
        for dy in range(-1, 2):
            ry = mid + dy
            if 0 <= ry < ROWS:
                grid[ry][x] = ROAD

    for _ in range(18):
        bx = random.randint(2, COLS - 4)
        by = random.randint(2, ROWS - 4)
        for ox in range(2):
            for oy in range(2):
                grid[by + oy][bx + ox] = RUIN

    return grid


def set_trench_cell(grid, x, y):
    if 0 <= x < COLS and 0 <= y < ROWS and grid[y][x] not in (ROAD, SHELL_WATER):
        grid[y][x] = TRENCH


def carve_trench_belt(grid, base_x):
    """Ligne de tranchées verticales (2 cases de large)."""
    for y in range(3, ROWS - 3):
        set_trench_cell(grid, base_x, y)
        set_trench_cell(grid, base_x + 1, y)


def carve_trench_network(grid):
    """Tranchées verticales : réseau ouest (toi) + lignes est (ennemi)."""
    for x in range(8, FRONT_COL - 4, 6):
        carve_trench_belt(grid, x)
    for x in range(FRONT_COL + 4, COLS - 6, 7):
        carve_trench_belt(grid, x)


def is_in_trench(grid, gx, gy):
    return grid[gy][gx] == TRENCH


def cell_center(gx, gy):
    return gx * CELL + CELL // 2, gy * CELL + CELL // 2


def pos_to_cell(mx, my):
    if my >= MAP_H:
        return None
    gx = mx // CELL
    gy = my // CELL
    if 0 <= gx < COLS and 0 <= gy < ROWS:
        return gx, gy
    return None


def division_at(divisions, gx, gy):
    for d in divisions:
        if d["gx"] == gx and d["gy"] == gy:
            return d
    return None


def can_place_division(grid, divisions, gx, gy, team):
    if division_at(divisions, gx, gy) is not None:
        return False
    if grid[gy][gx] in BLOCKED_TERRAIN:
        return False
    if team == TEAM_PLAYER and gx >= FRONT_COL - 2:
        return False
    if team == TEAM_ENEMY and gx <= FRONT_COL + 2:
        return False
    return True


def new_division(gx, gy, team, kind="infantry", weapon=WEAPON_RIFLE):
    if kind == "armor":
        weapon = WEAPON_CANNON
    return {
        "gx": gx,
        "gy": gy,
        "team": team,
        "strength": DIVISION_STRENGTH,
        "kind": kind,
        "weapon": weapon,
        "in_trench": False,
        "shoot_flash": 0,
        "idle": 0,
        "shot_gx": None,
        "shot_gy": None,
    }


def pick_enemy_weapon(kind):
    if kind == "armor":
        return WEAPON_CANNON
    if random.random() < 0.22:
        return WEAPON_MG
    return WEAPON_RIFLE


def try_add_enemy(divisions, grid, gx, gy, kind="infantry"):
    if can_place_division(grid, divisions, gx, gy, TEAM_ENEMY):
        unit = new_division(gx, gy, TEAM_ENEMY, kind, pick_enemy_weapon(kind))
        if is_in_trench(grid, gx, gy):
            unit["strength"] += TRENCH_PLACE_BONUS
        divisions.append(unit)
        return True
    return False


def spawn_enemy_divisions(grid, scenario=SCENARIO_OFFENSIVE):
    """Disposition realiste : ligne de front, reserves, chars en rerve."""
    divisions = []
    front_x = FRONT_COL + 3

    # 1) Ligne de front face au no man's land (infanterie espacée)
    for y in range(6, ROWS - 6, 2):
        try_add_enemy(divisions, grid, front_x, y, "infantry")

    # 2) Deuxième vague juste derrière (trous comblés)
    second_x = FRONT_COL + 7
    for y in range(8, ROWS - 8, 4):
        try_add_enemy(divisions, grid, second_x, y, "infantry")
        try_add_enemy(divisions, grid, second_x + 1, y + 1, "infantry")

    # 3) Chars en réserve — axe central (route) + flancs nord/sud
    mid_y = ROWS // 2
    armor_posts = [
        (FRONT_COL + 12, mid_y),
        (FRONT_COL + 12, mid_y - 1),
        (FRONT_COL + 15, mid_y + 2),
        (FRONT_COL + 15, mid_y - 2),
        (COLS - 7, 7),
        (COLS - 7, ROWS - 8),
        (COLS - 5, mid_y),
    ]
    for gx, gy in armor_posts:
        try_add_enemy(divisions, grid, gx, gy, "armor")

    # 4) Quartier général à l'est (derrière tout)
    hq_x = ENEMY_HQ_GX
    for gy in (mid_y - 3, mid_y, mid_y + 3):
        try_add_enemy(divisions, grid, hq_x, gy, "infantry")

    if scenario == SCENARIO_DEFENSIVE:
        for y in range(5, ROWS - 5, 2):
            try_add_enemy(divisions, grid, front_x, y, "infantry")
            try_add_enemy(divisions, grid, front_x + 1, y, "armor")

    return divisions


def unit_should_advance(unit, scenario):
    if scenario == SCENARIO_OFFENSIVE:
        return True
    return unit["team"] == TEAM_ENEMY


def living_count(divisions, team):
    return sum(1 for d in divisions if d["team"] == team and d["strength"] > 0)


def manhattan(gx1, gy1, gx2, gy2):
    return abs(gx1 - gx2) + abs(gy1 - gy2)


def chebyshev(gx1, gy1, gx2, gy2):
    return max(abs(gx1 - gx2), abs(gy1 - gy2))


def unit_range(unit, grid):
    """Portée de tir selon l'arme ; bonus en tranchée."""
    base = WEAPON_RANGE.get(unit.get("weapon", WEAPON_RIFLE), 3)
    if is_in_trench(grid, unit["gx"], unit["gy"]):
        base += TRENCH_RANGE_BONUS
    return base


def enemies_in_range(unit, divisions, grid):
    """Ennemis à portée de tir (distance Chebyshev)."""
    rng = unit_range(unit, grid)
    foes = []
    for foe in divisions:
        if foe["team"] == unit["team"] or foe["strength"] <= 0:
            continue
        dist = chebyshev(unit["gx"], unit["gy"], foe["gx"], foe["gy"])
        if 1 <= dist <= rng:
            foes.append(foe)
    return foes


def forward_score(gx, team):
    """Plus la valeur est haute, plus la case pousse vers le front ennemi."""
    if team == TEAM_ENEMY:
        return -gx
    return gx


def nearest_enemy(unit, divisions):
    target = None
    best_dist = 99999
    for d in divisions:
        if d["team"] == unit["team"] or d["strength"] <= 0:
            continue
        dist = abs(d["gx"] - unit["gx"]) + abs(d["gy"] - unit["gy"])
        if dist < best_dist:
            best_dist = dist
            target = d
    return target


def can_move_to(grid, divisions, gx, gy, mover):
    if not (0 <= gx < COLS and 0 <= gy < ROWS):
        return False
    if grid[gy][gx] in BLOCKED_TERRAIN:
        return False
    other = division_at(divisions, gx, gy)
    if other is not None and other is not mover:
        return False
    return True


def try_move_toward(unit, divisions, grid, target):
    """Avance vers l'ennemi ; s'arrête dès qu'une cible est à portée de tir."""
    if target is None:
        return
    if enemies_in_range(unit, divisions, grid):
        unit["idle"] = 0
        return

    ux, uy = unit["gx"], unit["gy"]
    tx, ty = target["gx"], target["gy"]
    current_dist = manhattan(ux, uy, tx, ty)

    candidates = []
    for mdx, mdy in ALL_DIRS:
        nx, ny = ux + mdx, uy + mdy
        if not can_move_to(grid, divisions, nx, ny, unit):
            continue
        dist = manhattan(nx, ny, tx, ty)
        candidates.append((dist, nx, ny))

    if not candidates:
        unit["idle"] = unit.get("idle", 0) + 1
        return

    closer = [c for c in candidates if c[0] < current_dist]
    if closer:
        pool = closer
    else:
        # Même distance : décaler sur le flanc pour débloquer la réserve
        pool = [c for c in candidates if c[0] == current_dist]
        if not pool and unit.get("idle", 0) >= 5:
            # Coincé longtemps : accepter un pas de côté même un peu plus loin
            pool = [c for c in candidates if c[0] <= current_dist + 1]

    if not pool:
        unit["idle"] = unit.get("idle", 0) + 1
        return

    best_dist = min(c[0] for c in pool)
    pool = [c for c in pool if c[0] == best_dist]

    def rank(c):
        dist, nx, ny = c
        lateral = abs(ny - ty)
        fwd = forward_score(nx, unit["team"])
        return (lateral, -fwd, random.random())

    _, nx, ny = min(pool, key=rank)
    if (nx, ny) != (ux, uy):
        unit["gx"], unit["gy"] = nx, ny
        unit["idle"] = 0
    else:
        unit["idle"] = unit.get("idle", 0) + 1


def attack_damage(attacker, defender, grid, distance=1):
    dmg = WEAPON_DAMAGE.get(attacker.get("weapon", WEAPON_RIFLE), 4)
    if defender["kind"] == "armor":
        dmg += 1
    if distance > 1:
        dmg = max(1, dmg - (distance - 1))
    if is_in_trench(grid, defender["gx"], defender["gy"]):
        dmg = max(1, dmg // TRENCH_DAMAGE_DIV)
    return dmg


def resolve_combat(divisions, grid):
    """Tir à distance : chaque paire en portée échange des tirs une fois par tour."""
    fought = set()
    for unit in divisions:
        if unit["strength"] <= 0:
            continue
        foes = enemies_in_range(unit, divisions, grid)
        if not foes:
            continue
        foe = min(
            foes,
            key=lambda f: chebyshev(unit["gx"], unit["gy"], f["gx"], f["gy"]),
        )
        pair = tuple(sorted([id(unit), id(foe)]))
        if pair in fought:
            continue
        fought.add(pair)

        dist = chebyshev(unit["gx"], unit["gy"], foe["gx"], foe["gy"])
        foe["strength"] -= attack_damage(unit, foe, grid, dist)
        if chebyshev(foe["gx"], foe["gy"], unit["gx"], unit["gy"]) <= unit_range(
            foe, grid
        ):
            foe_dist = chebyshev(foe["gx"], foe["gy"], unit["gx"], unit["gy"])
            unit["strength"] -= attack_damage(foe, unit, grid, foe_dist)

        unit["shoot_flash"] = 8
        foe["shoot_flash"] = 8
        unit["shot_gx"], unit["shot_gy"] = foe["gx"], foe["gy"]
        foe["shot_gx"], foe["shot_gy"] = unit["gx"], unit["gy"]


def battle_tick(divisions, grid, scenario):
    movers = [d for d in divisions if d["strength"] > 0]
    random.shuffle(movers)
    for unit in movers:
        if unit_should_advance(unit, scenario):
            target = nearest_enemy(unit, divisions)
            try_move_toward(unit, divisions, grid, target)
    resolve_combat(divisions, grid)
    divisions[:] = [d for d in divisions if d["strength"] > 0]


def check_winner(divisions):
    if living_count(divisions, TEAM_ENEMY) == 0:
        return "victoire"
    if living_count(divisions, TEAM_PLAYER) == 0:
        return "defaite"
    return None


def try_place_player(divisions, grid, mx, my, place_kind, place_weapon):
    if len([d for d in divisions if d["team"] == TEAM_PLAYER]) >= MAX_PLAYER_DIVISIONS:
        return False
    cell = pos_to_cell(mx, my)
    if not cell:
        return False
    gx, gy = cell
    if not can_place_division(grid, divisions, gx, gy, TEAM_PLAYER):
        return False
    kind = place_kind
    weapon = WEAPON_CANNON if kind == "armor" else place_weapon
    unit = new_division(gx, gy, TEAM_PLAYER, kind, weapon)
    if is_in_trench(grid, gx, gy):
        unit["strength"] += TRENCH_PLACE_BONUS
    divisions.append(unit)
    return True


def weapon_label(weapon):
    labels = {
        WEAPON_RIFLE: "FUSIL",
        WEAPON_MG: "MITRAILLEUSE",
        WEAPON_CANNON: "CANON",
    }
    return labels.get(weapon, weapon.upper())


def draw_weapon(surface, d, cx, cy):
    w = d.get("weapon", WEAPON_RIFLE)
    gun_color = (50, 50, 55) if d["team"] == TEAM_PLAYER else (35, 35, 40)
    flash = d.get("shoot_flash", 0) > 0
    muzzle = (255, 240, 120) if flash else (200, 200, 210)

    if w == WEAPON_CANNON:
        pygame.draw.rect(surface, gun_color, (cx + 6, cy - 3, 12, 5))
        pygame.draw.line(surface, muzzle, (cx + 18, cy - 1), (cx + 28, cy - 3), 3)
    elif w == WEAPON_MG:
        pygame.draw.line(surface, gun_color, (cx + 2, cy), (cx + 12, cy - 3), 3)
        pygame.draw.line(surface, gun_color, (cx + 2, cy + 2), (cx + 12, cy - 1), 2)
        if flash:
            pygame.draw.circle(surface, muzzle, (cx + 14, cy - 2), 4)
    else:
        pygame.draw.line(surface, gun_color, (cx + 2, cy - 1), (cx + 14, cy - 4), 2)
        if flash:
            pygame.draw.circle(surface, muzzle, (cx + 15, cy - 4), 3)


def country_colors(country_id):
    info = COUNTRIES[country_id]
    return info["fill"], info["border"]


def draw_shot_tracers(surface, divisions):
    """Trait de tir visible quand une unité tire à distance."""
    for d in divisions:
        if d.get("shoot_flash", 0) <= 0 or d.get("shot_gx") is None:
            continue
        cx, cy = cell_center(d["gx"], d["gy"])
        tx, ty = cell_center(d["shot_gx"], d["shot_gy"])
        pygame.draw.line(surface, (255, 215, 70), (cx, cy), (tx, ty), 2)
        pygame.draw.circle(surface, (255, 180, 50), (tx, ty), 3)


def draw_division(surface, d, player_country, enemy_country):
    cx, cy = cell_center(d["gx"], d["gy"])
    cid = player_country if d["team"] == TEAM_PLAYER else enemy_country
    fill, border = country_colors(cid)

    if d["kind"] == "armor":
        pygame.draw.rect(surface, fill, (cx - 9, cy - 6, 18, 12), border_radius=2)
        pygame.draw.rect(surface, (40, 40, 45), (cx - 7, cy - 8, 14, 5))
        pygame.draw.circle(surface, (30, 30, 35), (cx - 5, cy + 5), 3)
        pygame.draw.circle(surface, (30, 30, 35), (cx + 5, cy + 5), 3)
    else:
        pygame.draw.circle(surface, fill, (cx, cy), 8)
        pygame.draw.circle(surface, border, (cx, cy), 8, 2)

    draw_weapon(surface, d, cx, cy)

    if d.get("in_trench"):
        pygame.draw.rect(surface, (95, 85, 65), (cx - 10, cy + 5, 20, 4), border_radius=1)

    font = pygame.font.SysFont(None, 16)
    label = font.render(str(d["strength"]), True, (255, 255, 240))
    surface.blit(label, (cx - label.get_width() // 2, cy - 5))


def refresh_trench_status(divisions, grid):
    for d in divisions:
        d["in_trench"] = is_in_trench(grid, d["gx"], d["gy"])
        if d.get("shoot_flash", 0) > 0:
            d["shoot_flash"] -= 1


def place_tool_label(kind, weapon):
    if kind == "armor":
        return "CHAR + CANON"
    return weapon_label(weapon)


def draw_divisions(surface, divisions, player_country, enemy_country):
    for d in divisions:
        draw_division(surface, d, player_country, enemy_country)


def draw_cell(surface, x, y, terrain):
    rect = pygame.Rect(x * CELL, y * CELL, CELL, CELL)
    base = TERRAIN_COLORS[terrain]
    pygame.draw.rect(surface, base, rect)

    cx = rect.centerx
    cy = rect.centery

    if terrain == CRATER:
        pygame.draw.ellipse(surface, (32, 28, 24), rect.inflate(-4, -6))
        pygame.draw.ellipse(surface, (28, 24, 20), rect.inflate(-8, -10))
    elif terrain == TRENCH:
        pygame.draw.rect(surface, (32, 28, 24), rect.inflate(-2, -2))
        pygame.draw.line(surface, (22, 18, 16), (cx, rect.top + 2), (cx, rect.bottom - 2), 3)
        pygame.draw.line(surface, (50, 42, 36), (cx - 2, rect.top + 2), (cx - 2, rect.bottom - 2), 1)
        pygame.draw.rect(surface, (110, 95, 72), (rect.left + 1, rect.top + 1, 3, 3))
        pygame.draw.rect(surface, (110, 95, 72), (rect.right - 4, rect.top + 1, 3, 3))
    elif terrain == ROAD:
        pygame.draw.rect(surface, (100, 92, 78), rect.inflate(-6, -8))
    elif terrain == SHELL_WATER:
        pygame.draw.ellipse(surface, (55, 62, 72), rect.inflate(-5, -7))
    elif terrain == RUIN:
        pygame.draw.rect(surface, (45, 40, 36), (rect.x + 4, rect.y + 6, 5, 8))
        pygame.draw.rect(surface, (40, 35, 30), (rect.x + 10, rect.y + 8, 6, 6))
    elif terrain == SCORCHED:
        if (x + y) % 3 == 0:
            pygame.draw.line(surface, (40, 34, 28), (rect.left + 3, rect.top + 5), (rect.right - 4, rect.bottom - 4), 1)

    pygame.draw.rect(surface, (30, 26, 22), rect, 1)


def draw_front_line(surface):
    x = FRONT_COL * CELL
    for y in range(0, MAP_H, 12):
        pygame.draw.line(surface, COLOR_FRONT, (x, y), (x, min(y + 6, MAP_H)), 2)
    font = pygame.font.SysFont(None, 18)
    surface.blit(font.render("NO MAN'S LAND", True, (140, 120, 90)), (x - 52, 6))


def draw_map(surface, grid):
    for y in range(ROWS):
        for x in range(COLS):
            draw_cell(surface, x, y, grid[y][x])
    draw_front_line(surface)


def draw_hq_site(surface, gx, gy, country_id, flag_to_right):
    """Bunker de QG + mât avec le drapeau du pays choisi."""
    cx, cy = cell_center(gx, gy)
    bunker = pygame.Rect(cx - 18, cy - 2, 36, 16)
    pygame.draw.rect(surface, (42, 38, 34), bunker, border_radius=4)
    pygame.draw.rect(surface, (78, 70, 58), bunker, 2, border_radius=4)
    pygame.draw.rect(surface, (58, 52, 46), (cx - 6, cy - 6, 12, 8), border_radius=2)

    if flag_to_right:
        pole_x = cx + 12
        flag_rect = pygame.Rect(pole_x + 3, cy - 38, 62, 40)
    else:
        pole_x = cx - 12
        flag_rect = pygame.Rect(pole_x - 65, cy - 38, 62, 40)

    pygame.draw.line(surface, (95, 75, 48), (pole_x, cy + 10), (pole_x, cy - 36), 4)
    pygame.draw.circle(surface, (120, 95, 55), (pole_x, cy - 36), 4)
    draw_flag(surface, flag_rect, country_id)

    label_font = pygame.font.SysFont(None, 17)
    name_font = pygame.font.SysFont(None, 15)
    qg = label_font.render("QG", True, (235, 225, 190))
    surface.blit(qg, (cx - qg.get_width() // 2, cy + 14))
    short = COUNTRIES[country_id]["name"][:14]
    tag = name_font.render(short, True, (180, 175, 155))
    surface.blit(tag, (cx - tag.get_width() // 2, cy + 28))


def draw_headquarters(surface, player_country, enemy_country):
    """Drapeaux aux quartiers generaux ouest (toi) et est (ennemi)."""
    draw_hq_site(surface, PLAYER_HQ_GX, HQ_GY, player_country, flag_to_right=True)
    draw_hq_site(surface, ENEMY_HQ_GX, HQ_GY, enemy_country, flag_to_right=False)


def scenario_label(scenario):
    if scenario == SCENARIO_DEFENSIVE:
        return "SCENARIO DEFENSIF"
    return "SCENARIO OFFENSIF"


def country_display_name(country_id):
    info = COUNTRIES[country_id]
    return f"{info['name']} ({info['year']})"


def draw_hud(
    surface,
    font,
    divisions,
    phase,
    winner,
    scenario,
    place_kind,
    place_weapon,
    player_country,
    enemy_country,
):
    bar = pygame.Rect(0, MAP_H, WIDTH, HUD_H)
    pygame.draw.rect(surface, COLOR_HUD, bar)
    pygame.draw.line(surface, (70, 80, 60), (0, MAP_H), (WIDTH, MAP_H), 2)
    n_bleu = living_count(divisions, TEAM_PLAYER)
    n_rouge = living_count(divisions, TEAM_ENEMY)
    p_name = COUNTRIES[player_country]["name"]
    e_name = COUNTRIES[enemy_country]["name"]
    title = font.render(
        f"{p_name} vs {e_name} — {scenario_label(scenario)}",
        True,
        (230, 220, 180),
    )
    surface.blit(title, (12, MAP_H + 8))

    if phase == PHASE_END and winner:
        hint = font.render(
            f"{winner.upper()} — R = menu  |  Echap = quitter",
            True,
            (255, 220, 120) if winner == "victoire" else (255, 140, 120),
        )
    elif phase == PHASE_BATTLE:
        if scenario == SCENARIO_DEFENSIVE:
            battle_txt = f"DEFENSE — {p_name} {n_bleu}  |  {e_name} {n_rouge} attaque"
        else:
            battle_txt = f"OFFENSIVE — {p_name} {n_bleu}  |  {e_name} {n_rouge}"
        hint = font.render(battle_txt, True, (200, 160, 140))
    else:
        tool = place_tool_label(place_kind, place_weapon)
        if scenario == SCENARIO_DEFENSIVE:
            prep_txt = (
                f"Arme: {tool}  |  [F] fusil [G] MG [C] char  |  "
                f"Clic placer ({n_bleu}/{MAX_PLAYER_DIVISIONS})  |  Espace = attaque"
            )
        else:
            prep_txt = (
                f"Arme: {tool}  |  [F] [G] [C]  |  Clic ({n_bleu}/{MAX_PLAYER_DIVISIONS})  |  Espace = offensive"
            )
        hint = font.render(prep_txt, True, (150, 155, 140))
    surface.blit(hint, (12, MAP_H + 30))


def scenario_menu_rect(index):
    y = 200 + index * 78
    return pygame.Rect(WIDTH // 2 - 180, y, 360, 62).inflate(8, 8)


def country_menu_rect(index):
    col = index % 2
    row = index // 2
    w, h = 400, 54
    x = WIDTH // 2 - 410 + col * (w + 20)
    y = 128 + row * (h + 10)
    return pygame.Rect(x, y, w, h)


# Couleurs historiques (1914-1916)
FLAG_FR_BLUE = (0, 35, 149)
FLAG_FR_WHITE = (255, 255, 255)
FLAG_FR_RED = (237, 41, 57)
FLAG_UK_BLUE = (1, 33, 105)
FLAG_UK_RED = (200, 16, 46)
FLAG_UK_WHITE = (255, 255, 255)
FLAG_BE_BLACK = (0, 0, 0)
FLAG_BE_YELLOW = (253, 218, 36)
FLAG_BE_RED = (239, 51, 64)
FLAG_RS_RED = (198, 54, 60)
FLAG_RS_BLUE = (12, 64, 118)
FLAG_RS_WHITE = (255, 255, 255)
FLAG_RU_WHITE = (255, 255, 255)
FLAG_RU_BLUE = (0, 57, 166)
FLAG_RU_RED = (213, 43, 30)
FLAG_IT_GREEN = (0, 146, 70)
FLAG_IT_RED = (206, 43, 55)
FLAG_RO_BLUE = (0, 43, 127)
FLAG_RO_YELLOW = (252, 209, 22)
FLAG_RO_RED = (206, 17, 38)
FLAG_DE_BLACK = (0, 0, 0)
FLAG_DE_RED = (221, 0, 0)
FLAG_AH_RED = (200, 0, 0)
FLAG_AH_GOLD = (255, 205, 0)
FLAG_OTT_RED = (227, 10, 23)


def _tricolor_vertical(surface, r, left, mid, right):
    third = r.width // 3
    pygame.draw.rect(surface, left, (r.x, r.y, third, r.height))
    pygame.draw.rect(surface, mid, (r.x + third, r.y, third, r.height))
    pygame.draw.rect(surface, right, (r.x + 2 * third, r.y, r.width - 2 * third, r.height))


def _tricolor_horizontal(surface, r, top, mid, bot):
    h3 = r.height // 3
    pygame.draw.rect(surface, top, (r.x, r.y, r.width, h3))
    pygame.draw.rect(surface, mid, (r.x, r.y + h3, r.width, h3))
    pygame.draw.rect(surface, bot, (r.x, r.y + 2 * h3, r.width, r.height - 2 * h3))


def _star_polygon(cx, cy, outer_r, inner_ratio=0.4):
    points = []
    for i in range(10):
        ang = math.radians(-90 + i * 36)
        dist = outer_r if i % 2 == 0 else outer_r * inner_ratio
        points.append((cx + math.cos(ang) * dist, cy + math.sin(ang) * dist))
    return points


def _draw_crescent_star(surface, cx, cy, scale, bg_color):
    """Croissant et étoile ottomans (modèle 1844-1923)."""
    white = (255, 255, 255)
    r_out = int(11 * scale)
    r_in = int(9 * scale)
    offset = int(4 * scale)
    pygame.draw.circle(surface, white, (cx, cy), r_out)
    pygame.draw.circle(surface, bg_color, (cx + offset, cy), r_in)
    star_x = cx + int(14 * scale)
    star_y = cy - int(1 * scale)
    pygame.draw.polygon(surface, white, _star_polygon(star_x, star_y, 5 * scale))


def _draw_union_jack(surface, r):
    """Union Jack du Royaume-Uni (1801, identique en 1914)."""
    pygame.draw.rect(surface, FLAG_UK_BLUE, r)
    cx, cy = r.centerx, r.centery
    t = max(2, r.width // 6)

    # Saint-André (saltire blanc)
    pygame.draw.line(surface, FLAG_UK_WHITE, (r.x, r.y), (r.right, r.bottom), t)
    pygame.draw.line(surface, FLAG_UK_WHITE, (r.right, r.y), (r.x, r.bottom), t)

    # Saint-Patrick (saltire rouge, décalé — simplifié au centre)
    rt = max(1, t // 2)
    pygame.draw.line(surface, FLAG_UK_RED, (r.x + 2, r.y), (r.right - 2, r.bottom), rt)
    pygame.draw.line(surface, FLAG_UK_RED, (r.right - 2, r.y), (r.x + 2, r.bottom), rt)

    # Saint-Georges (croix rouge bordée de blanc)
    wt = max(2, r.width // 5)
    rt2 = max(1, wt // 2)
    pygame.draw.rect(surface, FLAG_UK_WHITE, (r.x, cy - wt // 2, r.width, wt))
    pygame.draw.rect(surface, FLAG_UK_WHITE, (cx - wt // 2, r.y, wt, r.height))
    pygame.draw.rect(surface, FLAG_UK_RED, (r.x, cy - rt2, r.width, rt2 * 2))
    pygame.draw.rect(surface, FLAG_UK_RED, (cx - rt2, r.y, rt2 * 2, r.height))


def _draw_serbian_eagle(surface, cx, cy, scale):
    """Petit blason serbe (aigle bicéphale blanc sur écusson rouge)."""
    shield_w = int(14 * scale)
    shield_h = int(16 * scale)
    sh = pygame.Rect(cx - shield_w // 2, cy - shield_h // 2, shield_w, shield_h)
    pygame.draw.rect(surface, FLAG_RS_RED, sh, border_radius=2)
    pygame.draw.rect(surface, (180, 140, 40), sh, 1, border_radius=2)
    # Aigle simplifié
    body = pygame.Rect(cx - 3, cy - 2, 6, 8)
    pygame.draw.ellipse(surface, FLAG_RS_WHITE, body)
    pygame.draw.circle(surface, FLAG_RS_WHITE, (cx - 5, cy - 5), 3)
    pygame.draw.circle(surface, FLAG_RS_WHITE, (cx + 5, cy - 5), 3)
    pygame.draw.circle(surface, FLAG_RS_RED, (cx - 5, cy - 5), 1)
    pygame.draw.circle(surface, FLAG_RS_RED, (cx + 5, cy - 5), 1)
    # Petite croix sur le bouclier
    pygame.draw.line(surface, (180, 140, 40), (cx, cy - 4), (cx, cy + 2), 1)
    pygame.draw.line(surface, (180, 140, 40), (cx - 2, cy - 1), (cx + 2, cy - 1), 1)


def _draw_austria_hungary_arms(surface, cx, cy, scale):
    """Blason dual monarchique simplifié (Autriche + Hongrie)."""
    w = int(18 * scale)
    h = int(14 * scale)
    left = pygame.Rect(cx - w // 2, cy - h // 2, w // 2, h)
    right = pygame.Rect(cx, cy - h // 2, w // 2, h)
    # Autriche : bandes rouge-blanc-rouge
    for i, col in enumerate([FLAG_AH_RED, FLAG_FR_WHITE, FLAG_AH_RED]):
        pygame.draw.rect(surface, col, (left.x, left.y + i * h // 3, left.width, h // 3))
    # Hongrie : rouge-blanc-vert horizontal
    hu = [(200, 0, 0), (255, 255, 255), (0, 120, 60)]
    for i, col in enumerate(hu):
        pygame.draw.rect(surface, col, (right.x, right.y + i * h // 3, right.width, h // 3))
    pygame.draw.rect(surface, (120, 90, 20), (cx - w // 2, cy - h // 2, w, h), 1)
    # Couronne impériale simplifiée au-dessus
    crown = pygame.Rect(cx - 4, cy - h // 2 - 4, 8, 4)
    pygame.draw.rect(surface, FLAG_AH_GOLD, crown)
    pygame.draw.polygon(surface, FLAG_AH_GOLD, [(cx - 6, cy - h // 2 - 4), (cx, cy - h // 2 - 8), (cx + 6, cy - h // 2 - 4)])


def draw_flag(surface, rect, country_id):
    """Drapeaux historiques de la Grande Guerre (1914-1916)."""
    r = rect.inflate(-4, -4)
    pygame.draw.rect(surface, (30, 30, 28), r, 1, border_radius=1)
    scale = max(0.6, min(r.width, r.height) / 38.0)
    cx, cy = r.centerx, r.centery

    if country_id == COUNTRY_FRANCE:
        # Tricolore vertical (depuis 1794)
        _tricolor_vertical(surface, r, FLAG_FR_BLUE, FLAG_FR_WHITE, FLAG_FR_RED)

    elif country_id == COUNTRY_UK:
        _draw_union_jack(surface, r)

    elif country_id == COUNTRY_BELGIUM:
        # Tricolore vertical (depuis 1831)
        _tricolor_vertical(surface, r, FLAG_BE_BLACK, FLAG_BE_YELLOW, FLAG_BE_RED)

    elif country_id == COUNTRY_SERBIA:
        # Royaume de Serbie : triband horizontal + blason
        _tricolor_horizontal(surface, r, FLAG_RS_RED, FLAG_RS_BLUE, FLAG_RS_WHITE)
        _draw_serbian_eagle(surface, cx, cy, scale)

    elif country_id == COUNTRY_RUSSIA:
        # Empire russe : blanc-bleu-rouge horizontal (1858-1917)
        _tricolor_horizontal(surface, r, FLAG_RU_WHITE, FLAG_RU_BLUE, FLAG_RU_RED)

    elif country_id == COUNTRY_ITALY:
        # Royaume d'Italie : vert-blanc-rouge vertical (1848)
        _tricolor_vertical(surface, r, FLAG_IT_GREEN, FLAG_FR_WHITE, FLAG_IT_RED)

    elif country_id == COUNTRY_ROMANIA:
        # Bleu-jaune-rouge vertical (1881)
        _tricolor_vertical(surface, r, FLAG_RO_BLUE, FLAG_RO_YELLOW, FLAG_RO_RED)

    elif country_id == COUNTRY_GERMANY:
        # Empire allemand : noir-blanc-rouge horizontal (1871-1918)
        _tricolor_horizontal(surface, r, FLAG_DE_BLACK, FLAG_FR_WHITE, FLAG_DE_RED)

    elif country_id == COUNTRY_AUSTRIA:
        # Autriche-Hongrie : triband rouge-blanc-rouge + blason dual
        _tricolor_horizontal(surface, r, FLAG_AH_RED, FLAG_FR_WHITE, FLAG_AH_RED)
        _draw_austria_hungary_arms(surface, cx, cy, scale)

    elif country_id == COUNTRY_OTTOMAN:
        # Empire ottoman : champ rouge, croissant et étoile blancs
        pygame.draw.rect(surface, FLAG_OTT_RED, r)
        _draw_crescent_star(surface, cx - int(4 * scale), cy, scale, FLAG_OTT_RED)


def country_key_for_index(index):
    if index < 9:
        return getattr(pygame, f"K_{index + 1}")
    return pygame.K_0


def run_country_menu(screen, font, clock, title_text, subtitle_text):
    """Choix d'un pays (drapeau + année). Retourne l'id pays ou None."""
    title_font = pygame.font.SysFont(None, 40)
    small = pygame.font.SysFont(None, 18)

    while True:
        screen.fill((14, 16, 14))
        title = title_font.render(title_text, True, (235, 228, 200))
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 52))
        sub = font.render(subtitle_text, True, (150, 155, 140))
        screen.blit(sub, (WIDTH // 2 - sub.get_width() // 2, 92))

        for i, cid in enumerate(COUNTRY_MENU_ORDER):
            info = COUNTRIES[cid]
            rect = country_menu_rect(i)
            inner = rect.inflate(-4, -4)
            pygame.draw.rect(screen, (42, 48, 38), inner, border_radius=6)
            pygame.draw.rect(screen, (100, 115, 85), inner, 2, border_radius=6)

            flag_rect = pygame.Rect(inner.x + 10, inner.y + 8, 64, 38)
            draw_flag(screen, flag_rect, cid)

            key_num = (i + 1) % 10
            key_label = "0" if key_num == 0 else str(key_num)
            label = font.render(
                f"[{key_label}] {info['name']}  —  {info['year']}",
                True,
                (230, 235, 220),
            )
            screen.blit(label, (inner.x + 84, inner.y + 16))

        hint = small.render(
            "Touches 1-0 ou clic  |  Echap = quitter",
            True,
            (130, 130, 125),
        )
        screen.blit(hint, (WIDTH // 2 - hint.get_width() // 2, HEIGHT - 44))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return None
                for i, cid in enumerate(COUNTRY_MENU_ORDER):
                    if event.key == country_key_for_index(i):
                        return cid
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos
                for i, cid in enumerate(COUNTRY_MENU_ORDER):
                    if country_menu_rect(i).collidepoint(mx, my):
                        return cid
        clock.tick(30)


def run_game_setup(screen, font, clock):
    """Scenario puis ton pays puis l'ennemi."""
    scenario = run_scenario_menu(screen, font, clock)
    if scenario is None:
        return None

    player_country = run_country_menu(
        screen,
        font,
        clock,
        "Choisis TON pays",
        f"Mode : {scenario_label(scenario)}  —  1914 a 1916",
    )
    if player_country is None:
        return None

    enemy_country = run_country_menu(
        screen,
        font,
        clock,
        "Choisis le pays ENNEMI",
        f"Tu joues : {COUNTRIES[player_country]['name']}",
    )
    if enemy_country is None:
        return None

    return scenario, player_country, enemy_country


def run_scenario_menu(screen, font, clock):
    """Menu : offensive ou defensive. Retourne le mode ou None."""
    title_font = pygame.font.SysFont(None, 44)
    choices = [
        (
            SCENARIO_OFFENSIVE,
            "1 — SCENARIO OFFENSIF",
            "Tu attaques : tes divisions avancent vers l'est",
        ),
        (
            SCENARIO_DEFENSIVE,
            "2 — SCENARIO DEFENSIF",
            "Tu tiens la ligne : l'ennemi attaque, tu ne bouges pas",
        ),
    ]

    while True:
        screen.fill((14, 16, 14))
        title = title_font.render("HOI4 — Choisis ton scenario", True, (235, 228, 200))
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 90))

        for i, (_, label, desc) in enumerate(choices):
            rect = scenario_menu_rect(i)
            inner = rect.inflate(-8, -8)
            pygame.draw.rect(screen, (42, 48, 38), inner, border_radius=8)
            pygame.draw.rect(screen, (100, 115, 85), inner, 2, border_radius=8)
            screen.blit(font.render(label, True, (230, 235, 220)), (inner.x + 14, inner.y + 10))
            screen.blit(font.render(desc, True, (150, 155, 140)), (inner.x + 14, inner.y + 32))

        hint = font.render("1 / 2 ou clic  |  Echap = quitter", True, (130, 130, 125))
        screen.blit(hint, (WIDTH // 2 - hint.get_width() // 2, HEIGHT - 50))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return None
                if event.key == pygame.K_1:
                    return SCENARIO_OFFENSIVE
                if event.key == pygame.K_2:
                    return SCENARIO_DEFENSIVE
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos
                for i, (mode, _, _) in enumerate(choices):
                    if scenario_menu_rect(i).collidepoint(mx, my):
                        return mode
        clock.tick(30)


def new_game(scenario, player_country, enemy_country):
    grid = generate_battlefield()
    divisions = spawn_enemy_divisions(grid, scenario)
    return grid, divisions, PHASE_PREP, None, scenario, player_country, enemy_country


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("HOI4 — Mini bataille")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 22)

    setup = run_game_setup(screen, font, clock)
    if setup is None:
        pygame.quit()
        sys.exit(0)
    scenario, player_country, enemy_country = setup

    grid, divisions, phase, winner, scenario, player_country, enemy_country = new_game(
        scenario, player_country, enemy_country
    )
    battle_timer = 0
    place_kind = "infantry"
    place_weapon = WEAPON_RIFLE

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r and phase == PHASE_END:
                    setup = run_game_setup(screen, font, clock)
                    if setup is None:
                        running = False
                    else:
                        scenario, player_country, enemy_country = setup
                        grid, divisions, phase, winner, scenario, player_country, enemy_country = (
                            new_game(scenario, player_country, enemy_country)
                        )
                        battle_timer = 0
                elif event.key == pygame.K_TAB and phase == PHASE_END:
                    setup = run_game_setup(screen, font, clock)
                    if setup:
                        scenario, player_country, enemy_country = setup
                        grid, divisions, phase, winner, scenario, player_country, enemy_country = (
                            new_game(scenario, player_country, enemy_country)
                        )
                        battle_timer = 0
                elif event.key == pygame.K_SPACE and phase == PHASE_PREP:
                    if living_count(divisions, TEAM_PLAYER) > 0:
                        phase = PHASE_BATTLE
                        battle_timer = 0
                elif phase == PHASE_PREP:
                    if event.key == pygame.K_f:
                        place_kind = "infantry"
                        place_weapon = WEAPON_RIFLE
                    elif event.key == pygame.K_g:
                        place_kind = "infantry"
                        place_weapon = WEAPON_MG
                    elif event.key in (pygame.K_c, pygame.K_e):
                        place_kind = "armor"
                        place_weapon = WEAPON_CANNON
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if phase == PHASE_PREP:
                    try_place_player(
                        divisions, grid, *event.pos, place_kind, place_weapon
                    )

        if phase == PHASE_BATTLE:
            battle_timer += 1
            if battle_timer >= BATTLE_TICK_INTERVAL:
                battle_timer = 0
                battle_tick(divisions, grid, scenario)
                result = check_winner(divisions)
                if result:
                    phase = PHASE_END
                    winner = result

        refresh_trench_status(divisions, grid)

        screen.fill(COLOR_BG)
        draw_map(screen, grid)
        draw_headquarters(screen, player_country, enemy_country)
        draw_shot_tracers(screen, divisions)
        draw_divisions(screen, divisions, player_country, enemy_country)
        draw_hud(
            screen,
            font,
            divisions,
            phase,
            winner,
            scenario,
            place_kind,
            place_weapon,
            player_country,
            enemy_country,
        )
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit(0)


if __name__ == "__main__":
    main()
