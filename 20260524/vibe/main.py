"""
Afrique du Nord 1942 — stratégie sur carte réelle (tuiles)
Mer Méditerranée, désert, villes, chars & infanterie, contrôle territorial.
"""

import math
import random
import sys
from collections import deque

import pygame

# --- Carte tuilée (profil géographique Afrique du Nord) ---
CELL = 20
COLS = 50
ROWS = 26
MAP_W = COLS * CELL
MAP_H = ROWS * CELL
PANEL_W = 240
HUD_H = 72
WIDTH = MAP_W + PANEL_W
HEIGHT = MAP_H + HUD_H

SEA = 0
DESERT = 1
HILL = 2
CITY = 3
COAST = 4

TERRAIN = {
    SEA: {"name": "mer", "color": (32, 72, 118), "pass": False, "cost": 99},
    DESERT: {"name": "desert", "color": (196, 168, 110), "pass": True, "cost": 1},
    HILL: {"name": "colline", "color": (140, 118, 78), "pass": True, "cost": 2},
    CITY: {"name": "ville", "color": (168, 148, 108), "pass": True, "cost": 1},
    COAST: {"name": "cote", "color": (148, 178, 128), "pass": True, "cost": 1},
}

TEAM_ALLIES = "allies"
TEAM_AXIS = "axis"

UNIT_INF = "infantry"
UNIT_ARMOR = "armor"
UNIT_ARTY = "artillery"

UNIT_STATS = {
    UNIT_INF: {"label": "Infanterie", "mp": 3, "atk": 4, "def": 3, "hp": 10},
    UNIT_ARMOR: {"label": "Chars", "mp": 4, "atk": 6, "def": 5, "hp": 12},
    UNIT_ARTY: {"label": "Artillerie", "mp": 2, "atk": 5, "def": 2, "hp": 8},
}

# Villes : position en fraction ouest→est (0=Atlantique, 1=Égypte), décalage vers l'intérieur
CITY_SPECS = [
    {"id": "casablanca", "label": "Casablanca", "west": 0.10, "inland": 1, "hq": TEAM_ALLIES},
    {"id": "marrakech", "label": "Marrakech", "west": 0.14, "inland": 4},
    {"id": "alger", "label": "Alger", "west": 0.26, "inland": 1},
    {"id": "tunis", "label": "Tunis", "west": 0.44, "inland": 1},
    {"id": "tripoli", "label": "Tripoli", "west": 0.58, "inland": 1, "hq": TEAM_AXIS},
    {"id": "benghazi", "label": "Benghazi", "west": 0.72, "inland": 1},
    {"id": "tobruk", "label": "Tobrouk", "west": 0.78, "inland": 2},
    {"id": "el_alamein", "label": "El Alamein", "west": 0.84, "inland": 1},
    {"id": "le_caire", "label": "Le Caire", "west": 0.92, "inland": 3},
]

CITIES = {}
CITY_BY_ID = {}


def _coast_row_for_column(x):
    """Ligne de côte méditerranéenne (forme Maroc → Égypte)."""
    t = x / max(1, COLS - 1)
    if t < 0.06:
        return 11
    if t < 0.20:
        return 9 + int(math.sin(x * 0.45) * 0.8)
    if t < 0.36:
        return 8
    if t < 0.46:
        return 7 if 0.38 < t < 0.44 else 8
    if t < 0.70:
        return 9 + int(0.5 * math.sin(x * 0.25))
    if t < 0.86:
        return 10
    return 11 + int((t - 0.86) * 12)


def _west_land_edge(x):
    """Limite ouest du continent (Maroc / Atlantique)."""
    t = x / max(1, COLS - 1)
    if t < 0.05:
        return COLS
    if t < 0.18:
        return max(0, int(2 + t * 18))
    return 0


