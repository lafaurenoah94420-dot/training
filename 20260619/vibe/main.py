"""Nahla Tower Defense — aspirateurs vs Nahla."""

import math
import random
import struct
import sys
from pathlib import Path

import pygame

# --- Écran ---
WIDTH, HEIGHT = 1280, 720
PLAY_H = 580
UI_H = HEIGHT - PLAY_H
FPS = 60
TITLE = "Nahla Tower Defense"

ASSETS = Path(__file__).parent
NAHLA_IMG = ASSETS / "nahla_head.png"

# --- Couleurs ---
BG = (32, 28, 38)
FLOOR = (48, 42, 52)
PATH = (62, 56, 68)
PATH_EDGE = (78, 72, 84)
WALL = (28, 24, 32)
TEXT = (245, 238, 225)
MUTED = (150, 140, 155)
ACCENT = (255, 168, 72)
DANGER = (220, 80, 80)
OK = (100, 210, 140)
GOLD = (255, 210, 80)
PANEL = (40, 36, 48)
PANEL_HI = (58, 52, 66)

START_LIVES = 15
START_MONEY = 200
PATH_W = 44
BUILD_R = 22
MAX_UPGRADE_LEVEL = 3

MENU = "menu"
MAP_SELECT = "map_select"
PLAYING = "playing"
GAME_OVER = "game_over"
WIN = "win"

# --- Tours Nahla ---
TOWER_TYPES = {
    "soldat": {
        "name": "Soldat",
        "cost": 55,
        "range": 105,
        "damage": 11,
        "slow": 0.2,
        "fire_rate": 32,
        "income": 0,
        "desc": "Fusil — tire et ralentit",
        "ring": (75, 88, 55),
        "scale": 0.9,
        "helmet": True,
        "rifle": True,
    },
    "grondeuse": {
        "name": "Grondeuse",
        "cost": 70,
        "range": 115,
        "damage": 14,
        "slow": 0,
        "fire_rate": 38,
        "income": 0,
        "desc": "Crache du mépris (dégâts)",
        "ring": (255, 120, 90),
        "scale": 0.9,
    },
    "paresseuse": {
        "name": "Paresseuse",
        "cost": 95,
        "range": 75,
        "damage": 38,
        "slow": 0.15,
        "fire_rate": 70,
        "income": 0,
        "desc": "Gros coups lents",
        "ring": (180, 140, 255),
        "scale": 1.05,
    },
    "banquiere": {
        "name": "Banquière",
        "cost": 65,
        "range": 0,
        "damage": 0,
        "slow": 0,
        "fire_rate": 0,
        "income": 4,
        "desc": "+croquettes / seconde",
        "ring": (255, 210, 80),
        "scale": 0.8,
    },
    "reine": {
        "name": "Reine",
        "cost": 150,
        "range": 130,
        "damage": 9,
        "slow": 0.35,
        "fire_rate": 42,
        "income": 0,
        "desc": "Ralentit + dégâts",
        "ring": (255, 90, 160),
        "scale": 1.15,
    },
    "sniper": {
        "name": "Sniper",
        "cost": 90,
        "range": 210,
        "damage": 48,
        "slow": 0,
        "fire_rate": 95,
        "income": 0,
        "desc": "Longue portée, critique",
        "ring": (60, 75, 95),
        "scale": 0.95,
        "scope": True,
    },
    "general": {
        "name": "Général",
        "cost": 120,
        "range": 0,
        "damage": 0,
        "slow": 0,
        "fire_rate": 0,
        "income": 0,
        "desc": "Buff les alliés proches",
        "ring": (220, 185, 60),
        "scale": 1.0,
        "general": True,
        "buff_range": 115,
        "buff_damage": 1.3,
        "buff_range_mul": 1.18,
    },
}

# --- Aspirateurs ---
ENEMY_TYPES = {
    "classique": {
        "name": "Classique",
        "hp_base": 45,
        "speed": 1.35,
        "reward": 12,
        "color": (100, 100, 110),
        "pipe": (70, 70, 78),
        "radius": 16,
    },
    "rapide": {
        "name": "Rapide",
        "hp_base": 28,
        "speed": 2.6,
        "reward": 18,
        "color": (200, 90, 90),
        "pipe": (150, 60, 60),
        "radius": 12,
    },
    "tank": {
        "name": "Tank",
        "hp_base": 140,
        "speed": 0.75,
        "reward": 30,
        "color": (70, 75, 90),
        "pipe": (50, 55, 65),
        "radius": 22,
    },
    "silencieux": {
        "name": "Silencieux",
        "hp_base": 55,
        "speed": 1.9,
        "reward": 22,
        "color": (130, 100, 180),
        "pipe": (90, 70, 130),
        "radius": 14,
        "slow_immune": True,
    },
    "mega": {
        "name": "Méga",
        "hp_base": 500,
        "speed": 0.55,
        "reward": 120,
        "color": (50, 50, 60),
        "pipe": (30, 30, 38),
        "radius": 28,
    },
}

