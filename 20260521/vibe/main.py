"""
Feu de forêt — simulation pygame (vibe 2026-05-21)
Carte + clic pour allumer + propagation du feu.
"""

import random
import sys

import pygame

CELL_SIZE = 14
COLS = 56
ROWS = 40
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE

GRASS = 0
TREE = 1
HOUSE = 2
ROCK = 3
POND = 4
FIRE = 5
BURNT = 6
ROAD = 7
SHOP = 8
HOSPITAL = 9
GARAGE = 10
SCHOOL = 11
BARRACKS = 12
BUNKER = 13
ARMORY = 14
COMMAND = 15
WATCHTOWER = 16
WALL = 17

CITY_BUILDINGS = {HOUSE, SHOP, HOSPITAL, GARAGE, SCHOOL}
MILITARY_BUILDINGS = {
    BARRACKS,
    BUNKER,
    ARMORY,
    COMMAND,
    WATCHTOWER,
    WALL,
    HOSPITAL,
    GARAGE,
}
BUILDINGS = CITY_BUILDINGS | MILITARY_BUILDINGS
FLAMMABLE = BUILDINGS | {GRASS, TREE, ROCK}

# Probabilité de base vers une case voisine
SPREAD_CHANCE = {
    GRASS: 0.26,
    TREE: 0.42,
    HOUSE: 0.09,
    ROCK: 0.14,
    SHOP: 0.08,
    HOSPITAL: 0.07,
    GARAGE: 0.1,
    SCHOOL: 0.09,
    BARRACKS: 0.08,
    BUNKER: 0.05,
    ARMORY: 0.11,
    COMMAND: 0.06,
    WATCHTOWER: 0.07,
    WALL: 0.04,
}
# Bonus si la flamme part d'un arbre (forêt plus inflammable)
TREE_FUEL_BOOST = 0.18

# Frames avant que la flamme devienne cendres
BURN_FRAMES = {
    GRASS: 14,
    TREE: 20,
    HOUSE: 32,
    ROCK: 22,
    SHOP: 28,
    HOSPITAL: 35,
    GARAGE: 26,
    SCHOOL: 30,
    BARRACKS: 28,
    BUNKER: 40,
    ARMORY: 30,
    COMMAND: 38,
    WATCHTOWER: 22,
    WALL: 18,
}

BOMB_RADIUS = 3
BOMB_KILL_RADIUS = BOMB_RADIUS * CELL_SIZE + 8

SPREAD_INTERVAL = 8
NEIGHBORS = ((0, 1), (0, -1), (1, 0), (-1, 0))

ZOMBIE_COUNT = 95
MAX_ZOMBIES_TOTAL = 200
SURVIVAL_PREP_SECONDS = 50
SURVIVAL_PREP_FRAMES = SURVIVAL_PREP_SECONDS * 60
SURVIVAL_INITIAL_HORDE = 140
SURVIVAL_SPAWN_INTERVAL = 10
SURVIVAL_SPAWN_PER_TICK = 5
MAX_ZOMBIES_SURVIVAL = 400
ZOMBIE_SPEED = 0.7
ZOMBIE_CHASE_SPEED = 0.95
ZOMBIE_BURN_DEATH = 45
ZOMBIE_HIT_RADIUS = 12
ZOMBIE_DETECT_MILITARY = 220
ZOMBIE_ATTACK_RANGE = 12
ZOMBIE_DAMAGE = 12
ZOMBIE_ATTACK_COOLDOWN = 35

SOLDIER_MAX_HP = 100

SOLDIER_SHOOT_RANGE = 48
SOLDIER_SHOOT_COOLDOWN = 20
SOLDIER_SPEED = 0.55
SOLDIER_RETREAT_DIST = 34
SOLDIER_POST_RETURN_DIST = 22
SOLDIER_ATTACK_PURSUE_DIST = 280
MAX_SOLDIERS = 25

VEHICLE_MAX_HP = 200
VEHICLE_SPEED = 0.45
VEHICLE_SHOOT_RANGE = 70
VEHICLE_RETREAT_DIST = 46
VEHICLE_POST_RETURN_DIST = 28
VEHICLE_ATTACK_PURSUE_DIST = 320
VEHICLE_SHOOT_COOLDOWN = 30
MAX_VEHICLES = 8

COLOR_BACKGROUND = (0, 0, 0)
COLOR_GRASS = (28, 72, 38)
COLOR_GRASS_ALT = (32, 78, 42)
COLOR_BASE_GROUND = (72, 75, 58)
COLOR_BASE_GROUND_ALT = (82, 85, 65)

current_map_type = "ville"
current_game_mode = "sandbox"


def new_burn_times():
    return [[0 for _ in range(COLS)] for _ in range(ROWS)]


def generate_world(map_type="ville"):
    grid = [[GRASS for _ in range(COLS)] for _ in range(ROWS)]
    if map_type == "base":
        for y in range(ROWS):
            for x in range(COLS):
                roll = random.random()
                if roll < 0.05:
                    grid[y][x] = TREE
                elif roll < 0.09:
                    grid[y][x] = ROCK
        build_base_roads(grid)
        seed_military_base(grid)
    else:
        for y in range(ROWS):
            for x in range(COLS):
                roll = random.random()
                if roll < 0.20:
                    grid[y][x] = TREE
                elif roll < 0.26:
                    grid[y][x] = ROCK
                elif roll < 0.30:
                    grid[y][x] = POND
        build_roads(grid)
        seed_city(grid)
    return grid


def is_building(state):
    return state in BUILDINGS


def place_building(grid, x, y, kind):
    if not (0 <= x < COLS and 0 <= y < ROWS):
        return
    if grid[y][x] in (GRASS, TREE):
        grid[y][x] = kind


def place_building_block(grid, x, y, kind, width=1, height=1):
    for oy in range(height):
        for ox in range(width):
            place_building(grid, x + ox, y + oy, kind)


def seed_military_base(grid):
    """Base militaire : QG, casernes, bunkers, tours, mur d'enceinte."""
    mid_x = COLS // 2
    mid_y = ROWS // 2

    place_building_block(grid, mid_x - 1, mid_y - 7, COMMAND, 2, 2)
    place_building_block(grid, mid_x + 3, mid_y - 7, HOSPITAL, 2, 1)
    place_building(grid, mid_x - 5, mid_y + 5, SHOP)

    for x in range(11, COLS - 12, 8):
        place_building_block(grid, x, mid_y + 3, BARRACKS, 2, 1)
        place_building_block(grid, x, mid_y - 4, BARRACKS, 2, 1)

    for y in range(11, ROWS - 12, 8):
        place_building_block(grid, mid_x + 4, y, BARRACKS, 1, 2)
        place_building_block(grid, mid_x - 6, y, BARRACKS, 1, 2)

    for x in range(16, COLS - 16, 7):
        if grid[mid_y + 2][x] in (GRASS, TREE):
            place_building(grid, x, mid_y + 2, ARMORY)
        if grid[mid_y - 3][x] in (GRASS, TREE):
            place_building(grid, x, mid_y - 3, GARAGE)

    for corner in ((9, 9), (COLS - 11, 9), (9, ROWS - 11), (COLS - 11, ROWS - 11)):
        place_building_block(grid, corner[0], corner[1], BUNKER, 2, 2)

    for x in range(11, COLS - 11, 9):
        place_building(grid, x, 6, WATCHTOWER)
        place_building(grid, x, ROWS - 7, WATCHTOWER)
    for y in range(11, ROWS - 11, 9):
        place_building(grid, 6, y, WATCHTOWER)
        place_building(grid, COLS - 7, y, WATCHTOWER)

    for x in range(5, COLS - 5):
        place_building(grid, x, 5, WALL)
        place_building(grid, x, ROWS - 6, WALL)
    for y in range(6, ROWS - 6):
        place_building(grid, 5, y, WALL)
        place_building(grid, COLS - 6, y, WALL)