def build_terrain():
    """Génère mer au nord, côte, Sahara, Atlas ; golfe de Tunis ; delta du Nil."""
    coast = [_coast_row_for_column(x) for x in range(COLS)]
    grid = [[SEA for _ in range(COLS)] for _ in range(ROWS)]

    for y in range(ROWS):
        for x in range(COLS):
            if x < _west_land_edge(x) and y > 6:
                continue
            cy = coast[x]
            if y < cy:
                grid[y][x] = SEA
            elif y == cy:
                grid[y][x] = COAST
            else:
                grid[y][x] = DESERT

    # Golfe de Tunis (mer qui mord la côte)
    for x, y in ((21, 5), (22, 5), (23, 6), (24, 5), (25, 6)):
        if in_bounds(x, y):
            grid[y][x] = SEA

    # Détroit de Gibraltar / Atlantique à l'ouest
    for y in range(6, 14):
        for x in range(0, 4):
            grid[y][x] = SEA

    # Chaîne de l'Atlas (Maroc – Algérie)
    for y in range(ROWS):
        for x in range(COLS):
            t = x / max(1, COLS - 1)
            cy = coast[x]
            if DESERT <= grid[y][x] <= COAST and 0.08 < t < 0.34 and cy + 2 <= y <= cy + 6:
                if (x + y) % 4 != 0:
                    grid[y][x] = HILL

    # Delta du Nil (Égypte, coin est)
    for x in range(42, COLS):
        for y in range(coast[x], min(ROWS, coast[x] + 5)):
            if x >= 44 and y >= coast[x] + 1:
                grid[y][x] = COAST if y == coast[x] + 1 else DESERT

    global CITIES, CITY_BY_ID
    CITIES = {}
    for spec in CITY_SPECS:
        gx = int(spec["west"] * (COLS - 6)) + 2
        gx = max(4, min(COLS - 2, gx))
        gy = coast[gx] + spec.get("inland", 1)
        gy = min(ROWS - 2, max(coast[gx] + 1, gy))
        while gy < ROWS and grid[gy][gx] == SEA:
            gy += 1
        if not in_bounds(gx, gy):
            continue
        info = {k: v for k, v in spec.items() if k not in ("west", "inland")}
        CITIES[(gx, gy)] = info
        grid[gy][gx] = CITY
        CITY_BY_ID[spec["id"]] = ((gx, gy), info)

    return grid


def enemy_team(team):
    return TEAM_AXIS if team == TEAM_ALLIES else TEAM_ALLIES


def team_label(team):
    return "Alliés" if team == TEAM_ALLIES else "Afrika Korps"


def tile_center(gx, gy):
    return gx * CELL + CELL // 2, gy * CELL + CELL // 2


def in_bounds(gx, gy):
    return 0 <= gx < COLS and 0 <= gy < ROWS


def city_at(gx, gy):
    return CITIES.get((gx, gy))


def unit_at(units, gx, gy):
    for u in units:
        if u["gx"] == gx and u["gy"] == gy and u["hp"] > 0:
            return u
    return None


def _adjacent_land(terrain, gx, gy, dx, dy):
    nx, ny = gx + dx, gy + dy
    if not in_bounds(nx, ny):
        return None
    if TERRAIN[terrain[ny][nx]]["pass"]:
        return nx, ny
    return None


