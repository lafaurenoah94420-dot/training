"""
Bataille de Tsushima (1905) — flottes japonaise vs russe
Mer, manœuvres, tir de bord (broadside), îles du détroit.
"""

import math
import random
import sys

import pygame

CELL = 22
COLS = 46
ROWS = 26
MAP_H = ROWS * CELL
HUD_H = 72
WIDTH = COLS * CELL
HEIGHT = MAP_H + HUD_H
MID_ROW = ROWS // 2

WATER = 0
SHALLOW = 1
ISLAND = 2

TERRAIN_COLORS = {
    WATER: (28, 72, 118),
    SHALLOW: (38, 98, 142),
    ISLAND: (92, 108, 72),
}

COLOR_BG = (12, 28, 48)
COLOR_HUD = (16, 32, 52)
COLOR_WAKE = (120, 180, 220)

TEAM_PLAYER = "player"
TEAM_ENEMY = "enemy"
MAX_PLAYER_SHIPS = 12

FACING_N = 0
FACING_E = 1
FACING_S = 2
FACING_W = 3
FACING_NAMES = ("N", "E", "S", "O")

FORWARD = {FACING_N: (0, -1), FACING_E: (1, 0), FACING_S: (0, 1), FACING_W: (-1, 0)}
LEFT_TURN = {FACING_N: FACING_W, FACING_W: FACING_S, FACING_S: FACING_E, FACING_E: FACING_N}
RIGHT_TURN = {FACING_N: FACING_E, FACING_E: FACING_S, FACING_S: FACING_W, FACING_W: FACING_N}

SHIP_BATTLESHIP = "cuirasse"
SHIP_CRUISER = "croiseur"
SHIP_TORPEDO = "torpilleur"

SHIP_STATS = {
    SHIP_BATTLESHIP: {"hp": 20, "range": 6, "damage": 9, "speed": 1, "label": "CUIRASSE"},
    SHIP_CRUISER: {"hp": 13, "range": 5, "damage": 6, "speed": 2, "label": "CROISEUR"},
    SHIP_TORPEDO: {"hp": 7, "range": 3, "damage": 10, "speed": 3, "label": "TORPILLEUR"},
}

BATTLE_TICK_INTERVAL = 18
PHASE_PREP = "prep"
PHASE_BATTLE = "battle"
PHASE_END = "end"

COUNTRY_JAPAN = "japan"
COUNTRY_RUSSIA = "russia"

COUNTRIES = {
    COUNTRY_JAPAN: {
        "name": "Japon",
        "fill": (180, 48, 42),
        "border": (120, 28, 24),
        "accent": (240, 240, 230),
    },
    COUNTRY_RUSSIA: {
        "name": "Russie",
        "fill": (58, 88, 148),
        "border": (38, 58, 98),
        "accent": (220, 180, 60),
    },
}


def generate_sea():
    """Détroit de Tsushima : eau, bas-fonds, îles au centre."""
    grid = [[WATER for _ in range(COLS)] for _ in range(ROWS)]

    for y in range(ROWS):
        for x in range(COLS):
            if random.random() < 0.08 and 4 < y < ROWS - 5:
                grid[y][x] = SHALLOW

    # Îles sur les côtés — couloir central libre pour les flottes
    islands = [
        (8, 11, 3, 3),
        (8, 18, 3, 2),
        (COLS - 9, 10, 3, 3),
        (COLS - 9, 17, 3, 2),
    ]
    for cx, cy, w, h in islands:
        for y in range(max(1, cy - h), min(ROWS - 1, cy + h + 1)):
            for x in range(max(1, cx - w), min(COLS - 1, cx + w + 1)):
                if (x - cx) ** 2 + (y - cy) ** 2 < (w * h * 0.5):
                    grid[y][x] = ISLAND

    for x in range(COLS):
        grid[0][x] = SHALLOW
        grid[ROWS - 1][x] = SHALLOW
    return grid


def cell_center(gx, gy):
    return gx * CELL + CELL // 2, gy * CELL + CELL // 2