def build_base_roads(grid):
    """Perimetre + grille interne + helipad au centre."""
    mid_x = COLS // 2
    mid_y = ROWS // 2
    margin = 4

    for x in range(margin, COLS - margin):
        set_road(grid, x, margin)
        set_road(grid, x, ROWS - 1 - margin)
    for y in range(margin, ROWS - margin):
        set_road(grid, margin, y)
        set_road(grid, COLS - 1 - margin, y)

    for x in range(margin + 7, COLS - margin, 7):
        carve_v_road(grid, x, margin + 1, ROWS - margin - 1)
    for y in range(margin + 7, ROWS - margin, 7):
        carve_h_road(grid, y, margin + 1, COLS - margin - 1)

    carve_h_road(grid, mid_y, mid_x - 3, mid_x + 3)
    carve_v_road(grid, mid_x, mid_y - 3, mid_y + 3)

    for y in range(ROWS):
        for x in range(COLS):
            if is_building(grid[y][x]):
                connect_house_to_network(grid, x, y, mid_x, mid_y)


def seed_city(grid):
    """Quartiers le long des routes : maisons, shops, hôpital, garage, école."""
    mid_x = COLS // 2
    mid_y = ROWS // 2
    kinds = [HOUSE, SHOP, HOSPITAL, GARAGE, SCHOOL]

    for x in range(6, COLS - 6, 3):
        for off in (2, -2, 3, -3):
            place_building(grid, x, mid_y + off, random.choice(kinds))

    for y in range(6, ROWS - 6, 3):
        for off in (2, -2, 3, -3):
            place_building(grid, mid_x + off, y, random.choice(kinds))

    for dx, dy in ((-4, -4), (4, -4), (-4, 4), (4, 4)):
        bx, by = mid_x + dx, mid_y + dy
        for ox in range(2):
            for oy in range(2):
                place_building(grid, bx + ox, by + oy, random.choice(kinds))


def set_road(grid, x, y):
    if not (0 <= x < COLS and 0 <= y < ROWS):
        return
    if grid[y][x] == POND or is_building(grid[y][x]):
        return
    grid[y][x] = ROAD


def carve_h_road(grid, y, x_start, x_end):
    for x in range(min(x_start, x_end), max(x_start, x_end) + 1):
        set_road(grid, x, y)


def carve_v_road(grid, x, y_start, y_end):
    for y in range(min(y_start, y_end), max(y_start, y_end) + 1):
        set_road(grid, x, y)


def connect_house_to_network(grid, hx, hy, mid_x, mid_y):
    """Route en L : maison → grande route horizontale → carrefour central."""
    carve_v_road(grid, hx, hy, mid_y)
    carve_h_road(grid, mid_y, hx, mid_x)


def build_roads(grid):
    """Croisement central (1 case) + raccord fin vers chaque maison."""
    mid_x = COLS // 2
    mid_y = ROWS // 2
    margin = 5

    carve_h_road(grid, mid_y, margin, COLS - 1 - margin)
    carve_v_road(grid, mid_x, margin, ROWS - 1 - margin)

    for y in range(ROWS):
        for x in range(COLS):
            if is_building(grid[y][x]):
                connect_house_to_network(grid, x, y, mid_x, mid_y)


def is_flammable(state):
    return state in FLAMMABLE


def spread_chance(source_origin, target_cell):
    """Plus de chances vers les arbres ; encore plus si on brûle déjà un arbre."""
    chance = SPREAD_CHANCE.get(target_cell, 0.2)
    if source_origin == TREE:
        chance += TREE_FUEL_BOOST
    return min(chance, 0.9)


def cell_rect(x, y):
    return pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)


def pos_to_cell(mx, my):
    x = mx // CELL_SIZE
    y = my // CELL_SIZE
    if 0 <= x < COLS and 0 <= y < ROWS:
        return x, y
    return None


def ignite(grid, burn_times, terrain_memory, x, y):
    state = grid[y][x]
    if not is_flammable(state):
        return False
    terrain_memory[y][x] = state
    grid[y][x] = FIRE
    burn_times[y][x] = 0
    return True


def update_fire(grid, burn_times, terrain_memory, tick):
    """Vieillissement des flammes + propagation."""
    to_ignite = []

    for y in range(ROWS):
        for x in range(COLS):
            if grid[y][x] != FIRE:
                continue
            burn_times[y][x] += 1
            origin = terrain_memory[y][x]
            limit = BURN_FRAMES.get(origin, 16)
            if burn_times[y][x] >= limit:
                grid[y][x] = BURNT
                burn_times[y][x] = 0

    if tick % SPREAD_INTERVAL != 0:
        return

    for y in range(ROWS):
        for x in range(COLS):
            if grid[y][x] != FIRE:
                continue
            source_origin = terrain_memory[y][x]
            for dy, dx in NEIGHBORS:
                ny, nx = y + dy, x + dx
                if not (0 <= nx < COLS and 0 <= ny < ROWS):
                    continue
                cell = grid[ny][nx]
                if not is_flammable(cell):
                    continue
                chance = spread_chance(source_origin, cell)
                if random.random() < chance:
                    to_ignite.append((nx, ny, cell))

    for nx, ny, origin in to_ignite:
        if grid[ny][nx] != FIRE:
            terrain_memory[ny][nx] = origin
            grid[ny][nx] = FIRE
            burn_times[ny][nx] = 0


def draw_grass(surface, x, y):
    if current_map_type == "base":
        base = COLOR_BASE_GROUND if (x + y) % 3 else COLOR_BASE_GROUND_ALT
    else:
        base = COLOR_GRASS if (x + y) % 3 else COLOR_GRASS_ALT
    pygame.draw.rect(surface, base, cell_rect(x, y))


def draw_tree(surface, x, y):
    draw_grass(surface, x, y)
    px = x * CELL_SIZE
    py = y * CELL_SIZE
    cx = px + CELL_SIZE // 2
    trunk = pygame.Rect(cx - 2, py + CELL_SIZE - 6, 4, 5)
    pygame.draw.rect(surface, (72, 48, 28), trunk)
    pygame.draw.circle(surface, (18, 58, 24), (cx, py + 5), 5)
    pygame.draw.circle(surface, (42, 110, 48), (cx - 3, py + 7), 4)
    pygame.draw.circle(surface, (50, 125, 55), (cx + 3, py + 6), 4)