def init_game(player_team):
    terrain = build_terrain()
    units = []
    uid = 0

    def add(team, utype, gx, gy):
        nonlocal uid
        if not in_bounds(gx, gy) or not TERRAIN[terrain[gy][gx]]["pass"]:
            return
        st = UNIT_STATS[utype]
        units.append(
            {
                "id": uid,
                "team": team,
                "type": utype,
                "gx": gx,
                "gy": gy,
                "hp": st["hp"],
                "mp_left": st["mp"],
                "moved": False,
            }
        )
        uid += 1

    def near_city(city_id, dx=0, dy=0):
        pos, _ = CITY_BY_ID[city_id]
        gx, gy = pos[0] + dx, pos[1] + dy
        if in_bounds(gx, gy) and TERRAIN[terrain[gy][gx]]["pass"]:
            return gx, gy
        for ddx, ddy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            p = _adjacent_land(terrain, pos[0], pos[1], ddx, ddy)
            if p:
                return p[0] + dx, p[1] + dy
        return pos

    if player_team == TEAM_ALLIES:
        c1 = near_city("casablanca")
        add(TEAM_ALLIES, UNIT_ARMOR, *c1)
        add(TEAM_ALLIES, UNIT_INF, c1[0] + 1, c1[1])
        a = near_city("alger")
        add(TEAM_ALLIES, UNIT_INF, *a)
        ca = near_city("le_caire")
        add(TEAM_ALLIES, UNIT_ARMOR, *ca)
        e = near_city("el_alamein")
        add(TEAM_ALLIES, UNIT_ARTY, *e)
        t = near_city("tripoli")
        add(TEAM_AXIS, UNIT_ARMOR, *t)
        add(TEAM_AXIS, UNIT_INF, t[0] + 1, t[1])
        b = near_city("benghazi")
        add(TEAM_AXIS, UNIT_ARMOR, *b)
        tu = near_city("tunis")
        add(TEAM_AXIS, UNIT_INF, *tu)
    else:
        t = near_city("tripoli")
        add(TEAM_AXIS, UNIT_ARMOR, *t)
        add(TEAM_AXIS, UNIT_INF, t[0] - 1, t[1])
        b = near_city("benghazi")
        add(TEAM_AXIS, UNIT_ARMOR, *b)
        tu = near_city("tunis")
        add(TEAM_AXIS, UNIT_INF, *tu)
        c1 = near_city("casablanca")
        add(TEAM_ALLIES, UNIT_INF, *c1)
        a = near_city("alger")
        add(TEAM_ALLIES, UNIT_ARMOR, *a)
        ca = near_city("le_caire")
        add(TEAM_ALLIES, UNIT_INF, *ca)

    control = {}
    for pos, info in CITIES.items():
        gx, gy = pos
        if info.get("hq") == TEAM_ALLIES:
            control[info["id"]] = TEAM_ALLIES
        elif info.get("hq") == TEAM_AXIS:
            control[info["id"]] = TEAM_AXIS
        else:
            control[info["id"]] = None

    return {
        "terrain": terrain,
        "units": units,
        "control": control,
        "player": player_team,
        "turn": "player",
        "turn_num": 1,
        "selected": None,
        "reachable": {},
        "result": None,
        "log": ["Carte Afrique du Nord chargée (ouest → est). Prenez le QG ennemi."],
        "hover": None,
        "combat_fx": 0,
        "combat_pos": None,
        "ai_step": 0,
    }


def add_log(state, msg):
    state["log"].append(msg)
    if len(state["log"]) > 9:
        state["log"].pop(0)


def movement_cost(terrain, gx, gy):
    t = terrain[gy][gx]
    return TERRAIN[t]["cost"]


def compute_reachable(state, unit):
    terrain = state["terrain"]
    units = state["units"]
    mp = unit["mp_left"]
    start = (unit["gx"], unit["gy"])
    dist = {start: 0}
    q = deque([start])
    while q:
        x, y = q.popleft()
        d0 = dist[(x, y)]
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if not in_bounds(nx, ny):
                continue
            if not TERRAIN[terrain[ny][nx]]["pass"]:
                continue
            cost = movement_cost(terrain, nx, ny)
            nd = d0 + cost
            if nd > mp:
                continue
            other = unit_at(units, nx, ny)
            if other and other["team"] != unit["team"]:
                if (nx, ny) not in dist or nd < dist[(nx, ny)]:
                    dist[(nx, ny)] = nd
                continue
            if (nx, ny) not in dist or nd < dist[(nx, ny)]:
                dist[(nx, ny)] = nd
                q.append((nx, ny))
    dist.pop(start, None)
    return dist


def reset_mp_for_team(units, team):
    for u in units:
        if u["team"] == team and u["hp"] > 0:
            u["mp_left"] = UNIT_STATS[u["type"]]["mp"]
            u["moved"] = False


def city_reinforcements(state, team):
    count = 0
    for cid, owner in state["control"].items():
        if owner == team:
            gx, gy = CITY_BY_ID[cid][0]
            if unit_at(state["units"], gx, gy) is None:
                st = UNIT_STATS[UNIT_INF]
                state["units"].append(
                    {
                        "id": 9000 + random.randint(0, 999),
                        "team": team,
                        "type": UNIT_INF,
                        "gx": gx,
                        "gy": gy,
                        "hp": st["hp"] // 2 + 2,
                        "mp_left": 0,
                        "moved": True,
                    }
                )
                count += 1
            else:
                u = unit_at(state["units"], gx, gy)
                if u["team"] == team:
                    u["hp"] = min(UNIT_STATS[u["type"]]["hp"], u["hp"] + 2)
                    count += 1
    return count