def pos_to_cell(mx, my):
    if my >= MAP_H or mx < 0 or my < 0 or mx >= WIDTH:
        return None
    return mx // CELL, my // CELL


def is_water(grid, gx, gy):
    if not (0 <= gx < COLS and 0 <= gy < ROWS):
        return False
    return grid[gy][gx] != ISLAND


def ship_at(ships, gx, gy):
    for s in ships:
        if s["gx"] == gx and s["gy"] == gy and s["hp"] > 0:
            return s
    return None


def player_deploys_south(player_country):
    return player_country == COUNTRY_JAPAN


def can_place_ship(grid, ships, gx, gy, team, player_country):
    if ship_at(ships, gx, gy):
        return False
    if not is_water(grid, gx, gy):
        return False
    south = player_deploys_south(player_country)
    if team == TEAM_PLAYER:
        if south and gy <= MID_ROW + 1:
            return False
        if not south and gy >= MID_ROW - 1:
            return False
    else:
        if south and gy >= MID_ROW - 1:
            return False
        if not south and gy <= MID_ROW + 1:
            return False
    return True


def new_ship(gx, gy, team, kind, facing=FACING_N):
    stats = SHIP_STATS[kind]
    return {
        "gx": gx,
        "gy": gy,
        "team": team,
        "kind": kind,
        "facing": facing,
        "hp": stats["hp"],
        "max_hp": stats["hp"],
        "shoot_flash": 0,
        "shot_gx": None,
        "shot_gy": None,
        "wake": [],
        "smoke": 0,
        "stuck": 0,
    }


def spawn_enemy_fleet(grid, player_country):
    ships = []
    south_player = player_deploys_south(player_country)
    base_y = 4 if south_player else ROWS - 5
    facing = FACING_S if south_player else FACING_N

    line_x = [8, 14, 20, 26, 32, 38]
    for i, gx in enumerate(line_x):
        kind = SHIP_BATTLESHIP if i % 3 == 0 else SHIP_CRUISER
        gy = base_y + (i % 3) * 2
        if can_place_ship(grid, ships, gx, gy, TEAM_ENEMY, player_country):
            ships.append(new_ship(gx, gy, TEAM_ENEMY, kind, facing))

    for gx in (12, 22, 34):
        gy = base_y + 5
        if can_place_ship(grid, ships, gx, gy, TEAM_ENEMY, player_country):
            ships.append(new_ship(gx, gy, TEAM_ENEMY, SHIP_TORPEDO, facing))

    reserve_y = base_y + 7
    for gx in (18, 28):
        if can_place_ship(grid, ships, gx, reserve_y, TEAM_ENEMY, player_country):
            ships.append(new_ship(gx, reserve_y, TEAM_ENEMY, SHIP_CRUISER, facing))

    return ships


def in_broadside_arc(ship, tx, ty):
    """Cible dans l'arc de tir perpendiculaire à la proue."""
    stats = SHIP_STATS[ship["kind"]]
    dx = tx - ship["gx"]
    dy = ty - ship["gy"]
    dist = math.hypot(dx, dy)
    if dist < 1 or dist > stats["range"]:
        return False
    f = ship["facing"]
    if f in (FACING_N, FACING_S):
        return abs(dx) > abs(dy) * 0.6
    return abs(dy) > abs(dx) * 0.6


def crossing_the_t_bonus(attacker, target):
    """Bonus si on tire sur la proue ou la poupe ennemie (enfilade)."""
    dx = target["gx"] - attacker["gx"]
    dy = target["gy"] - attacker["gy"]
    tf = target["facing"]
    fwd = FORWARD[tf]
    dot = dx * fwd[0] + dy * fwd[1]
    if abs(dot) >= max(abs(dx), abs(dy)) * 0.7:
        return 1.5
    return 1.0


def find_shot_target(ship, ships):
    best = None
    best_score = -1
    for other in ships:
        if other["team"] == ship["team"] or other["hp"] <= 0:
            continue
        if not in_broadside_arc(ship, other["gx"], other["gy"]):
            continue
        score = SHIP_STATS[ship["kind"]]["damage"] * crossing_the_t_bonus(ship, other)
        score += (SHIP_STATS[other["kind"]]["hp"] - other["hp"]) * 0.1
        if score > best_score:
            best_score = score
            best = other
    return best