# --- Maps ---
MAPS = [
    {
        "id": "couloir",
        "name": "Couloir",
        "subtitle": "Chemin droit — idéal pour débuter",
        "waypoints": [(60, 290), (350, 290), (350, 120), (750, 120), (750, 420), (1180, 420)],
        "build_spots": [
            (180, 220), (180, 360), (280, 180), (450, 200), (450, 360),
            (520, 80), (620, 180), (850, 80), (850, 200), (650, 480),
            (950, 360), (1050, 480), (1100, 300),
        ],
        "floor": (50, 44, 54),
        "rug": (72, 52, 48),
    },
    {
        "id": "salon",
        "name": "Salon",
        "subtitle": "Virages serrés — placement tactique",
        "waypoints": [(60, 450), (300, 450), (300, 150), (600, 150), (600, 350), (900, 350), (900, 80), (1180, 80)],
        "build_spots": [
            (150, 380), (150, 520), (220, 250), (400, 220), (400, 80),
            (480, 420), (520, 250), (700, 220), (700, 420), (780, 150),
            (820, 280), (1000, 150), (1000, 420), (1050, 280), (1100, 160),
        ],
        "floor": (55, 48, 42),
        "rug": (88, 62, 52),
    },
    {
        "id": "cuisine",
        "name": "Cuisine",
        "subtitle": "Labyrinthe — vagues brutales",
        "waypoints": [(60, 100), (250, 100), (250, 480), (500, 480), (500, 200), (750, 200), (750, 400), (980, 400), (980, 100), (1180, 100)],
        "build_spots": [
            (120, 200), (120, 350), (200, 50), (350, 180), (350, 400),
            (400, 520), (580, 520), (580, 350), (620, 130), (850, 130),
            (850, 300), (850, 480), (900, 250), (1050, 200), (1050, 350), (1100, 50),
        ],
        "floor": (46, 50, 48),
        "rug": (65, 70, 62),
    },
]

MAX_WAVES = 20

HELMET_MAIN = (72, 85, 52)
HELMET_DARK = (52, 62, 38)
HELMET_RIM = (45, 54, 32)
HELMET_SHINE = (100, 115, 72)