def resolve_combat(att, defender, terrain, gx, gy, control):
    ast = UNIT_STATS[att["type"]]
    dst = UNIT_STATS[defender["type"]]
    atk_val = ast["atk"]
    def_val = dst["def"]
    if terrain[gy][gx] == HILL:
        def_val += 1
    c = city_at(gx, gy)
    if c and control.get(c["id"]) == defender["team"]:
        def_val += 2
        if c.get("hq") == defender["team"]:
            def_val += 1
    dmg_to_def = max(1, atk_val - def_val // 2)
    dmg_to_att = max(1, def_val - atk_val // 2)
    return dmg_to_def, dmg_to_att


def fight(state, att, defender):
    terrain = state["terrain"]
    gx, gy = defender["gx"], defender["gy"]
    d1, d2 = resolve_combat(att, defender, terrain, gx, gy, state["control"])
    defender["hp"] -= d1
    att["hp"] -= d2
    add_log(
        state,
        f"Combat : {UNIT_STATS[att['type']]['label']} vs {UNIT_STATS[defender['type']]['label']} "
        f"(-{d2} / -{d1})",
    )
    state["combat_fx"] = 40
    state["combat_pos"] = (gx, gy)
    if defender["hp"] <= 0:
        att["gx"] = gx
        att["gy"] = gy
        att["mp_left"] = max(0, att["mp_left"] - movement_cost(terrain, gx, gy))
    if att["hp"] <= 0:
        pass


def capture_city(state, unit):
    c = city_at(unit["gx"], unit["gy"])
    if not c:
        return
    cid = c["id"]
    if state["control"].get(cid) != unit["team"]:
        state["control"][cid] = unit["team"]
        add_log(state, f"{c['label']} tombe aux mains des {team_label(unit['team'])}.")


def check_victory(state):
    player = state["player"]
    enemy = enemy_team(player)
    for meta in CITIES.values():
        cid = meta["id"]
        owner = state["control"].get(cid)
        if meta.get("hq") == enemy and owner == player:
            return "victoire"
        if meta.get("hq") == player and owner == enemy:
            return "defaite"
    alive_p = [u for u in state["units"] if u["hp"] > 0 and u["team"] == player]
    alive_e = [u for u in state["units"] if u["hp"] > 0 and u["team"] == enemy]
    if not alive_p:
        return "defaite"
    if not alive_e:
        return "victoire"
    return None


def move_unit(state, unit, gx, gy):
    terrain = state["terrain"]
    dist_map = state.get("_reach_cache")
    if dist_map is None:
        dist_map = compute_reachable(state, unit)
    start = (unit["gx"], unit["gy"])
    if (gx, gy) not in dist_map:
        return False
    cost = dist_map[(gx, gy)]
    unit["gx"] = gx
    unit["gy"] = gy
    unit["mp_left"] -= cost
    unit["moved"] = True
    capture_city(state, unit)
    return True


def pos_to_cell(mx, my):
    if mx >= MAP_W or my >= MAP_H:
        return None
    return mx // CELL, my // CELL


def ai_play(state):
    player = state["player"]
    enemy = enemy_team(player)
    units = [u for u in state["units"] if u["hp"] > 0 and u["team"] == enemy and not u["moved"]]
    random.shuffle(units)
    acted = 0
    for unit in units[:3]:
        reach = compute_reachable(state, unit)
        if not reach:
            unit["moved"] = True
            continue
        target_hq = None
        for meta in CITIES.values():
            if meta.get("hq") == player:
                target_hq = CITY_BY_ID[meta["id"]][0]
                break
        best = None
        best_score = -1
        for (tx, ty), cost in reach.items():
            score = 0
            other = unit_at(state["units"], tx, ty)
            if other and other["team"] == player:
                score = 60 + UNIT_STATS[unit["type"]]["atk"]
            elif city_at(tx, ty):
                c = city_at(tx, ty)
                if state["control"].get(c["id"]) != enemy:
                    score = 45
            if target_hq:
                score += max(0, 30 - abs(tx - target_hq[0]) - abs(ty - target_hq[1]))
            score -= cost
            if score > best_score:
                best_score = score
                best = (tx, ty)
        if best:
            tx, ty = best
            other = unit_at(state["units"], tx, ty)
            if other and other["team"] == player:
                fight(state, unit, other)
            else:
                state["_reach_cache"] = reach
                move_unit(state, unit, tx, ty)
            unit["moved"] = True
            acted += 1
    state.pop("_reach_cache", None)
    return acted


def draw_terrain_tile(surface, gx, gy, t, tick, control, city):
    rect = pygame.Rect(gx * CELL, gy * CELL, CELL, CELL)
    base = TERRAIN[t]["color"]
    if t == SEA:
        wave = int(8 * math.sin(tick * 0.05 + gx * 0.4 + gy * 0.3))
        col = tuple(max(0, min(255, c + wave)) for c in base)
    else:
        shade = ((gx + gy) % 3) * 6
        col = tuple(max(0, min(255, c - shade)) for c in base)
    pygame.draw.rect(surface, col, rect)

    if t == COAST:
        pygame.draw.line(surface, (100, 140, 160), (rect.left, rect.top), (rect.right, rect.top), 2)
    if t == HILL:
        pygame.draw.polygon(
            surface,
            (100, 82, 58),
            [(rect.centerx, rect.top + 4), (rect.left + 4, rect.bottom - 4), (rect.right - 4, rect.bottom - 4)],
        )

    if city:
        owner = control.get(city["id"])
        if owner == TEAM_ALLIES:
            tint = (60, 90, 60)
        elif owner == TEAM_AXIS:
            tint = (90, 70, 50)
        else:
            tint = (80, 75, 65)
        pygame.draw.rect(surface, tint, rect.inflate(-6, -6), border_radius=4)
        if city.get("hq"):
            pygame.draw.rect(surface, (255, 210, 80), rect.inflate(-16, -16), 2, border_radius=2)

    pygame.draw.rect(surface, (40, 34, 24), rect, 1)


def draw_map(surface, state, tick):
    terrain = state["terrain"]
    for y in range(ROWS):
        for x in range(COLS):
            city = city_at(x, y)
            draw_terrain_tile(surface, x, y, terrain[y][x], tick, state["control"], city)

    small = pygame.font.SysFont(None, 18)
    surface.blit(small.render("← Maroc", True, (60, 50, 40)), (8, MAP_H - 22))
    surface.blit(small.render("Égypte →", True, (60, 50, 40)), (MAP_W - 72, MAP_H - 22))
    surface.blit(small.render("Méditerranée ↑", True, (80, 120, 160)), (MAP_W // 2 - 50, 6))

    reach = state.get("reachable", {})
    for (rx, ry), cost in reach.items():
        r = pygame.Rect(rx * CELL, ry * CELL, CELL, CELL)
        s = pygame.Surface((CELL, CELL), pygame.SRCALPHA)
        s.fill((100, 200, 120, 90 if cost <= 2 else 60))
        surface.blit(s, r.topleft)

    sel = state.get("selected")
    if sel:
        r = pygame.Rect(sel["gx"] * CELL, sel["gy"] * CELL, CELL, CELL)
        pygame.draw.rect(surface, (255, 230, 80), r, 3)

    if state.get("combat_fx", 0) > 0 and state.get("combat_pos"):
        cx, cy = state["combat_pos"]
        r = pygame.Rect(cx * CELL, cy * CELL, CELL, CELL)
        pygame.draw.rect(surface, (255, 100, 60), r.inflate(4, 4), 3)

    for pos, info in CITIES.items():
        gx, gy = pos
        cx, cy = tile_center(gx, gy)
        f = pygame.font.SysFont(None, 16)
        name = f.render(info["label"][:10], True, (30, 24, 16))
        surface.blit(name, (cx - name.get_width() // 2, gy * CELL - 14))


def draw_unit(surface, u):
    cx, cy = tile_center(u["gx"], u["gy"])
    col = (70, 110, 75) if u["team"] == TEAM_ALLIES else (120, 95, 60)
    dark = (40, 70, 45) if u["team"] == TEAM_ALLIES else (80, 60, 38)
    pygame.draw.circle(surface, dark, (cx + 2, cy + 2), 11)
    pygame.draw.circle(surface, col, (cx, cy), 11)
    if u["type"] == UNIT_ARMOR:
        pygame.draw.rect(surface, dark, (cx - 9, cy - 3, 18, 7), border_radius=2)
        pygame.draw.line(surface, (200, 180, 100), (cx + 4, cy - 1), (cx + 12, cy - 3), 2)
    elif u["type"] == UNIT_ARTY:
        pygame.draw.circle(surface, dark, (cx - 6, cy + 4), 3)
        pygame.draw.circle(surface, dark, (cx + 6, cy + 4), 3)
        pygame.draw.line(surface, (200, 180, 100), (cx - 4, cy - 4), (cx + 10, cy - 6), 3)
    else:
        pygame.draw.circle(surface, (220, 200, 170), (cx, cy - 3), 3)
        pygame.draw.line(surface, (180, 160, 120), (cx, cy), (cx + 8, cy - 4), 2)
    hp = pygame.font.SysFont(None, 18).render(str(u["hp"]), True, (255, 250, 235))
    surface.blit(hp, (cx - hp.get_width() // 2, cy + 8))


def draw_panel(surface, state):
    px = MAP_W
    pygame.draw.rect(surface, (28, 24, 18), (px, 0, PANEL_W, MAP_H))
    y = 14
    f = pygame.font.SysFont(None, 22)
    surface.blit(f.render("État-major", True, (210, 190, 140)), (px + 12, y))
    y += 28
    small = pygame.font.SysFont(None, 18)
    for line in state["log"][-8:]:
        surface.blit(small.render(line[:38], True, (175, 165, 145)), (px + 10, y))
        y += 20
    y = MAP_H - 150
    surface.blit(small.render(f"Tour {state['turn_num']}", True, (200, 190, 170)), (px + 10, y))
    y += 22
    sel = state.get("selected")
    if sel:
        st = UNIT_STATS[sel["type"]]
        surface.blit(
            small.render(f"{st['label']} PV:{sel['hp']} PM:{sel['mp_left']}", True, (200, 190, 170)),
            (px + 10, y),
        )


def draw_hud(surface, state):
    pygame.draw.rect(surface, (18, 16, 12), (0, MAP_H, WIDTH, HUD_H))
    if state["result"] == "victoire":
        msg = f"VICTOIRE — {team_label(state['player'])}  [R] rejouer"
    elif state["result"] == "defaite":
        msg = f"DÉFAITE  [R] rejouer"
    elif state["turn"] == "ai":
        msg = f"Tour {state['turn_num']} — {team_label(enemy_team(state['player']))} en mouvement..."
    else:
        msg = (
            f"Tour {state['turn_num']} | Clic unité → clic case verte | "
            f"[ESPACE] fin de tour (renforts dans villes tenues)"
        )
    surface.blit(pygame.font.SysFont(None, 24).render(msg, True, (220, 205, 175)), (12, MAP_H + 10))
    surface.blit(
        pygame.font.SysFont(None, 18).render(
            "Carte tuilée : mer, désert, cols, villes — contrôle le QG Tripoli ou Casablanca",
            True,
            (130, 120, 100),
        ),
        (12, MAP_H + 38),
    )


def draw_overlay(surface, state):
    if not state["result"]:
        return
    ov = pygame.Surface((MAP_W, MAP_H))
    ov.set_alpha(170)
    ov.fill((0, 0, 0))
    surface.blit(ov, (0, 0))
    txt = "VICTOIRE" if state["result"] == "victoire" else "DÉFAITE"
    col = (100, 220, 120) if state["result"] == "victoire" else (230, 90, 70)
    t = pygame.font.SysFont(None, 64).render(txt, True, col)
    surface.blit(t, (MAP_W // 2 - t.get_width() // 2, MAP_H // 2 - 30))


def run_menu(screen):
    clock = pygame.time.Clock()
    tick = 0
    preview = init_game(TEAM_ALLIES)
    while True:
        tick += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return TEAM_ALLIES
                if event.key == pygame.K_2:
                    return TEAM_AXIS
        draw_map(screen, preview, tick)
        for u in preview["units"]:
            draw_unit(screen, u)
        box = pygame.Rect(MAP_W // 2 - 200, MAP_H // 2 - 70, 400, 140)
        pygame.draw.rect(screen, (35, 30, 22), box, border_radius=10)
        pygame.draw.rect(screen, (110, 95, 65), box, 2, border_radius=10)
        f = pygame.font.SysFont(None, 28)
        for i, line in enumerate(
            ["[1] Alliés", "[2] Afrika Korps", "Carte réelle : Maroc → Égypte"]
        ):
            t = f.render(line, True, (230, 210, 170))
            screen.blit(t, (box.centerx - t.get_width() // 2, box.top + 20 + i * 36))
        pygame.display.flip()
        clock.tick(60)


def end_turn(state):
    player = state["player"]
    enemy = enemy_team(player)
    if state["turn"] == "player":
        state["turn"] = "ai"
        state["ai_step"] = 45
        reset_mp_for_team(state["units"], enemy)
    else:
        pass


def finish_ai_turn(state):
    enemy = enemy_team(state["player"])
    n = ai_play(state)
    add_log(state, f"IA : {n} unité(s) active(s).")
    r = city_reinforcements(state, enemy)
    if r:
        add_log(state, f"Renforts axe : {r} ville(s).")
    state["result"] = check_victory(state)
    if not state["result"]:
        state["turn_num"] += 1
        state["turn"] = "player"
        reset_mp_for_team(state["units"], state["player"])
        r2 = city_reinforcements(state, state["player"])
        if r2:
            add_log(state, f"Tes renforts : {r2} ville(s).")
    state["selected"] = None
    state["reachable"] = {}


def handle_click(state, gx, gy):
    if state["result"] or state["turn"] != "player":
        return
    units = state["units"]
    player = state["player"]
    unit = unit_at(units, gx, gy)
    sel = state.get("selected")

    if sel is None:
        if unit and unit["team"] == player and not unit["moved"]:
            state["selected"] = unit
            state["reachable"] = compute_reachable(state, unit)
            add_log(state, f"Ordre à {UNIT_STATS[unit['type']]['label']} ({unit['gx']},{unit['gy']})")
        return

    if unit and unit["id"] == sel["id"]:
        state["selected"] = None
        state["reachable"] = {}
        return

    if unit and unit["team"] == player and not unit["moved"]:
        state["selected"] = unit
        state["reachable"] = compute_reachable(state, unit)
        return

    if (gx, gy) in state["reachable"]:
        other = unit_at(units, gx, gy)
        if other and other["team"] != player:
            fight(state, sel, other)
            sel["moved"] = True
            sel["mp_left"] = 0
        else:
            state["_reach_cache"] = state["reachable"]
            move_unit(state, sel, gx, gy)
        state["selected"] = None
        state["reachable"] = {}
        state.pop("_reach_cache", None)
        state["result"] = check_victory(state)
        return

    add_log(state, "Ordre impossible sur cette case.")


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Afrique du Nord 1942 — carte stratégique")
    clock = pygame.time.Clock()
    tick = 0

    player = run_menu(screen)
    state = init_game(player)
    city_reinforcements(state, player)

    running = True
    while running:
        tick += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif state["result"] and event.key == pygame.K_r:
                    state = init_game(player)
                    city_reinforcements(state, player)
                elif state["turn"] == "player" and not state["result"] and event.key == pygame.K_SPACE:
                    end_turn(state)
                elif state["turn"] == "player" and not state["result"] and event.key == pygame.K_TAB:
                    sel = state.get("selected")
                    if sel:
                        sel["moved"] = True
                        state["selected"] = None
                        state["reachable"] = {}
            elif event.type == pygame.MOUSEMOTION:
                state["hover"] = pos_to_cell(*event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                cell = pos_to_cell(*event.pos)
                if cell:
                    handle_click(state, *cell)

        if state["turn"] == "ai" and not state["result"]:
            state["ai_step"] -= 1
            if state["ai_step"] <= 0:
                finish_ai_turn(state)

        if state["combat_fx"] > 0:
            state["combat_fx"] -= 1

        draw_map(screen, state, tick)
        for u in state["units"]:
            if u["hp"] > 0:
                draw_unit(screen, u)
        draw_panel(screen, state)
        draw_hud(screen, state)
        draw_overlay(screen, state)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit(0)


if __name__ == "__main__":
    main()