def draw_house(surface, x, y):
    px = x * CELL_SIZE
    py = y * CELL_SIZE
    pygame.draw.rect(surface, (45, 62, 40), cell_rect(x, y))
    body = pygame.Rect(px + 2, py + 6, CELL_SIZE - 4, CELL_SIZE - 7)
    pygame.draw.rect(surface, (110, 85, 62), body)
    roof = [(px + 1, py + 7), (px + CELL_SIZE // 2, py + 1), (px + CELL_SIZE - 2, py + 7)]
    pygame.draw.polygon(surface, (165, 55, 42), roof)
    pygame.draw.rect(surface, (55, 90, 120), (px + 5, py + 9, 3, 4))


def draw_shop(surface, x, y):
    px = x * CELL_SIZE
    py = y * CELL_SIZE
    pygame.draw.rect(surface, (55, 55, 60), cell_rect(x, y))
    pygame.draw.rect(surface, (140, 120, 70), (px + 1, py + 4, CELL_SIZE - 2, 5))
    pygame.draw.rect(surface, (200, 180, 90), (px + 2, py + 9, CELL_SIZE - 4, CELL_SIZE - 10))
    pygame.draw.rect(surface, (90, 60, 40), (px + 5, py + 10, 4, 5))


def draw_hospital(surface, x, y):
    px = x * CELL_SIZE
    py = y * CELL_SIZE
    pygame.draw.rect(surface, (200, 205, 210), cell_rect(x, y))
    pygame.draw.rect(surface, (170, 175, 185), (px + 2, py + 5, CELL_SIZE - 4, CELL_SIZE - 6))
    cx = px + CELL_SIZE // 2
    cy = py + CELL_SIZE // 2
    pygame.draw.rect(surface, (200, 50, 50), (cx - 4, cy - 1, 8, 3))
    pygame.draw.rect(surface, (200, 50, 50), (cx - 1, cy - 4, 3, 8))


def draw_garage(surface, x, y):
    px = x * CELL_SIZE
    py = y * CELL_SIZE
    pygame.draw.rect(surface, (50, 52, 58), cell_rect(x, y))
    pygame.draw.rect(surface, (75, 78, 85), (px + 2, py + 4, CELL_SIZE - 4, CELL_SIZE - 5))
    pygame.draw.rect(surface, (40, 42, 48), (px + 3, py + 8, CELL_SIZE - 6, CELL_SIZE - 9))
    pygame.draw.circle(surface, (120, 125, 135), (px + 4, py + 11), 2)


def draw_school(surface, x, y):
    px = x * CELL_SIZE
    py = y * CELL_SIZE
    pygame.draw.rect(surface, (120, 55, 45), cell_rect(x, y))
    pygame.draw.rect(surface, (160, 75, 55), (px + 2, py + 5, CELL_SIZE - 4, CELL_SIZE - 6))
    pygame.draw.rect(surface, (240, 220, 160), (px + 4, py + 7, 5, 4))


def draw_barracks(surface, x, y):
    px = x * CELL_SIZE
    py = y * CELL_SIZE
    pygame.draw.rect(surface, (58, 62, 48), cell_rect(x, y))
    body = pygame.Rect(px + 1, py + 4, CELL_SIZE - 2, CELL_SIZE - 5)
    pygame.draw.rect(surface, (88, 92, 68), body)
    pygame.draw.rect(surface, (48, 52, 40), (px + 1, py + 3, CELL_SIZE - 2, 2))
    for wx in (px + 3, px + 8):
        pygame.draw.rect(surface, (120, 130, 95), (wx, py + 7, 2, 3))


def draw_bunker(surface, x, y):
    px = x * CELL_SIZE
    py = y * CELL_SIZE
    pygame.draw.rect(surface, (42, 44, 46), cell_rect(x, y))
    pygame.draw.rect(surface, (62, 65, 68), (px + 1, py + 5, CELL_SIZE - 2, CELL_SIZE - 6))
    pygame.draw.rect(surface, (28, 30, 32), (px + 4, py + 8, 5, 2))
    pygame.draw.circle(surface, (35, 38, 40), (px + 6, py + 9), 1)


def draw_armory(surface, x, y):
    px = x * CELL_SIZE
    py = y * CELL_SIZE
    pygame.draw.rect(surface, (52, 54, 50), cell_rect(x, y))
    pygame.draw.rect(surface, (95, 98, 88), (px + 1, py + 3, CELL_SIZE - 2, CELL_SIZE - 4))
    pygame.draw.rect(surface, (200, 170, 40), (px + 2, py + 5, CELL_SIZE - 4, 2))
    pygame.draw.rect(surface, (40, 42, 38), (px + 4, py + 9, CELL_SIZE - 8, CELL_SIZE - 10))


def draw_command(surface, x, y):
    px = x * CELL_SIZE
    py = y * CELL_SIZE
    pygame.draw.rect(surface, (50, 55, 52), cell_rect(x, y))
    pygame.draw.rect(surface, (72, 88, 75), (px + 2, py + 5, CELL_SIZE - 4, CELL_SIZE - 6))
    pygame.draw.rect(surface, (200, 50, 45), (px + CELL_SIZE - 5, py + 2, 3, 4))
    pygame.draw.line(surface, (90, 95, 90), (px + CELL_SIZE // 2, py + 2), (px + CELL_SIZE // 2, py + 4), 1)
    pygame.draw.circle(surface, (220, 220, 220), (px + CELL_SIZE // 2, py + 1), 1)


def draw_watchtower(surface, x, y):
    px = x * CELL_SIZE
    py = y * CELL_SIZE
    draw_grass(surface, x, y)
    cx = px + CELL_SIZE // 2
    pygame.draw.rect(surface, (70, 72, 68), (cx - 2, py + 4, 4, CELL_SIZE - 5))
    pygame.draw.rect(surface, (90, 92, 88), (cx - 4, py + 2, 8, 3))
    pygame.draw.rect(surface, (55, 58, 54), (cx - 1, py + 1, 2, 2))


def draw_wall(surface, x, y):
    px = x * CELL_SIZE
    py = y * CELL_SIZE
    pygame.draw.rect(surface, (65, 68, 55), cell_rect(x, y))
    for i in range(3):
        bx = px + 1 + i * 4
        pygame.draw.rect(surface, (120, 110, 85), (bx, py + 6, 4, 5))
        pygame.draw.rect(surface, (100, 95, 75), (bx, py + 4, 4, 3))


def draw_rock(surface, x, y):
    draw_grass(surface, x, y)
    px = x * CELL_SIZE
    py = y * CELL_SIZE
    pygame.draw.ellipse(
        surface,
        (95, 95, 100),
        (px + 2, py + 4, CELL_SIZE - 4, CELL_SIZE - 6),
    )


def draw_pond(surface, x, y):
    pygame.draw.rect(surface, (18, 42, 72), cell_rect(x, y))
    pygame.draw.rect(surface, (28, 68, 110), cell_rect(x, y).inflate(-4, -4))


def draw_road(surface, x, y, grid):
    rect = cell_rect(x, y)
    pygame.draw.rect(surface, (48, 50, 54), rect)
    pygame.draw.rect(surface, (62, 64, 68), rect.inflate(-4, -4))
    mid_x, mid_y = COLS // 2, ROWS // 2
    if y == mid_y or x == mid_x:
        cx = rect.centerx
        cy = rect.centery
        if y == mid_y:
            pygame.draw.line(surface, (200, 180, 60), (rect.left + 2, cy), (rect.right - 2, cy), 1)
        if x == mid_x:
            pygame.draw.line(surface, (200, 180, 60), (cx, rect.top + 2), (cx, rect.bottom - 2), 1)
    if current_map_type == "base" and abs(x - mid_x) <= 3 and abs(y - mid_y) <= 3:
        pygame.draw.circle(surface, (150, 155, 165), rect.center, 4, 1)
        if x == mid_x and y == mid_y:
            pygame.draw.line(surface, (180, 185, 195), (rect.left + 3, rect.centery), (rect.right - 3, rect.centery), 2)
            pygame.draw.line(surface, (180, 185, 195), (rect.centerx, rect.top + 3), (rect.centerx, rect.bottom - 3), 2)


def draw_fire(surface, x, y, flicker):
    base = (255, 90 + flicker, 15)
    pygame.draw.rect(surface, base, cell_rect(x, y))
    cx = x * CELL_SIZE + CELL_SIZE // 2
    cy = y * CELL_SIZE + CELL_SIZE // 2
    pygame.draw.circle(surface, (255, 210, 70), (cx, cy), 5)
    pygame.draw.circle(surface, (255, 140, 30), (cx, cy - 1), 3)


def draw_burnt(surface, x, y):
    pygame.draw.rect(surface, (42, 34, 30), cell_rect(x, y))
    px = x * CELL_SIZE + 4
    py = y * CELL_SIZE + 5
    pygame.draw.line(surface, (28, 24, 22), (px, py), (px + 5, py + 6), 1)


def draw_cell(surface, grid, x, y, flicker):
    state = grid[y][x]
    if state == GRASS:
        draw_grass(surface, x, y)
    elif state == TREE:
        draw_tree(surface, x, y)
    elif state == HOUSE:
        draw_house(surface, x, y)
    elif state == SHOP:
        draw_shop(surface, x, y)
    elif state == HOSPITAL:
        draw_hospital(surface, x, y)
    elif state == GARAGE:
        draw_garage(surface, x, y)
    elif state == SCHOOL:
        draw_school(surface, x, y)
    elif state == BARRACKS:
        draw_barracks(surface, x, y)
    elif state == BUNKER:
        draw_bunker(surface, x, y)
    elif state == ARMORY:
        draw_armory(surface, x, y)
    elif state == COMMAND:
        draw_command(surface, x, y)
    elif state == WATCHTOWER:
        draw_watchtower(surface, x, y)
    elif state == WALL:
        draw_wall(surface, x, y)
    elif state == ROCK:
        draw_rock(surface, x, y)
    elif state == POND:
        draw_pond(surface, x, y)
    elif state == ROAD:
        draw_road(surface, x, y, grid)
    elif state == FIRE:
        draw_fire(surface, x, y, flicker)
    elif state == BURNT:
        draw_burnt(surface, x, y)


def draw_world(surface, grid, flicker):
    for y in range(ROWS):
        for x in range(COLS):
            draw_cell(surface, grid, x, y, flicker)


def count_cells(grid):
    trees = buildings = rocks = ponds = fires = burnt = 0
    for row in grid:
        for cell in row:
            if cell == TREE:
                trees += 1
            elif is_building(cell):
                buildings += 1
            elif cell == ROCK:
                rocks += 1
            elif cell == POND:
                ponds += 1
            elif cell == FIRE:
                fires += 1
            elif cell == BURNT:
                burnt += 1
    return trees, buildings, rocks, ponds, fires, burnt


def kill_zombies_in_radius(mx, my, zombies, radius_px):
    survivors = []
    r_sq = radius_px * radius_px
    for z in zombies:
        dx = z["px"] - mx
        dy = z["py"] - my
        if dx * dx + dy * dy <= r_sq:
            continue
        survivors.append(z)
    return survivors


def bombard(grid, burn_times, terrain_memory, zombies, mx, my):
    """Explosion : feu en zone + zombies tués."""
    cell = pos_to_cell(mx, my)
    if not cell:
        return zombies, None
    cx, cy = cell
    for dy in range(-BOMB_RADIUS, BOMB_RADIUS + 1):
        for dx in range(-BOMB_RADIUS, BOMB_RADIUS + 1):
            if dx * dx + dy * dy > BOMB_RADIUS * BOMB_RADIUS + 1:
                continue
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < COLS and 0 <= ny < ROWS:
                ignite(grid, burn_times, terrain_memory, nx, ny)
    zombies = kill_zombies_in_radius(mx, my, zombies, BOMB_KILL_RADIUS)
    return zombies, {"x": mx, "y": my, "timer": 18, "max": 18}


def update_explosions(explosions):
    alive = []
    for boom in explosions:
        boom["timer"] -= 1
        if boom["timer"] > 0:
            alive.append(boom)
    return alive


def draw_explosions(surface, explosions):
    for boom in explosions:
        progress = 1 - boom["timer"] / boom["max"]
        radius = int(12 + progress * 40)
        pygame.draw.circle(surface, (255, 220, 120), (boom["x"], boom["y"]), radius, 3)
        pygame.draw.circle(surface, (255, 80, 20), (boom["x"], boom["y"]), radius // 2)


def try_kill_zombie(mx, my, zombies):
    """Clic sur un zombie = mort instantanée."""
    survivors = []
    killed = False
    radius_sq = ZOMBIE_HIT_RADIUS * ZOMBIE_HIT_RADIUS
    for z in zombies:
        dx = z["px"] - mx
        dy = z["py"] - my
        if dx * dx + dy * dy <= radius_sq:
            killed = True
        else:
            survivors.append(z)
    return survivors, killed


def new_zombie(px, py):
    dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
    return {
        "px": px,
        "py": py,
        "dx": dx,
        "dy": dy,
        "wander": random.randint(25, 70),
        "burn": 0,
        "attack_cd": 0,
    }


def max_zombies_cap():
    if current_game_mode == "survival":
        return MAX_ZOMBIES_SURVIVAL
    return MAX_ZOMBIES_TOTAL


def spawn_zombies(grid):
    zombies = []
    tries = 0
    while len(zombies) < ZOMBIE_COUNT and tries < 12000:
        tries += 1
        cx = random.randint(0, COLS - 1)
        cy = random.randint(0, ROWS - 1)
        if grid[cy][cx] == POND:
            continue
        px = cx * CELL_SIZE + CELL_SIZE / 2
        py = cy * CELL_SIZE + CELL_SIZE / 2
        zombies.append(new_zombie(px, py))
    return zombies


def random_edge_cell():
    side = random.randint(0, 3)
    if side == 0:
        return random.randint(0, COLS - 1), 0
    if side == 1:
        return random.randint(0, COLS - 1), ROWS - 1
    if side == 2:
        return 0, random.randint(0, ROWS - 1)
    return COLS - 1, random.randint(0, ROWS - 1)


def spawn_zombie_on_edge(grid, zombies):
    """Fait apparaitre un zombie sur un bord de la carte."""
    if len(zombies) >= max_zombies_cap():
        return False
    for _ in range(40):
        x, y = random_edge_cell()
        if grid[y][x] == POND:
            continue
        px, py = cell_center_px(x, y)
        zombies.append(new_zombie(px, py))
        return True
    return False


def spawn_survival_horde(grid, zombies, count):
    for _ in range(count):
        spawn_zombie_on_edge(grid, zombies)
    return zombies


def spawn_zombie_at(grid, zombies, mx, my):
    """Place un zombie où tu cliques."""
    if len(zombies) >= max_zombies_cap():
        return False
    cell = pos_to_cell(mx, my)
    if not cell:
        return False
    x, y = cell
    if grid[y][x] == POND:
        return False
    zombies.append(new_zombie(mx, my))
    return True


def cell_at_pixel(px, py):
    return int(px // CELL_SIZE), int(py // CELL_SIZE)


def can_zombie_enter(grid, gx, gy):
    if not (0 <= gx < COLS and 0 <= gy < ROWS):
        return False
    return grid[gy][gx] not in (POND,)


def nearest_military_target(z, soldiers, vehicles, max_range):
    target = None
    best_dist_sq = max_range * max_range
    for unit in soldiers + vehicles:
        if unit["hp"] <= 0:
            continue
        dx = unit["px"] - z["px"]
        dy = unit["py"] - z["py"]
        d = dx * dx + dy * dy
        if d < best_dist_sq:
            best_dist_sq = d
            target = unit
    return target, best_dist_sq


def move_zombie(z, grid, dx, dy, speed):
    dist = (dx * dx + dy * dy) ** 0.5
    if dist == 0:
        return
    nx = z["px"] + dx / dist * speed
    ny = z["py"] + dy / dist * speed
    gx, gy = cell_at_pixel(nx, ny)
    if can_zombie_enter(grid, gx, gy):
        z["px"], z["py"] = nx, ny
        cell = grid[gy][gx]
        if cell == FIRE:
            z["burn"] += 5
        else:
            z["burn"] = max(0, z["burn"] - 1)


def update_zombies(zombies, grid, soldiers, vehicles):
    survivors = []
    for z in zombies:
        z["attack_cd"] = max(0, z.get("attack_cd", 0) - 1)

        target, dist_sq = nearest_military_target(
            z, soldiers, vehicles, ZOMBIE_DETECT_MILITARY
        )
        chased = False

        if target is not None:
            dx = target["px"] - z["px"]
            dy = target["py"] - z["py"]
            dist = (dist_sq) ** 0.5
            if dist <= ZOMBIE_ATTACK_RANGE:
                if z["attack_cd"] == 0:
                    target["hp"] -= ZOMBIE_DAMAGE
                    target["hit_flash"] = 14
                    z["attack_cd"] = ZOMBIE_ATTACK_COOLDOWN
                chased = True
            elif dist > 0:
                move_zombie(z, grid, dx, dy, ZOMBIE_CHASE_SPEED)
                chased = True

        if not chased:
            z["wander"] -= 1
            if z["wander"] <= 0:
                z["wander"] = random.randint(35, 90)
                z["dx"], z["dy"] = random.choice(
                    [
                        (1, 0),
                        (-1, 0),
                        (0, 1),
                        (0, -1),
                        (1, 1),
                        (-1, 1),
                        (1, -1),
                        (-1, -1),
                    ]
                )
            move_zombie(z, grid, z["dx"], z["dy"], ZOMBIE_SPEED)

        if z["burn"] < ZOMBIE_BURN_DEATH:
            survivors.append(z)

    return survivors


def draw_zombie(surface, z, frame):
    px, py = int(z["px"]), int(z["py"])
    wobble = 1 if (frame // 8 + id(z)) % 2 else 0
    body = pygame.Rect(px - 4, py - 2 + wobble, 8, 9)
    pygame.draw.ellipse(surface, (58, 72, 52), body)
    pygame.draw.circle(surface, (75, 88, 62), (px, py - 5 + wobble), 4)
    pygame.draw.circle(surface, (40, 50, 35), (px - 1, py - 6 + wobble), 1)
    pygame.draw.circle(surface, (40, 50, 35), (px + 2, py - 6 + wobble), 1)
    if z["burn"] > 30:
        pygame.draw.circle(surface, (255, 120, 40), (px, py - 3), 3, 1)


def draw_zombies(surface, zombies, frame):
    for z in zombies:
        draw_zombie(surface, z, frame)


def can_unit_stand(grid, gx, gy):
    if not (0 <= gx < COLS and 0 <= gy < ROWS):
        return False
    return grid[gy][gx] != POND


def cell_center_px(gx, gy):
    return gx * CELL_SIZE + CELL_SIZE / 2, gy * CELL_SIZE + CELL_SIZE / 2


def nudge_off_water(grid, unit):
    """Si l'unité est sur l'eau, la repousse sur une case walkable."""
    gx, gy = cell_at_pixel(unit["px"], unit["py"])
    if can_unit_stand(grid, gx, gy):
        return
    for radius in range(1, 5):
        for dy in range(-radius, radius + 1):
            for dx in range(-radius, radius + 1):
                nx, ny = gx + dx, gy + dy
                if can_unit_stand(grid, nx, ny):
                    unit["px"], unit["py"] = cell_center_px(nx, ny)
                    return


def find_nearest_zombie(unit, zombies):
    nearest = None
    best_dist_sq = 999999999
    for z in zombies:
        dx = z["px"] - unit["px"]
        dy = z["py"] - unit["py"]
        d = dx * dx + dy * dy
        if d < best_dist_sq:
            best_dist_sq = d
            nearest = z
    return nearest, best_dist_sq


def apply_defensive_posture(
    unit, grid, zombies, shoot_range, retreat_dist, move_speed, max_hp
):
    """Tient le poste : recule si trop proche, ne poursuit jamais les zombies."""
    nearest, dist_sq = find_nearest_zombie(unit, zombies)

    if nearest is None:
        ax = unit.get("anchor_x")
        ay = unit.get("anchor_y")
        if ax is not None:
            adx = ax - unit["px"]
            ady = ay - unit["py"]
            post_dist = unit.get("post_return_dist", SOLDIER_POST_RETURN_DIST)
            if adx * adx + ady * ady > post_dist * post_dist:
                try_move_unit(unit, grid, ax, ay, move_speed * 0.35)
        return

    dist = dist_sq ** 0.5
    if dist < 0.01:
        dist = 0.01
    dx = nearest["px"] - unit["px"]
    dy = nearest["py"] - unit["py"]

    retreat_line = retreat_dist
    if unit["hp"] / max_hp < 0.45:
        retreat_line = shoot_range * 0.72

    if dist < retreat_line:
        back_x = unit["px"] - dx / dist * move_speed
        back_y = unit["py"] - dy / dist * move_speed
        try_move_unit(unit, grid, back_x, back_y, move_speed)
        ax = unit.get("anchor_x")
        ay = unit.get("anchor_y")
        if ax is not None and dist < retreat_line * 0.65:
            try_move_unit(unit, grid, ax, ay, move_speed * 0.4)


def apply_attack_posture(unit, grid, zombies, shoot_range, move_speed, max_pursue_dist):
    """Avance vers les zombies proches pour les engager."""
    nearest, dist_sq = find_nearest_zombie(unit, zombies)
    if nearest is None:
        return
    dist = dist_sq ** 0.5
    if dist > max_pursue_dist:
        return
    if dist <= shoot_range * 0.8:
        return
    try_move_unit(unit, grid, nearest["px"], nearest["py"], move_speed)


def apply_unit_movement(unit, grid, zombies, stance, shoot_range, retreat_dist, move_speed, max_hp, max_pursue):
    if stance == "attack":
        apply_attack_posture(unit, grid, zombies, shoot_range, move_speed, max_pursue)
    else:
        apply_defensive_posture(
            unit, grid, zombies, shoot_range, retreat_dist, move_speed, max_hp
        )


def freeze_unit_anchors(units):
    """En defense : le poste actuel devient la position a tenir."""
    for unit in units:
        unit["anchor_x"] = unit["px"]
        unit["anchor_y"] = unit["py"]


def stance_button_rects():
    y = HEIGHT - 36
    return {
        "attack": pygame.Rect(WIDTH - 198, y, 94, 30),
        "defense": pygame.Rect(WIDTH - 98, y, 94, 30),
    }


def draw_stance_buttons(surface, font, stance):
    for key, label in (("attack", "ATTAQUE"), ("defense", "DEFENSE")):
        rect = stance_button_rects()[key]
        active = stance == key
        if key == "attack":
            fill = (140, 55, 45) if active else (55, 42, 40)
            border = (220, 100, 70) if active else (90, 70, 65)
        else:
            fill = (45, 75, 95) if active else (40, 48, 52)
            border = (90, 160, 210) if active else (70, 80, 88)
        pygame.draw.rect(surface, fill, rect, border_radius=6)
        pygame.draw.rect(surface, border, rect, 2, border_radius=6)
        text = font.render(label, True, (240, 240, 235))
        surface.blit(
            text,
            (rect.centerx - text.get_width() // 2, rect.centery - text.get_height() // 2),
        )


def stance_button_at(mx, my):
    for key, rect in stance_button_rects().items():
        if rect.collidepoint(mx, my):
            return key
    return None


def try_move_unit(unit, grid, target_px, target_py, speed):
    """Avance vers la cible ; contourne l'eau si le chemin direct est bloqué."""
    dx = target_px - unit["px"]
    dy = target_py - unit["py"]
    dist = (dx * dx + dy * dy) ** 0.5
    moves = [(speed, 0), (-speed, 0), (0, speed), (0, -speed)]
    if dist > 0:
        moves.insert(0, (dx / dist * speed, dy / dist * speed))
    for mdx, mdy in moves:
        nx = unit["px"] + mdx
        ny = unit["py"] + mdy
        gx, gy = cell_at_pixel(nx, ny)
        if can_unit_stand(grid, gx, gy):
            unit["px"], unit["py"] = nx, ny
            return


def spawn_soldier_at(grid, soldiers, mx, my):
    """Place un soldat où tu cliques."""
    if len(soldiers) >= MAX_SOLDIERS:
        return False
    cell = pos_to_cell(mx, my)
    if not cell:
        return False
    x, y = cell
    if not can_unit_stand(grid, x, y):
        return False
    cx, cy = cell_center_px(x, y)
    soldiers.append(
        {
            "px": cx,
            "py": cy,
            "anchor_x": cx,
            "anchor_y": cy,
            "post_return_dist": SOLDIER_POST_RETURN_DIST,
            "shoot_cd": 0,
            "hp": SOLDIER_MAX_HP,
            "hit_flash": 0,
        }
    )
    return True


def update_soldiers(soldiers, zombies, grid, stance):
    survivors = list(zombies)
    alive_soldiers = []
    for s in soldiers:
        if s["hp"] <= 0:
            continue
        nudge_off_water(grid, s)
        s["hit_flash"] = max(0, s.get("hit_flash", 0) - 1)
        s["shoot_cd"] = max(0, s["shoot_cd"] - 1)

        apply_unit_movement(
            s,
            grid,
            survivors,
            stance,
            SOLDIER_SHOOT_RANGE,
            SOLDIER_RETREAT_DIST,
            SOLDIER_SPEED,
            SOLDIER_MAX_HP,
            SOLDIER_ATTACK_PURSUE_DIST,
        )
        nudge_off_water(grid, s)

        if s["shoot_cd"] == 0 and survivors:
            range_sq = SOLDIER_SHOOT_RANGE * SOLDIER_SHOOT_RANGE
            shot = None
            shot_dist = range_sq + 1
            for z in survivors:
                dx = z["px"] - s["px"]
                dy = z["py"] - s["py"]
                d = dx * dx + dy * dy
                if d <= range_sq and d < shot_dist:
                    shot_dist = d
                    shot = z
            if shot is not None:
                survivors.remove(shot)
                s["shoot_cd"] = SOLDIER_SHOOT_COOLDOWN

        alive_soldiers.append(s)

    soldiers[:] = alive_soldiers
    return survivors


def draw_soldier(surface, s):
    px, py = int(s["px"]), int(s["py"])
    body_color = (180, 70, 70) if s.get("hit_flash", 0) > 0 else (55, 75, 48)
    pygame.draw.ellipse(surface, body_color, (px - 5, py - 2, 10, 10))
    pygame.draw.circle(surface, (90, 110, 70), (px, py - 6), 5)
    pygame.draw.line(surface, (35, 35, 40), (px + 2, py - 1), (px + 11, py - 3), 2)
    if s["shoot_cd"] > SOLDIER_SHOOT_COOLDOWN - 6:
        pygame.draw.circle(surface, (255, 255, 140), (px + 12, py - 4), 4)
    # Barre de vie
    hp_ratio = s["hp"] / SOLDIER_MAX_HP
    bar_w = 12
    pygame.draw.rect(surface, (40, 40, 40), (px - 6, py - 12, bar_w, 3))
    pygame.draw.rect(surface, (80, 200, 80), (px - 6, py - 12, int(bar_w * hp_ratio), 3))


def draw_soldiers(surface, soldiers):
    for s in soldiers:
        draw_soldier(surface, s)


def spawn_vehicle_at(grid, vehicles, mx, my):
    """Place un véhicule où tu cliques (pas dans l'eau)."""
    if len(vehicles) >= MAX_VEHICLES:
        return False
    cell = pos_to_cell(mx, my)
    if not cell:
        return False
    x, y = cell
    if grid[y][x] == POND:
        return False
    cx, cy = cell_center_px(x, y)
    vehicles.append(
        {
            "px": cx,
            "py": cy,
            "anchor_x": cx,
            "anchor_y": cy,
            "post_return_dist": VEHICLE_POST_RETURN_DIST,
            "hp": VEHICLE_MAX_HP,
            "hit_flash": 0,
            "shoot_cd": 0,
        }
    )
    return True


def current_tool_label(weapon):
    labels = {
        "fire": "FEU",
        "bomb": "BOMBARDEMENT",
        "soldier": "PLACER SOLDAT",
        "vehicle": "PLACER VEHICULE",
        "zombie": "PLACER ZOMBIE",
    }
    return labels.get(weapon, weapon)


def update_vehicles(vehicles, zombies, grid, stance):
    survivors = list(zombies)
    range_sq = VEHICLE_SHOOT_RANGE * VEHICLE_SHOOT_RANGE
    alive_vehicles = []

    for v in vehicles:
        if v["hp"] <= 0:
            continue
        nudge_off_water(grid, v)
        v["hit_flash"] = max(0, v.get("hit_flash", 0) - 1)
        v["shoot_cd"] = max(0, v.get("shoot_cd", 0) - 1)

        apply_unit_movement(
            v,
            grid,
            survivors,
            stance,
            VEHICLE_SHOOT_RANGE,
            VEHICLE_RETREAT_DIST,
            VEHICLE_SPEED,
            VEHICLE_MAX_HP,
            VEHICLE_ATTACK_PURSUE_DIST,
        )
        nudge_off_water(grid, v)

        if v["shoot_cd"] == 0 and survivors:
            shot = None
            shot_dist = range_sq + 1
            for z in survivors:
                dx = z["px"] - v["px"]
                dy = z["py"] - v["py"]
                d = dx * dx + dy * dy
                if d <= range_sq and d < shot_dist:
                    shot_dist = d
                    shot = z
            if shot is not None:
                survivors.remove(shot)
                v["shoot_cd"] = VEHICLE_SHOOT_COOLDOWN

        alive_vehicles.append(v)

    vehicles[:] = alive_vehicles
    return survivors


def draw_vehicle(surface, v):
    px, py = int(v["px"]), int(v["py"])
    color = (90, 50, 50) if v.get("hit_flash", 0) > 0 else (65, 72, 58)
    pygame.draw.rect(surface, color, (px - 9, py - 5, 18, 12), border_radius=2)
    pygame.draw.rect(surface, (45, 48, 42), (px - 6, py - 7, 12, 6))
    pygame.draw.circle(surface, (30, 30, 35), (px - 5, py + 6), 3)
    pygame.draw.circle(surface, (30, 30, 35), (px + 5, py + 6), 3)
    pygame.draw.rect(surface, (50, 60, 50), (px + 4, py - 4, 8, 5))
    if v.get("shoot_cd", 0) > VEHICLE_SHOOT_COOLDOWN - 8:
        pygame.draw.line(surface, (255, 220, 100), (px + 10, py - 2), (px + 28, py - 4), 3)
        pygame.draw.circle(surface, (255, 180, 60), (px + 28, py - 4), 4)
    bar_w = 18
    hp_ratio = v["hp"] / VEHICLE_MAX_HP
    pygame.draw.rect(surface, (40, 40, 40), (px - 9, py - 14, bar_w, 3))
    pygame.draw.rect(surface, (100, 180, 220), (px - 9, py - 14, int(bar_w * hp_ratio), 3))


def draw_vehicles(surface, vehicles):
    for v in vehicles:
        draw_vehicle(surface, v)


def reset_world(map_type=None, game_mode=None):
    global current_map_type, current_game_mode
    if game_mode is not None:
        current_game_mode = game_mode
    if map_type is not None:
        current_map_type = map_type
    grid = generate_world(current_map_type)
    burn_times = new_burn_times()
    terrain_memory = [[GRASS for _ in range(COLS)] for _ in range(ROWS)]
    for y in range(ROWS):
        for x in range(COLS):
            cell = grid[y][x]
            if is_flammable(cell):
                terrain_memory[y][x] = cell
    if current_game_mode == "survival":
        zombies = []
        prep_frames = SURVIVAL_PREP_FRAMES
        start_weapon = "soldier"
    else:
        zombies = spawn_zombies(grid)
        prep_frames = 0
        start_weapon = "fire"
    return (
        grid,
        burn_times,
        terrain_memory,
        zombies,
        [],
        [],
        [],
        start_weapon,
        prep_frames,
    )


def begin_survival_assault(grid, zombies):
    return spawn_survival_horde(grid, zombies, SURVIVAL_INITIAL_HORDE)


def hud_map_label():
    if current_game_mode == "survival":
        return "SURVIE"
    if current_map_type == "base":
        return "BASE MILITAIRE"
    return "VILLE"


def menu_choice_rect(index):
    y = 115 + index * 72
    return pygame.Rect(WIDTH // 2 - 155, y, 310, 54).inflate(8, 8)


def run_map_menu(screen, font, clock):
    """Menu : retourne (game_mode, map_type) ou None."""
    title_font = pygame.font.SysFont(None, 40)
    # map_type, game_mode, label, description
    choices = [
        ("ville", "sandbox", "1 — Map VILLE", "Foret, etangs, maisons et commerces"),
        ("base", "sandbox", "2 — Base MILITAIRE", "QG, bunkers, tours, casernes, helipad"),
        (
            "base",
            "survival",
            "3 — MODE SURVIE",
            f"{SURVIVAL_PREP_SECONDS}s pour placer — horde de tous les cotes",
        ),
    ]

    while True:
        screen.fill((12, 14, 16))
        title = title_font.render("Project Zomboid — Choisis ta map", True, (235, 230, 210))
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 40))

        for i, (_, _, label, desc) in enumerate(choices):
            rect = menu_choice_rect(i)
            inner = rect.inflate(-8, -8)
            pygame.draw.rect(screen, (38, 48, 42), inner, border_radius=8)
            pygame.draw.rect(screen, (90, 120, 85), inner, 2, border_radius=8)
            screen.blit(font.render(label, True, (230, 235, 220)), (inner.x + 14, inner.y + 8))
            screen.blit(font.render(desc, True, (150, 155, 145)), (inner.x + 14, inner.y + 28))

        hint = font.render(
            "1 / 2 / 3  |  clic  |  Echap = quitter",
            True,
            (130, 130, 125),
        )
        screen.blit(hint, (WIDTH // 2 - hint.get_width() // 2, HEIGHT - 40))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return None
                if event.key == pygame.K_1:
                    return ("sandbox", "ville")
                if event.key == pygame.K_2:
                    return ("sandbox", "base")
                if event.key == pygame.K_3:
                    return ("survival", "base")
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos
                for i, (map_type, game_mode, _, _) in enumerate(choices):
                    if menu_choice_rect(i).collidepoint(mx, my):
                        return (game_mode, map_type)
        clock.tick(30)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Feu de forêt — Zomboid vibe")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 20)

    menu_pick = run_map_menu(screen, font, clock)
    if menu_pick is None:
        pygame.quit()
        sys.exit(0)
    game_mode, selected_map = menu_pick

    (
        grid,
        burn_times,
        terrain_memory,
        zombies,
        explosions,
        soldiers,
        vehicles,
        weapon,
        survival_prep,
    ) = reset_world(selected_map, game_mode)
    tick = 0
    survival_active = False
    military_stance = "defense"
    map_label = hud_map_label()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    (
                        grid,
                        burn_times,
                        terrain_memory,
                        zombies,
                        explosions,
                        soldiers,
                        vehicles,
                        weapon,
                        survival_prep,
                    ) = reset_world(current_map_type, current_game_mode)
                    survival_active = False
                    tick = 0
                elif event.key == pygame.K_TAB:
                    new_pick = run_map_menu(screen, font, clock)
                    if new_pick:
                        game_mode, selected_map = new_pick
                        (
                            grid,
                            burn_times,
                            terrain_memory,
                            zombies,
                            explosions,
                            soldiers,
                            vehicles,
                            weapon,
                            survival_prep,
                        ) = reset_world(selected_map, game_mode)
                        survival_active = False
                        map_label = hud_map_label()
                        tick = 0
                elif event.key == pygame.K_SPACE and current_game_mode == "survival" and survival_prep > 0:
                    survival_prep = 0
                    zombies = begin_survival_assault(grid, zombies)
                    survival_active = True
                elif event.key in (pygame.K_3, pygame.K_m):
                    weapon = "soldier"
                elif event.key in (pygame.K_4, pygame.K_v):
                    weapon = "vehicle"
                elif event.key in (pygame.K_a,):
                    military_stance = "attack"
                elif event.key in (pygame.K_d,):
                    military_stance = "defense"
                    freeze_unit_anchors(soldiers)
                    freeze_unit_anchors(vehicles)
                elif current_game_mode != "survival" or survival_active:
                    if event.key in (pygame.K_1, pygame.K_f):
                        weapon = "fire"
                    elif event.key in (pygame.K_2, pygame.K_b):
                        weapon = "bomb"
                    elif event.key in (pygame.K_5, pygame.K_z):
                        weapon = "zombie"
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos
                clicked_stance = stance_button_at(mx, my)
                if clicked_stance == "attack":
                    military_stance = "attack"
                    continue
                if clicked_stance == "defense":
                    military_stance = "defense"
                    freeze_unit_anchors(soldiers)
                    freeze_unit_anchors(vehicles)
                    continue
                in_prep = current_game_mode == "survival" and survival_prep > 0
                if weapon == "zombie" and not in_prep and current_game_mode != "survival":
                    spawn_zombie_at(grid, zombies, mx, my)
                elif weapon == "soldier":
                    spawn_soldier_at(grid, soldiers, mx, my)
                elif weapon == "vehicle":
                    spawn_vehicle_at(grid, vehicles, mx, my)
                elif weapon == "bomb" and not in_prep:
                    zombies, boom = bombard(
                        grid, burn_times, terrain_memory, zombies, mx, my
                    )
                    if boom:
                        explosions.append(boom)
                elif weapon == "fire" and not in_prep:
                    zombies, killed = try_kill_zombie(mx, my, zombies)
                    if not killed:
                        cell = pos_to_cell(mx, my)
                        if cell:
                            ignite(
                                grid, burn_times, terrain_memory, cell[0], cell[1]
                            )

        if current_game_mode == "survival":
            if survival_prep > 0:
                survival_prep -= 1
                if survival_prep == 0:
                    zombies = begin_survival_assault(grid, zombies)
                    survival_active = True
            elif survival_active and tick % SURVIVAL_SPAWN_INTERVAL == 0:
                for _ in range(SURVIVAL_SPAWN_PER_TICK):
                    spawn_zombie_on_edge(grid, zombies)

        if current_game_mode != "survival" or survival_active:
            update_fire(grid, burn_times, terrain_memory, tick)
            zombies = update_zombies(zombies, grid, soldiers, vehicles)
            zombies = update_vehicles(vehicles, zombies, grid, military_stance)
            zombies = update_soldiers(soldiers, zombies, grid, military_stance)
            explosions = update_explosions(explosions)
        tick += 1
        flicker = (tick // 2) % 25

        screen.fill(COLOR_BACKGROUND)
        draw_world(screen, grid, flicker)
        draw_zombies(screen, zombies, tick)
        draw_soldiers(screen, soldiers)
        draw_vehicles(screen, vehicles)
        draw_explosions(screen, explosions)

        if current_game_mode == "survival" and survival_prep > 0:
            secs_left = max(1, (survival_prep + 59) // 60)
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 90))
            screen.blit(overlay, (0, 0))
            big = pygame.font.SysFont(None, 52)
            prep_text = big.render(f"PREPARATION — {secs_left}s", True, (255, 230, 160))
            screen.blit(prep_text, (WIDTH // 2 - prep_text.get_width() // 2, HEIGHT // 2 - 40))
            prep_sub = font.render(
                "Place tes soldats [3] et vehicules [4] — Espace = lancer la vague",
                True,
                (200, 200, 190),
            )
            screen.blit(prep_sub, (WIDTH // 2 - prep_sub.get_width() // 2, HEIGHT // 2 + 10))

        trees, buildings, rocks, ponds, fires, burnt = count_cells(grid)
        tool = current_tool_label(weapon)
        stance_name = "ATTAQUE" if military_stance == "attack" else "DEFENSE"
        hint = font.render(
            f"{map_label}  |  {stance_name}  |  {tool}  |  🔥{fires}  🧟{len(zombies)}  🪖{len(soldiers)}  🚗{len(vehicles)}",
            True,
            (230, 200, 160),
        )
        screen.blit(hint, (8, 6))
        draw_stance_buttons(screen, font, military_stance)
        if current_game_mode == "survival" and survival_prep > 0:
            sub = font.render(
                "Mode survie : uniquement soldats et vehicules pendant la prep",
                True,
                (180, 200, 160),
            )
        elif current_game_mode == "survival":
            sub = font.render(
                "SURVIE — boutons ATTAQUE/DEFENSE en bas a droite  |  [A][D]  |  [1][2] feu bombe",
                True,
                (200, 140, 140),
            )
        else:
            sub = font.render(
                "Boutons ATTAQUE/DEFENSE (bas droite) ou [A]/[D] — [3] soldat [4] vehicule",
                True,
                (150, 150, 150),
            )
        screen.blit(sub, (8, 24))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit(0)


if __name__ == "__main__":
    main()