def can_sail_to(grid, ships, ship, nx, ny):
    if not is_water(grid, nx, ny):
        return False
    occupant = ship_at(ships, nx, ny)
    return occupant is None or occupant is ship


def manhattan_dist(gx, gy, tx, ty):
    return abs(tx - gx) + abs(ty - gy)


def forward_cell(ship):
    dx, dy = FORWARD[ship["facing"]]
    return ship["gx"] + dx, ship["gy"] + dy


def valid_facings(ship, grid, ships):
    options = []
    for facing in (FACING_N, FACING_E, FACING_S, FACING_W):
        dx, dy = FORWARD[facing]
        nx, ny = ship["gx"] + dx, ship["gy"] + dy
        if can_sail_to(grid, ships, ship, nx, ny):
            options.append(facing)
    return options


def choose_best_facing(ship, grid, ships, tx, ty):
    """Choisit un cap où le navire peut avancer et se rapproche de la cible."""
    options = valid_facings(ship, grid, ships)
    if not options:
        return ship["facing"]

    def score(facing):
        dx, dy = FORWARD[facing]
        nx, ny = ship["gx"] + dx, ship["gy"] + dy
        dist = manhattan_dist(nx, ny, tx, ty)
        if facing == ship["facing"]:
            dist -= 1
        return dist

    return min(options, key=score)


def turn_toward(ship, target_facing):
    if ship["facing"] == target_facing:
        return
    left = LEFT_TURN[ship["facing"]]
    right = RIGHT_TURN[ship["facing"]]
    ship["facing"] = left if left == target_facing else right


def try_move_ship(ship, grid, ships, nx, ny):
    if not can_sail_to(grid, ships, ship, nx, ny):
        return False
    ship["wake"].append((ship["gx"], ship["gy"]))
    if len(ship["wake"]) > 6:
        ship["wake"].pop(0)
    ship["gx"] = nx
    ship["gy"] = ny
    ship["stuck"] = 0
    return True


def navigate_ship(ship, grid, ships, tx, ty):
    """Avance en contournant îles et navires amis."""
    speed = SHIP_STATS[ship["kind"]]["speed"]
    moved = False

    for _ in range(speed):
        nx, ny = forward_cell(ship)
        if can_sail_to(grid, ships, ship, nx, ny):
            try_move_ship(ship, grid, ships, nx, ny)
            moved = True
            continue

        ship["stuck"] += 1
        best = choose_best_facing(ship, grid, ships, tx, ty)
        if best != ship["facing"]:
            turn_toward(ship, best)
            nx, ny = forward_cell(ship)
            if can_sail_to(grid, ships, ship, nx, ny):
                try_move_ship(ship, grid, ships, nx, ny)
                moved = True
            break

        turn_toward(ship, LEFT_TURN[ship["facing"]])
        break

    if not moved:
        ship["stuck"] += 1
        if ship["stuck"] >= 2:
            best = choose_best_facing(ship, grid, ships, tx, ty)
            turn_toward(ship, best)


def battle_tick(ships, grid):
    order = sorted(ships, key=lambda s: (-SHIP_STATS[s["kind"]]["speed"], random.random()))
    for ship in order:
        if ship["hp"] <= 0:
            continue

        target = find_shot_target(ship, ships)
        if target:
            dmg = int(SHIP_STATS[ship["kind"]]["damage"] * crossing_the_t_bonus(ship, target))
            target["hp"] -= dmg
            target["smoke"] = min(30, target["smoke"] + 4)
            ship["shoot_flash"] = 10
            ship["shot_gx"] = target["gx"]
            ship["shot_gy"] = target["gy"]
            continue

        enemies = [s for s in ships if s["team"] != ship["team"] and s["hp"] > 0]
        if not enemies:
            continue

        ex = sum(e["gx"] for e in enemies) // len(enemies)
        ey = sum(e["gy"] for e in enemies) // len(enemies)

        best = choose_best_facing(ship, grid, ships, ex, ey)
        if best != ship["facing"]:
            turn_toward(ship, best)
            continue

        navigate_ship(ship, grid, ships, ex, ey)