def add_soldier_helmet(sprite):
    """Casque militaire dessiné sur la tête de Nahla."""
    size = sprite.get_width()
    surf = sprite.copy()
    cx = size // 2
    lift = int(size * 0.05)  # décalage vers le haut

    # Dôme du casque (couvre le haut de la tête)
    dome_w = int(size * 0.92)
    dome_h = int(size * 0.48)
    dome_rect = pygame.Rect(cx - dome_w // 2, int(size * 0.02) - lift, dome_w, dome_h)
    pygame.draw.ellipse(surf, HELMET_MAIN, dome_rect)
    pygame.draw.ellipse(surf, HELMET_DARK, dome_rect, 2)

    # Reflet
    shine_rect = pygame.Rect(cx - dome_w // 4, int(size * 0.08) - lift, dome_w // 3, dome_h // 3)
    pygame.draw.ellipse(surf, HELMET_SHINE, shine_rect)

    # Bord / visière du casque
    brim_y = int(size * 0.38) - lift
    brim_rect = pygame.Rect(cx - int(size * 0.52), brim_y, int(size * 1.04), int(size * 0.12))
    pygame.draw.ellipse(surf, HELMET_RIM, brim_rect)
    pygame.draw.line(surf, HELMET_DARK, (cx - int(size * 0.5), brim_y + 4), (cx + int(size * 0.5), brim_y + 4), 2)

    # Insigne militaire (étoile simplifiée)
    star_y = int(size * 0.22) - lift
    pygame.draw.circle(surf, (200, 190, 80), (cx, star_y), 5)
    for angle in range(0, 360, 72):
        rad = math.radians(angle - 90)
        x2 = cx + int(math.cos(rad) * 7)
        y2 = star_y + int(math.sin(rad) * 7)
        pygame.draw.line(surf, (200, 190, 80), (cx, star_y), (x2, y2), 2)

    # Sangle sous le menton (suggestion)
    pygame.draw.arc(surf, HELMET_DARK, pygame.Rect(cx - int(size * 0.3), int(size * 0.55) - lift, int(size * 0.6), int(size * 0.25)), math.pi * 0.15, math.pi * 0.85, 2)

    return surf


def add_soldier_rifle(sprite):
    """Fusil d'assaut dessiné sur le côté de Nahla."""
    size = sprite.get_width()
    surf = sprite.copy()
    cx, cy = size // 2, size // 2
    gun = (42, 46, 38)
    metal = (95, 100, 92)
    wood = (68, 50, 34)

    # Crosse
    pygame.draw.rect(surf, wood, (cx - int(size * 0.18), cy + int(size * 0.08), int(size * 0.14), int(size * 0.1)), border_radius=2)
    # Corps
    pygame.draw.rect(surf, gun, (cx - int(size * 0.06), cy + int(size * 0.06), int(size * 0.38), int(size * 0.13)), border_radius=2)
    # Canon
    pygame.draw.rect(surf, metal, (cx + int(size * 0.28), cy + int(size * 0.09), int(size * 0.32), int(size * 0.07)), border_radius=1)
    # Chargeur
    pygame.draw.rect(surf, gun, (cx + int(size * 0.08), cy + int(size * 0.17), int(size * 0.08), int(size * 0.1)), border_radius=1)
    # Poignée
    pygame.draw.rect(surf, wood, (cx + int(size * 0.02), cy + int(size * 0.17), int(size * 0.07), int(size * 0.09)), border_radius=1)

    return surf


def add_sniper_scope(sprite):
    """Lunette de sniper sur Nahla."""
    size = sprite.get_width()
    surf = sprite.copy()
    cx, cy = size // 2, size // 2
    scope = (35, 40, 48)
    glass = (80, 160, 200)
    lift = int(size * 0.04)

    pygame.draw.circle(surf, scope, (cx, cy - lift), int(size * 0.22), 3)
    pygame.draw.circle(surf, glass, (cx, cy - lift), int(size * 0.14))
    pygame.draw.circle(surf, (20, 25, 30), (cx, cy - lift), int(size * 0.06))
    pygame.draw.rect(surf, scope, (cx - int(size * 0.06), cy - lift - int(size * 0.32), int(size * 0.12), int(size * 0.14)))
    pygame.draw.line(surf, scope, (cx, cy - lift), (cx + int(size * 0.35), cy + int(size * 0.05)), 3)
    return surf


def add_general_insignia(sprite):
    """Épaulettes et médailles du Général Nahla."""
    size = sprite.get_width()
    surf = sprite.copy()
    cx, cy = size // 2, size // 2
    gold = (230, 195, 70)
    red = (180, 50, 50)

    pygame.draw.rect(surf, gold, (cx - int(size * 0.42), cy + int(size * 0.12), int(size * 0.18), int(size * 0.1)), border_radius=2)
    pygame.draw.rect(surf, gold, (cx + int(size * 0.24), cy + int(size * 0.12), int(size * 0.18), int(size * 0.1)), border_radius=2)
    for dx in (-int(size * 0.12), int(size * 0.12)):
        pygame.draw.circle(surf, red, (cx + dx, cy + int(size * 0.22)), 5)
        pygame.draw.circle(surf, gold, (cx + dx, cy + int(size * 0.22)), 5, 1)
    pygame.draw.polygon(surf, gold, [(cx, int(size * 0.05)), (cx - 8, int(size * 0.18)), (cx + 8, int(size * 0.18))])
    return surf


def load_nahla_sprites():
    base = None
    if NAHLA_IMG.exists():
        base = pygame.image.load(str(NAHLA_IMG)).convert_alpha()
    sprites = {}
    for key, cfg in TOWER_TYPES.items():
        size = int(48 * cfg["scale"])
        if base is not None:
            img = pygame.transform.smoothscale(base, (size, size))
            if cfg.get("helmet"):
                img = add_soldier_helmet(img)
            if cfg.get("rifle"):
                img = add_soldier_rifle(img)
            if cfg.get("scope"):
                img = add_sniper_scope(img)
            if cfg.get("general"):
                img = add_general_insignia(img)
            sprites[key] = img
        else:
            surf = pygame.Surface((size, size), pygame.SRCALPHA)
            pygame.draw.circle(surf, cfg["ring"], (size // 2, size // 2), size // 2)
            if cfg.get("helmet"):
                surf = add_soldier_helmet(surf)
            if cfg.get("rifle"):
                surf = add_soldier_rifle(surf)
            if cfg.get("scope"):
                surf = add_sniper_scope(surf)
            if cfg.get("general"):
                surf = add_general_insignia(surf)
            sprites[key] = surf
    return sprites


def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def draw_text(surf, text, pos, size=22, color=TEXT, center=False, bold=False):
    font = pygame.font.SysFont("arial", size, bold=bold)
    img = font.render(text, True, color)
    rect = img.get_rect()
    if center:
        rect.center = pos
    else:
        rect.topleft = pos
    surf.blit(img, rect)
    return rect


def draw_path(surface, waypoints, path_w=PATH_W):
    if len(waypoints) < 2:
        return
    for i in range(len(waypoints) - 1):
        pygame.draw.line(surface, PATH_EDGE, waypoints[i], waypoints[i + 1], path_w + 8)
    for i in range(len(waypoints) - 1):
        pygame.draw.line(surface, PATH, waypoints[i], waypoints[i + 1], path_w)
    for pt in waypoints:
        pygame.draw.circle(surface, PATH_EDGE, pt, path_w // 2 + 4)
        pygame.draw.circle(surface, PATH, pt, path_w // 2)


def draw_build_spot(surface, pos, occupied=False, hover=False):
    color = (80, 70, 55) if not occupied else (55, 50, 45)
    if hover and not occupied:
        color = (110, 95, 70)
    pygame.draw.circle(surface, color, pos, BUILD_R)
    pygame.draw.circle(surface, (100, 88, 65), pos, BUILD_R, 2)


def draw_enemy(surface, enemy):
    cfg = ENEMY_TYPES[enemy["kind"]]
    x, y = int(enemy["x"]), int(enemy["y"])
    r = cfg["radius"]
    pygame.draw.circle(surface, cfg["color"], (x, y), r)
    pygame.draw.circle(surface, cfg["pipe"], (x - r // 2, y), r // 3)
    pygame.draw.rect(surface, (200, 200, 210), (x + r // 3, y - r // 4, r, r // 2), border_radius=3)
    # Barre de vie
    ratio = max(0, enemy["hp"] / enemy["max_hp"])
    bar_w = r * 2
    pygame.draw.rect(surface, (40, 40, 45), (x - r, y - r - 10, bar_w, 5))
    pygame.draw.rect(surface, OK if ratio > 0.4 else DANGER, (x - r, y - r - 10, int(bar_w * ratio), 5))


def draw_tower(surface, tower, sprites, selected=False, buffed=False):
    cfg = TOWER_TYPES[tower["kind"]]
    x, y = tower["x"], tower["y"]
    sprite = sprites[tower["kind"]]
    rect = sprite.get_rect(center=(x, y))
    if buffed:
        pygame.draw.circle(surface, (220, 185, 60), (x, y), BUILD_R + 10, 2)
    if selected:
        pygame.draw.circle(surface, cfg["ring"], (x, y), BUILD_R + 6, 3)
    pygame.draw.circle(surface, cfg["ring"], (x, y), BUILD_R + 2, 2)
    surface.blit(sprite, rect)
    level = tower.get("level", 1)
    if level > 1:
        for i in range(level):
            pygame.draw.circle(surface, GOLD, (x - 8 + i * 8, y - BUILD_R - 6), 3)


class SoundBank:
    """Sons générés en code — pas de fichiers externes."""

    def __init__(self):
        if not pygame.mixer.get_init():
            pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
        self.enabled = True
        self.sfx = {
            "rifle": self._tone(180, 55, 0.35, sweep_end=90),
            "sniper": self._noise_burst(120, 0.5),
            "meow": self._meow(),
            "place": self._chime([520, 780], 90, 0.25),
            "upgrade": self._chime([440, 660, 880], 140, 0.3),
            "kill": self._tone(320, 70, 0.2, decay_fast=True),
            "wave": self._chime([220, 330, 440, 550], 200, 0.35),
            "buff": self._tone(660, 100, 0.15),
            "hurt": self._tone(110, 180, 0.4, shape="square"),
            "coin": self._chime([880, 1100], 60, 0.18),
            "vacuum": self._hum(),
        }

    def _pack(self, samples):
        return pygame.mixer.Sound(buffer=b"".join(struct.pack("<hh", s, s) for s in samples))

    def _tone(self, freq, ms, vol, sweep_end=None, decay_fast=False, shape="sine"):
        rate = 22050
        n = int(rate * ms / 1000)
        out = []
        for i in range(n):
            t = i / rate
            f = freq + (sweep_end - freq) * (i / n) if sweep_end else freq
            if shape == "sine":
                v = math.sin(2 * math.pi * f * t)
            else:
                v = 1.0 if math.sin(2 * math.pi * f * t) > 0 else -1.0
            attack = min(1.0, i / (rate * 0.004))
            decay = 1 - (i / n) ** (2.5 if decay_fast else 1.2)
            sample = int(32767 * vol * attack * decay * v)
            out.append(max(-32767, min(32767, sample)))
        return self._pack(out)

    def _chime(self, freqs, ms, vol):
        rate = 22050
        n = int(rate * ms / 1000)
        out = [0] * n
        for freq in freqs:
            for i in range(n):
                t = i / rate
                env = min(1.0, i / (rate * 0.008)) * (1 - i / n)
                out[i] += int(32767 * vol * env * math.sin(2 * math.pi * freq * t) / len(freqs))
        return self._pack([max(-32767, min(32767, s)) for s in out])

    def _meow(self):
        rate = 22050
        ms = 220
        n = int(rate * ms / 1000)
        out = []
        for i in range(n):
            t = i / rate
            f = 820 - 380 * (i / n) + 40 * math.sin(t * 28)
            env = math.sin(math.pi * i / n) ** 1.4
            v = math.sin(2 * math.pi * f * t)
            out.append(int(32767 * 0.28 * env * v))
        return self._pack(out)

    def _noise_burst(self, ms, vol):
        rate = 22050
        n = int(rate * ms / 1000)
        out = []
        for i in range(n):
            env = (1 - i / n) ** 1.5
            v = random.uniform(-1, 1) * env
            v += 0.4 * math.sin(2 * math.pi * 120 * i / rate)
            out.append(int(32767 * vol * v))
        return self._pack([max(-32767, min(32767, s)) for s in out])

    def _hum(self):
        rate = 22050
        ms = 300
        n = int(rate * ms / 1000)
        out = []
        for i in range(n):
            t = i / rate
            v = 0.5 * math.sin(2 * math.pi * 55 * t) + 0.3 * math.sin(2 * math.pi * 82 * t)
            env = min(1.0, i / (rate * 0.02)) * (1 - i / n)
            out.append(int(32767 * 0.12 * env * v))
        return self._pack(out)

    def play(self, name):
        if self.enabled and name in self.sfx:
            self.sfx[name].play()


def wave_plan(wave_num):
    """Composition de la vague selon le numéro."""
    plan = []
    count = 5 + wave_num * 2
    for _ in range(count):
        plan.append("classique")
    if wave_num >= 2:
        plan += ["rapide"] * (1 + wave_num // 2)
    if wave_num >= 4:
        plan += ["tank"] * (wave_num // 4)
    if wave_num >= 6:
        plan += ["silencieux"] * (1 + wave_num // 5)
    if wave_num % 5 == 0:
        plan += ["mega"] * (wave_num // 5)
    random.shuffle(plan)
    return plan


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.nahla_sprites = load_nahla_sprites()
        self.sounds = SoundBank()
        self.reset_all()

    def reset_all(self):
        self.state = MENU
        self.map_index = 0
        self.reset_run()

    def reset_run(self):
        self.lives = START_LIVES
        self.money = START_MONEY
        self.score = 0
        self.wave = 0
        self.wave_active = False
        self.wave_queue = []
        self.spawn_timer = 0
        self.spawn_interval = 55
        self.enemies = []
        self.towers = []
        self.selected_tower_type = "soldat"
        self.hover_spot = None
        self.message = ""
        self.message_timer = 0
        self.between_waves_timer = 90
        self.income_timer = 0
        self.shots = []

    def current_map(self):
        return MAPS[self.map_index]

    def hp_scale(self):
        return 1.0 + self.wave * 0.18

    def speed_scale(self):
        return 1.0 + self.wave * 0.04

    def spawn_enemy(self, kind):
        cfg = ENEMY_TYPES[kind]
        hp = int(cfg["hp_base"] * self.hp_scale())
        self.enemies.append({
            "kind": kind,
            "hp": hp,
            "max_hp": hp,
            "speed": cfg["speed"] * self.speed_scale(),
            "reward": cfg["reward"],
            "wp": 0,
            "x": float(self.current_map()["waypoints"][0][0]),
            "y": float(self.current_map()["waypoints"][0][1]),
            "slow_timer": 0,
            "slow_factor": 1.0,
        })
        if kind in ("rapide", "mega"):
            self.sounds.play("vacuum")

    def start_wave(self):
        if self.wave_active or self.wave >= MAX_WAVES:
            return
        self.wave += 1
        self.wave_queue = wave_plan(self.wave)
        self.wave_active = True
        self.spawn_timer = 0
        self.spawn_interval = max(22, 60 - self.wave * 2)
        self.sounds.play("wave")
        self.set_message(f"Vague {self.wave} !")

    def set_message(self, text, duration=120):
        self.message = text
        self.message_timer = duration

    def nearest_build_spot(self, pos):
        best, best_d = None, BUILD_R + 8
        for spot in self.current_map()["build_spots"]:
            d = dist(pos, spot)
            if d < best_d:
                best, best_d = spot, d
        return best

    def spot_occupied(self, spot):
        for t in self.towers:
            if t["x"] == spot[0] and t["y"] == spot[1]:
                return True
        return False

    def tower_at_spot(self, spot):
        for t in self.towers:
            if t["x"] == spot[0] and t["y"] == spot[1]:
                return t
        return None

    def is_buffed(self, tower):
        if tower["kind"] == "general":
            return False
        for other in self.towers:
            if other["kind"] != "general":
                continue
            gcfg = TOWER_TYPES["general"]
            glvl = other.get("level", 1)
            buff_range = gcfg["buff_range"] * (1 + 0.12 * (glvl - 1))
            if dist((tower["x"], tower["y"]), (other["x"], other["y"])) <= buff_range:
                return True
        return False

    def get_tower_stats(self, tower):
        cfg = TOWER_TYPES[tower["kind"]]
        level = tower.get("level", 1)
        dmg_mul = 1 + (level - 1) * 0.28
        range_mul = 1 + (level - 1) * 0.14
        fire_mul = max(0.55, 1 - (level - 1) * 0.12)
        income_bonus = (level - 1) * 2

        for other in self.towers:
            if other is tower or other["kind"] != "general":
                continue
            gcfg = TOWER_TYPES["general"]
            glvl = other.get("level", 1)
            buff_range = gcfg["buff_range"] * (1 + 0.12 * (glvl - 1))
            if dist((tower["x"], tower["y"]), (other["x"], other["y"])) <= buff_range:
                dmg_mul *= gcfg["buff_damage"] + 0.08 * (glvl - 1)
                range_mul *= gcfg["buff_range_mul"] + 0.05 * (glvl - 1)

        return {
            "damage": cfg["damage"] * dmg_mul,
            "range": cfg["range"] * range_mul,
            "fire_rate": max(8, int(cfg["fire_rate"] * fire_mul)) if cfg["fire_rate"] else 0,
            "slow": cfg["slow"],
            "income": cfg["income"] + income_bonus,
        }

    def upgrade_cost(self, tower):
        base = TOWER_TYPES[tower["kind"]]["cost"]
        level = tower.get("level", 1)
        return int(base * 0.65 * level)

    def try_upgrade_tower(self, spot):
        tower = self.tower_at_spot(spot)
        if tower is None:
            return
        level = tower.get("level", 1)
        if level >= MAX_UPGRADE_LEVEL:
            self.set_message("Niveau max atteint")
            return
        cost = self.upgrade_cost(tower)
        if self.money < cost:
            self.set_message(f"Amélioration : {cost} croquettes")
            return
        self.money -= cost
        tower["level"] = level + 1
        self.sounds.play("upgrade")
        self.set_message(f"{TOWER_TYPES[tower['kind']]['name']} → niveau {tower['level']}")

    def try_place_tower(self, spot):
        if self.spot_occupied(spot):
            self.set_message("Déjà occupé")
            return
        cfg = TOWER_TYPES[self.selected_tower_type]
        if self.money < cfg["cost"]:
            self.set_message("Pas assez de croquettes")
            return
        self.money -= cfg["cost"]
        self.towers.append({
            "kind": self.selected_tower_type,
            "x": spot[0],
            "y": spot[1],
            "cooldown": 0,
            "income_timer": 0,
            "level": 1,
        })
        self.sounds.play("meow")
        self.sounds.play("place")
        if self.selected_tower_type == "general":
            self.sounds.play("buff")
        self.set_message(f"{cfg['name']} placée")

    def sell_tower_at(self, spot):
        for i, t in enumerate(self.towers):
            if t["x"] == spot[0] and t["y"] == spot[1]:
                refund = TOWER_TYPES[t["kind"]]["cost"] // 2
                self.money += refund
                del self.towers[i]
                self.set_message(f"Vendue (+{refund})")
                return

    def update_enemies(self):
        wps = self.current_map()["waypoints"]
        for enemy in self.enemies[:]:
            if enemy["slow_timer"] > 0:
                enemy["slow_timer"] -= 1
            else:
                enemy["slow_factor"] = 1.0

            speed = enemy["speed"] * enemy["slow_factor"]
            target = wps[enemy["wp"] + 1] if enemy["wp"] + 1 < len(wps) else None
            if target is None:
                self.enemies.remove(enemy)
                self.lives -= 1
                self.sounds.play("hurt")
                self.set_message("Aspirateur arrivé ! -1 vie", 90)
                if self.lives <= 0:
                    self.state = GAME_OVER
                    self.sounds.play("hurt")
                continue

            dx = target[0] - enemy["x"]
            dy = target[1] - enemy["y"]
            d = math.hypot(dx, dy)
            if d < speed:
                enemy["x"], enemy["y"] = float(target[0]), float(target[1])
                enemy["wp"] += 1
            else:
                enemy["x"] += dx / d * speed
                enemy["y"] += dy / d * speed

            if enemy["hp"] <= 0:
                self.money += enemy["reward"]
                self.score += enemy["reward"]
                self.sounds.play("kill")
                self.sounds.play("coin")
                self.enemies.remove(enemy)

    def update_towers(self):
        for tower in self.towers:
            cfg = TOWER_TYPES[tower["kind"]]
            stats = self.get_tower_stats(tower)

            if stats["income"] > 0:
                tower["income_timer"] += 1
                if tower["income_timer"] >= 60:
                    tower["income_timer"] = 0
                    self.money += stats["income"]

            if cfg.get("general"):
                continue

            if stats["damage"] <= 0 and stats["slow"] <= 0:
                continue

            tower["cooldown"] = max(0, tower["cooldown"] - 1)
            if tower["cooldown"] > 0:
                continue

            target = None
            best_prog = -1
            for enemy in self.enemies:
                if dist((tower["x"], tower["y"]), (enemy["x"], enemy["y"])) <= stats["range"]:
                    prog = enemy["wp"] + enemy["x"] / 10000
                    if prog > best_prog:
                        best_prog = prog
                        target = enemy

            if target is None:
                continue

            if stats["damage"] > 0:
                target["hp"] -= stats["damage"]
                tower["cooldown"] = stats["fire_rate"]
                if tower["kind"] == "soldat":
                    self.sounds.play("rifle")
                    self.shots.append({
                        "x1": tower["x"] + 12,
                        "y1": tower["y"] + 8,
                        "x2": target["x"],
                        "y2": target["y"],
                        "timer": 10,
                        "color": (255, 230, 100),
                    })
                elif tower["kind"] == "sniper":
                    self.sounds.play("sniper")
                    self.shots.append({
                        "x1": tower["x"],
                        "y1": tower["y"],
                        "x2": target["x"],
                        "y2": target["y"],
                        "timer": 14,
                        "color": (120, 220, 255),
                        "thick": 3,
                    })

            if stats["slow"] > 0 and not ENEMY_TYPES[target["kind"]].get("slow_immune"):
                target["slow_factor"] = 1.0 - stats["slow"]
                target["slow_timer"] = 45

    def update_shots(self):
        for shot in self.shots[:]:
            shot["timer"] -= 1
            if shot["timer"] <= 0:
                self.shots.remove(shot)

    def draw_shots(self):
        for shot in self.shots:
            color = shot.get("color", (255, 230, 100))
            thick = shot.get("thick", 2)
            pygame.draw.line(self.screen, color, (shot["x1"], shot["y1"]), (shot["x2"], shot["y2"]), thick)
            pygame.draw.circle(self.screen, color, (int(shot["x2"]), int(shot["y2"])), 4)

    def update_wave(self):
        if not self.wave_active:
            if self.wave < MAX_WAVES and not self.enemies:
                self.between_waves_timer -= 1
                if self.between_waves_timer <= 0:
                    self.start_wave()
            return

        if self.wave_queue:
            self.spawn_timer += 1
            if self.spawn_timer >= self.spawn_interval:
                self.spawn_timer = 0
                kind = self.wave_queue.pop(0)
                self.spawn_enemy(kind)
        elif not self.enemies:
            self.wave_active = False
            self.between_waves_timer = 150
            if self.wave >= MAX_WAVES:
                self.state = WIN
                self.sounds.play("upgrade")
            else:
                self.set_message(f"Vague {self.wave} terminée — prépare-toi")

    def handle_click_playing(self, pos, button):
        if pos[1] >= PLAY_H:
            self.handle_ui_click(pos)
            return
        spot = self.nearest_build_spot(pos)
        if spot is None:
            return
        if button == 1:
            self.try_place_tower(spot)
        elif button == 2:
            self.try_upgrade_tower(spot)
        elif button == 3:
            self.sell_tower_at(spot)

    def handle_ui_click(self, pos):
        keys = list(TOWER_TYPES.keys())
        slot_w = WIDTH // len(keys)
        idx = pos[0] // slot_w
        if 0 <= idx < len(keys):
            self.selected_tower_type = keys[idx]

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.state == PLAYING:
                        self.state = MAP_SELECT
                    else:
                        return False
                if self.state == MENU and event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    self.state = MAP_SELECT
                if self.state == MAP_SELECT and event.key in (pygame.K_1, pygame.K_2, pygame.K_3):
                    self.map_index = event.key - pygame.K_1
                    self.reset_run()
                    self.state = PLAYING
                    self.between_waves_timer = 120
                if self.state == PLAYING and event.key == pygame.K_SPACE:
                    if not self.wave_active:
                        self.between_waves_timer = 0
                if self.state == PLAYING and event.key == pygame.K_u:
                    if self.hover_spot:
                        self.try_upgrade_tower(self.hover_spot)
                if self.state in (GAME_OVER, WIN) and event.key == pygame.K_r:
                    self.state = MAP_SELECT
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.state == MENU:
                    self.state = MAP_SELECT
                elif self.state == MAP_SELECT:
                    self.handle_map_select_click(event.pos)
                elif self.state == PLAYING:
                    self.handle_click_playing(event.pos, event.button)
        return True

    def handle_map_select_click(self, pos):
        card_w, card_h = 340, 320
        gap = 40
        total_w = 3 * card_w + 2 * gap
        start_x = (WIDTH - total_w) // 2
        y = 200
        for i in range(3):
            x = start_x + i * (card_w + gap)
            rect = pygame.Rect(x, y, card_w, card_h)
            if rect.collidepoint(pos):
                self.map_index = i
                self.reset_run()
                self.state = PLAYING
                self.between_waves_timer = 120

    def update(self):
        if self.message_timer > 0:
            self.message_timer -= 1

        if self.state != PLAYING:
            return

        mx, my = pygame.mouse.get_pos()
        if my < PLAY_H:
            self.hover_spot = self.nearest_build_spot((mx, my))
        else:
            self.hover_spot = None

        self.update_towers()
        self.update_enemies()
        self.update_shots()
        self.update_wave()

    def draw_playfield(self):
        m = self.current_map()
        self.screen.fill(BG)
        pygame.draw.rect(self.screen, m["floor"], (0, 0, WIDTH, PLAY_H))
        # Tapis
        for i, spot in enumerate(m["build_spots"]):
            if i % 2 == 0:
                pygame.draw.circle(self.screen, m["rug"], spot, BUILD_R + 8, 0)

        draw_path(self.screen, m["waypoints"])

        for spot in m["build_spots"]:
            draw_build_spot(self.screen, spot, self.spot_occupied(spot), spot == self.hover_spot)

        for tower in self.towers:
            if tower["kind"] == "general":
                gcfg = TOWER_TYPES["general"]
                glvl = tower.get("level", 1)
                br = int(gcfg["buff_range"] * (1 + 0.12 * (glvl - 1)))
                aura = pygame.Surface((br * 2, br * 2), pygame.SRCALPHA)
                pygame.draw.circle(aura, (220, 185, 60, 35), (br, br), br)
                self.screen.blit(aura, (tower["x"] - br, tower["y"] - br))

        for tower in self.towers:
            draw_tower(self.screen, tower, self.nahla_sprites, buffed=self.is_buffed(tower))

        for enemy in self.enemies:
            draw_enemy(self.screen, enemy)

        self.draw_shots()

        # Portes départ / arrivée
        start = m["waypoints"][0]
        end = m["waypoints"][-1]
        draw_text(self.screen, "ENTRÉE", (start[0] - 30, start[1] - 35), 16, MUTED)
        draw_text(self.screen, "CANAPÉ", (end[0] - 30, end[1] - 35), 16, DANGER)

        if self.hover_spot and not self.spot_occupied(self.hover_spot):
            cfg = TOWER_TYPES[self.selected_tower_type]
            if cfg["range"] > 0:
                pygame.draw.circle(self.screen, cfg["ring"], self.hover_spot, int(cfg["range"]), 1)
        elif self.hover_spot and self.tower_at_spot(self.hover_spot):
            tower = self.tower_at_spot(self.hover_spot)
            stats = self.get_tower_stats(tower)
            if stats["range"] > 0:
                pygame.draw.circle(self.screen, TOWER_TYPES[tower["kind"]]["ring"], self.hover_spot, int(stats["range"]), 1)
            lvl = tower.get("level", 1)
            if lvl < MAX_UPGRADE_LEVEL:
                cost = self.upgrade_cost(tower)
                draw_text(self.screen, f"[U] Améliorer → niv.{lvl + 1} ({cost})", (WIDTH // 2, PLAY_H - 52), 18, GOLD, center=True)

    def draw_hud(self):
        pygame.draw.rect(self.screen, PANEL, (0, PLAY_H, WIDTH, UI_H))
        pygame.draw.line(self.screen, PANEL_HI, (0, PLAY_H), (WIDTH, PLAY_H), 2)

        draw_text(self.screen, f"Vies {self.lives}", (20, PLAY_H + 14), 24, OK if self.lives > 5 else DANGER, bold=True)
        draw_text(self.screen, f"Croquettes {self.money}", (20, PLAY_H + 44), 22, GOLD)
        draw_text(self.screen, f"Vague {self.wave}/{MAX_WAVES}", (240, PLAY_H + 14), 22)
        draw_text(self.screen, f"Score {self.score}", (240, PLAY_H + 44), 22, MUTED)
        draw_text(self.screen, self.current_map()["name"], (420, PLAY_H + 14), 22, ACCENT, bold=True)

        if not self.wave_active and self.wave < MAX_WAVES:
            secs = max(0, self.between_waves_timer // 60 + 1)
            draw_text(self.screen, f"Prochaine vague dans {secs}s  [ESPACE]", (420, PLAY_H + 44), 18, MUTED)
        elif self.wave_active:
            left = len(self.wave_queue) + len(self.enemies)
            draw_text(self.screen, f"Ennemis restants ~{left}", (420, PLAY_H + 44), 18, DANGER)

        if self.message and self.message_timer > 0:
            draw_text(self.screen, self.message, (WIDTH // 2, PLAY_H - 28), 22, ACCENT, center=True)

        # Slots tours
        keys = list(TOWER_TYPES.keys())
        slot_w = WIDTH // len(keys)
        for i, key in enumerate(keys):
            cfg = TOWER_TYPES[key]
            x = i * slot_w
            rect = pygame.Rect(x + 4, PLAY_H + 72, slot_w - 8, UI_H - 80)
            sel = key == self.selected_tower_type
            pygame.draw.rect(self.screen, PANEL_HI if sel else (50, 46, 58), rect, border_radius=8)
            if sel:
                pygame.draw.rect(self.screen, cfg["ring"], rect, 2, border_radius=8)

            sprite = self.nahla_sprites[key]
            sr = sprite.get_rect(center=(rect.centerx, rect.top + 28))
            self.screen.blit(sprite, sr)
            draw_text(self.screen, cfg["name"], (rect.centerx, rect.top + 50), 14, TEXT, center=True)
            draw_text(self.screen, f"{cfg['cost']}", (rect.centerx, rect.bottom - 18), 14, GOLD, center=True)

    def draw_menu(self):
        self.screen.fill(BG)
        draw_text(self.screen, "NAHLA TOWER DEFENSE", (WIDTH // 2, 180), 52, ACCENT, center=True, bold=True)
        draw_text(self.screen, "Les aspirateurs veulent le canapé. Place Nahla.", (WIDTH // 2, 250), 24, TEXT, center=True)
        draw_text(self.screen, "CLIQUE ou ENTRÉE pour commencer", (WIDTH // 2, 340), 22, MUTED, center=True)
        draw_text(self.screen, "Clic molette ou [U] sur une unité = améliorer", (WIDTH // 2, 375), 18, MUTED, center=True)

        y = 400
        for key, cfg in TOWER_TYPES.items():
            draw_text(self.screen, f"• {cfg['name']} — {cfg['desc']} ({cfg['cost']})", (WIDTH // 2, y), 18, MUTED, center=True)
            y += 28

    def draw_map_select(self):
        self.screen.fill(BG)
        draw_text(self.screen, "CHOISIS LA MAP", (WIDTH // 2, 80), 40, ACCENT, center=True, bold=True)
        draw_text(self.screen, "1 / 2 / 3 ou clic sur une carte", (WIDTH // 2, 130), 20, MUTED, center=True)

        card_w, card_h = 340, 320
        gap = 40
        total_w = 3 * card_w + 2 * gap
        start_x = (WIDTH - total_w) // 2
        y = 200

        for i, m in enumerate(MAPS):
            x = start_x + i * (card_w + gap)
            rect = pygame.Rect(x, y, card_w, card_h)
            pygame.draw.rect(self.screen, PANEL, rect, border_radius=12)
            pygame.draw.rect(self.screen, ACCENT if i == 1 else PANEL_HI, rect, 2, border_radius=12)

            mini = pygame.Surface((card_w - 40, 140))
            mini.fill(m["floor"])
            draw_path(mini, [(20, 70), (80, 70), (80, 30), (200, 30), (200, 110), (280, 110)] if i == 0 else
                             [(20, 110), (80, 110), (80, 30), (160, 30), (160, 80), (240, 80), (240, 20), (280, 20)] if i == 1 else
                             [(20, 20), (60, 20), (60, 120), (140, 120), (140, 50), (200, 50), (200, 100), (260, 100), (260, 20), (280, 20)],
                             path_w=16)
            self.screen.blit(mini, (x + 20, y + 20))

            draw_text(self.screen, m["name"], (rect.centerx, y + 175), 28, TEXT, center=True, bold=True)
            draw_text(self.screen, m["subtitle"], (rect.centerx, y + 210), 17, MUTED, center=True)
            draw_text(self.screen, f"[{i + 1}]", (rect.centerx, y + 270), 22, ACCENT, center=True)

    def draw_end(self, win=False):
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        self.screen.blit(overlay, (0, 0))
        title = "VICTOIRE — Nahla garde le canapé" if win else "GAME OVER — Les aspirateurs gagnent"
        color = OK if win else DANGER
        draw_text(self.screen, title, (WIDTH // 2, HEIGHT // 2 - 30), 36, color, center=True, bold=True)
        draw_text(self.screen, f"Score final : {self.score}", (WIDTH // 2, HEIGHT // 2 + 20), 24, TEXT, center=True)
        draw_text(self.screen, "R — choisir une autre map", (WIDTH // 2, HEIGHT // 2 + 60), 20, MUTED, center=True)

    def draw(self):
        if self.state == MENU:
            self.draw_menu()
        elif self.state == MAP_SELECT:
            self.draw_map_select()
        elif self.state == PLAYING:
            self.draw_playfield()
            self.draw_hud()
        elif self.state == GAME_OVER:
            self.draw_playfield()
            self.draw_hud()
            self.draw_end(False)
        elif self.state == WIN:
            self.draw_playfield()
            self.draw_hud()
            self.draw_end(True)
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    Game().run()