def living_count(ships, team):
    return sum(1 for s in ships if s["team"] == team and s["hp"] > 0)


def check_winner(ships):
    if living_count(ships, TEAM_ENEMY) == 0:
        return "victoire"
    if living_count(ships, TEAM_PLAYER) == 0:
        return "defaite"
    return None


def try_place_player(ships, grid, mx, my, kind, facing, player_country):
    if living_count(ships, TEAM_PLAYER) >= MAX_PLAYER_SHIPS:
        return False
    cell = pos_to_cell(mx, my)
    if not cell:
        return False
    gx, gy = cell
    if not can_place_ship(grid, ships, gx, gy, TEAM_PLAYER, player_country):
        return False
    ships.append(new_ship(gx, gy, TEAM_PLAYER, kind, facing))
    return True


def wave_color(base, x, y, tick):
    wave = math.sin((x * 0.35 + y * 0.25 + tick * 0.04)) * 8
    return tuple(max(0, min(255, c + int(wave))) for c in base)


def draw_water_cell(surface, x, y, terrain, tick):
    rect = pygame.Rect(x * CELL, y * CELL, CELL, CELL)
    base = TERRAIN_COLORS[terrain]
    color = wave_color(base, x, y, tick)
    pygame.draw.rect(surface, color, rect)

    if terrain == WATER:
        if (x + y + tick // 8) % 7 == 0:
            pygame.draw.line(
                surface,
                (180, 220, 255),
                (rect.left + 3, rect.centery),
                (rect.right - 3, rect.centery - 1),
                1,
            )
    elif terrain == SHALLOW:
        pygame.draw.circle(surface, (200, 230, 255), (rect.centerx, rect.centery), 2, 1)
    elif terrain == ISLAND:
        pygame.draw.ellipse(surface, (72, 88, 58), rect.inflate(-4, -6))
        if (x + y) % 3 == 0:
            pygame.draw.circle(surface, (58, 78, 48), (rect.centerx + 2, rect.centery - 2), 2)

    pygame.draw.rect(surface, (18, 40, 68), rect, 1)


def draw_map(surface, grid, tick):
    for y in range(ROWS):
        for x in range(COLS):
            draw_water_cell(surface, x, y, grid[y][x], tick)

    font = pygame.font.SysFont(None, 20)
    label = font.render("DETROIT DE TSUSHIMA", True, (180, 210, 240))
    surface.blit(label, (WIDTH // 2 - label.get_width() // 2, 8))


def draw_wake(surface, ship):
    for i, (wx, wy) in enumerate(ship["wake"]):
        cx, cy = cell_center(wx, wy)
        alpha = 40 + i * 20
        pygame.draw.circle(surface, COLOR_WAKE, (cx, cy), 3 + i // 2)
        _ = alpha


def draw_ship_hull(surface, ship, country_id):
    cx, cy = cell_center(ship["gx"], ship["gy"])
    info = COUNTRIES[country_id]
    fill, border, accent = info["fill"], info["border"], info["accent"]
    f = ship["facing"]

    kind = ship["kind"]
    if kind == SHIP_BATTLESHIP:
        length, width = 16, 10
    elif kind == SHIP_CRUISER:
        length, width = 13, 8
    else:
        length, width = 10, 6

    if f in (FACING_E, FACING_W):
        hull = pygame.Rect(cx - length // 2, cy - width // 2, length, width)
    else:
        hull = pygame.Rect(cx - width // 2, cy - length // 2, width, length)

    pygame.draw.rect(surface, fill, hull, border_radius=3)
    pygame.draw.rect(surface, border, hull, 2, border_radius=3)

    # cheminées
    stack_color = (48, 48, 52)
    if f == FACING_E:
        pygame.draw.rect(surface, stack_color, (cx - 4, cy - 5, 4, 6))
        pygame.draw.rect(surface, stack_color, (cx + 1, cy - 4, 3, 5))
        pygame.draw.line(surface, accent, (cx + 8, cy - 2), (cx + 14, cy - 4), 3)
        pygame.draw.line(surface, accent, (cx + 8, cy + 2), (cx + 14, cy + 4), 3)
    elif f == FACING_W:
        pygame.draw.rect(surface, stack_color, (cx - 1, cy - 5, 4, 6))
        pygame.draw.rect(surface, stack_color, (cx - 6, cy - 4, 3, 5))
        pygame.draw.line(surface, accent, (cx - 8, cy - 2), (cx - 14, cy - 4), 3)
        pygame.draw.line(surface, accent, (cx - 8, cy + 2), (cx - 14, cy + 4), 3)
    elif f == FACING_S:
        pygame.draw.rect(surface, stack_color, (cx - 5, cy - 4, 6, 4))
        pygame.draw.line(surface, accent, (cx - 2, cy + 6), (cx - 4, cy + 12), 3)
        pygame.draw.line(surface, accent, (cx + 2, cy + 6), (cx + 4, cy + 12), 3)
    else:
        pygame.draw.rect(surface, stack_color, (cx - 5, cy - 1, 6, 4))
        pygame.draw.line(surface, accent, (cx - 2, cy - 6), (cx - 4, cy - 12), 3)
        pygame.draw.line(surface, accent, (cx + 2, cy - 6), (cx + 4, cy - 12), 3)

    if ship.get("smoke", 0) > 0:
        for ox in (-6, 0, 6):
            pygame.draw.circle(
                surface,
                (120, 120, 120),
                (cx + ox, cy - 10 - ship["smoke"] // 3),
                4 + ship["smoke"] // 8,
            )

    if ship["hp"] < ship["max_hp"] * 0.4:
        pygame.draw.circle(surface, (255, 140, 60), (cx + 4, cy - 6), 3)


def draw_shot_effects(surface, ships):
    for s in ships:
        if s.get("shoot_flash", 0) <= 0 or s.get("shot_gx") is None:
            continue
        cx, cy = cell_center(s["gx"], s["gy"])
        tx, ty = cell_center(s["shot_gx"], s["shot_gy"])
        pygame.draw.line(surface, (255, 230, 120), (cx, cy), (tx, ty), 2)
        pygame.draw.circle(surface, (255, 180, 80), (tx, ty), 5)
        splash = pygame.Rect(tx - 8, ty - 4, 16, 8)
        pygame.draw.ellipse(surface, (200, 230, 255), splash, 2)


def draw_ships(surface, ships, player_country, enemy_country):
    for s in ships:
        if s["hp"] <= 0:
            continue
        cid = player_country if s["team"] == TEAM_PLAYER else enemy_country
        draw_wake(surface, s)
        draw_ship_hull(surface, s, cid)

        cx, cy = cell_center(s["gx"], s["gy"])
        font = pygame.font.SysFont(None, 16)
        hp_text = font.render(str(s["hp"]), True, (255, 252, 235))
        surface.blit(hp_text, (cx - hp_text.get_width() // 2, cy + 8))


def refresh_fx(ships):
    for s in ships:
        if s.get("shoot_flash", 0) > 0:
            s["shoot_flash"] -= 1
        if s.get("smoke", 0) > 0:
            s["smoke"] -= 1


def draw_hud(
    surface,
    font,
    ships,
    phase,
    winner,
    place_kind,
    place_facing,
    player_country,
    enemy_country,
):
    pygame.draw.rect(surface, COLOR_HUD, (0, MAP_H, WIDTH, HUD_H))
    pygame.draw.line(surface, (60, 100, 140), (0, MAP_H), (WIDTH, MAP_H), 2)

    p_name = COUNTRIES[player_country]["name"]
    e_name = COUNTRIES[enemy_country]["name"]
    p_count = living_count(ships, TEAM_PLAYER)
    e_count = living_count(ships, TEAM_ENEMY)

    if phase == PHASE_PREP:
        deploy = "sud" if player_deploys_south(player_country) else "nord"
        msg = (
            f"TSUSHIMA 1905 | {p_name} vs {e_name} | "
            f"1 cuirasse  2 croiseur  3 torpilleur  R tourner ({FACING_NAMES[place_facing]})  "
            f"clic placer ({SHIP_STATS[place_kind]['label']}) zone {deploy} | ESPACE lancer"
        )
    elif phase == PHASE_BATTLE:
        msg = f"BATAILLE NAVALE | {p_name}: {p_count} navires | {e_name}: {e_count} | tir de bord + enfilade"
    elif winner == "victoire":
        msg = f"VICTOIRE ! La flotte {p_name} contrôle le détroit."
    else:
        msg = f"DEFAITE. La flotte {e_name} domine la mer du Japon."

    text = font.render(msg, True, (210, 225, 240))
    surface.blit(text, (12, MAP_H + 10))

    sub = font.render(
        "Manœuvres : les navires tournent pour aligner leurs canons sur le flanc.",
        True,
        (140, 170, 200),
    )
    surface.blit(sub, (12, MAP_H + 38))


def run_country_menu(screen, font):
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return COUNTRY_JAPAN, COUNTRY_RUSSIA
                if event.key == pygame.K_2:
                    return COUNTRY_RUSSIA, COUNTRY_JAPAN

        screen.fill(COLOR_BG)
        lines = [
            "BATAILLE DE TSUSHIMA — 27 mai 1905",
            "",
            "Flotte combinée (Togo) vs flotte de la Baltique.",
            "Place ta flotte, puis regarde la bataille navale.",
            "",
            "1 — Jouer le Japon (deploie au sud)",
            "2 — Jouer la Russie (deploie au nord)",
        ]
        y = 80
        for line in lines:
            color = (240, 220, 160) if line.startswith("1") or line.startswith("2") else (200, 220, 240)
            t = font.render(line, True, color)
            screen.blit(t, (WIDTH // 2 - t.get_width() // 2, y))
            y += 36 if line == "" else 30

        pygame.display.flip()
        clock.tick(30)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tsushima 1905 — bataille navale")
    font = pygame.font.SysFont(None, 22)
    clock = pygame.time.Clock()

    player_country, enemy_country = run_country_menu(screen, font)

    grid = generate_sea()
    ships = spawn_enemy_fleet(grid, player_country)
    phase = PHASE_PREP
    winner = None
    place_kind = SHIP_CRUISER
    place_facing = FACING_N
    battle_timer = 0
    anim_tick = 0

    running = True
    while running:
        anim_tick += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif phase == PHASE_PREP:
                    if event.key == pygame.K_SPACE:
                        if living_count(ships, TEAM_PLAYER) > 0:
                            phase = PHASE_BATTLE
                    elif event.key == pygame.K_1:
                        place_kind = SHIP_BATTLESHIP
                    elif event.key == pygame.K_2:
                        place_kind = SHIP_CRUISER
                    elif event.key == pygame.K_3:
                        place_kind = SHIP_TORPEDO
                    elif event.key == pygame.K_r:
                        place_facing = RIGHT_TURN[place_facing]
                elif phase == PHASE_END and event.key == pygame.K_r:
                    grid = generate_sea()
                    ships = spawn_enemy_fleet(grid, player_country)
                    phase = PHASE_PREP
                    winner = None
                    place_kind = SHIP_CRUISER
                    place_facing = FACING_N
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if phase == PHASE_PREP:
                    try_place_player(
                        ships, grid, *event.pos, place_kind, place_facing, player_country
                    )

        if phase == PHASE_BATTLE:
            battle_timer += 1
            if battle_timer >= BATTLE_TICK_INTERVAL:
                battle_timer = 0
                battle_tick(ships, grid)
                result = check_winner(ships)
                if result:
                    phase = PHASE_END
                    winner = result

        refresh_fx(ships)

        screen.fill(COLOR_BG)
        draw_map(screen, grid, anim_tick)
        draw_shot_effects(screen, ships)
        draw_ships(screen, ships, player_country, enemy_country)
        draw_hud(
            screen,
            font,
            ships,
            phase,
            winner,
            place_kind,
            place_facing,
            player_country,
            enemy_country,
        )
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit(0)


if __name__ == "__main__":
    main()
