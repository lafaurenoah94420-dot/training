"""Sprites des objets qui tombent sur Nahla."""

import pygame

OBJECT_SIZE = 48


def _blank():
    return pygame.Surface((OBJECT_SIZE, OBJECT_SIZE), pygame.SRCALPHA)


def make_brosse_sprite():
    surf = _blank()
    # Manche
    pygame.draw.rect(surf, (120, 75, 45), (20, 4, 8, 22), border_radius=3)
    pygame.draw.rect(surf, (90, 55, 30), (20, 4, 8, 22), 2, border_radius=3)
    # Poignée
    pygame.draw.ellipse(surf, (150, 95, 55), (18, 2, 12, 8))
    # Tête de brosse
    pygame.draw.rect(surf, (210, 170, 110), (14, 24, 20, 10), border_radius=4)
    # Poils
    for x in range(16, 33, 3):
        pygame.draw.line(surf, (240, 210, 150), (x, 34), (x, 44), 2)
    return surf


def make_reveil_sprite():
    surf = _blank()
    # Pattes
    pygame.draw.line(surf, (180, 180, 180), (14, 42), (10, 46), 3)
    pygame.draw.line(surf, (180, 180, 180), (34, 42), (38, 46), 3)
    # Cloches
    pygame.draw.circle(surf, (255, 210, 60), (12, 14), 5)
    pygame.draw.circle(surf, (255, 210, 60), (36, 14), 5)
    pygame.draw.rect(surf, (255, 210, 60), (10, 12, 28, 4), border_radius=2)
    # Corps
    pygame.draw.circle(surf, (230, 60, 60), (24, 28), 16)
    pygame.draw.circle(surf, (180, 40, 40), (24, 28), 16, 2)
    # Cadran
    pygame.draw.circle(surf, (255, 245, 230), (24, 28), 10)
    # Aiguilles
    pygame.draw.line(surf, (30, 30, 30), (24, 28), (24, 20), 2)
    pygame.draw.line(surf, (30, 30, 30), (24, 28), (30, 28), 2)
    pygame.draw.circle(surf, (30, 30, 30), (24, 28), 2)
    return surf


def make_seringue_sprite():
    surf = _blank()
    # Aiguille
    pygame.draw.line(surf, (160, 160, 170), (24, 38), (24, 46), 2)
    # Corps
    pygame.draw.rect(surf, (210, 230, 245), (18, 18, 12, 20), border_radius=2)
    pygame.draw.rect(surf, (120, 160, 200), (18, 18, 12, 20), 2, border_radius=2)
    # Liquide
    pygame.draw.rect(surf, (80, 180, 255), (20, 24, 8, 12), border_radius=1)
    # Piston
    pygame.draw.rect(surf, (200, 200, 210), (20, 8, 8, 12), border_radius=2)
    pygame.draw.rect(surf, (140, 140, 150), (22, 4, 4, 6))
    # Doigtiers
    pygame.draw.ellipse(surf, (180, 180, 190), (16, 16, 16, 6))
    return surf


def make_croquettes_sprite():
    surf = _blank()
    # Bol
    pygame.draw.ellipse(surf, (200, 80, 60), (10, 28, 28, 14))
    pygame.draw.rect(surf, (200, 80, 60), (10, 28, 28, 8))
    pygame.draw.ellipse(surf, (240, 120, 90), (12, 26, 24, 10))
    # Croquettes
    for x, y in ((16, 24), (22, 22), (28, 24), (20, 28), (26, 28)):
        pygame.draw.circle(surf, (150, 90, 40), (x, y), 3)
        pygame.draw.circle(surf, (180, 110, 50), (x - 1, y - 1), 1)
    return surf


def make_laser_sprite():
    surf = _blank()
    # Pointeur
    pygame.draw.polygon(surf, (50, 50, 55), [(10, 36), (28, 36), (34, 30), (10, 30)])
    pygame.draw.rect(surf, (70, 70, 75), (8, 28, 14, 8), border_radius=2)
    pygame.draw.circle(surf, (220, 40, 40), (12, 32), 3)
    # Rayon
    pygame.draw.line(surf, (255, 60, 60), (34, 30), (42, 8), 2)
    pygame.draw.circle(surf, (255, 80, 80), (42, 8), 5)
    pygame.draw.circle(surf, (255, 200, 200), (42, 8), 2)
    return surf


def make_aspirateur_sprite():
    surf = _blank()
    # Tuyau
    pygame.draw.arc(surf, (90, 90, 95), (6, 6, 20, 20), 0.5, 2.2, 4)
    # Corps
    pygame.draw.rect(surf, (120, 120, 130), (18, 10, 14, 26), border_radius=4)
    pygame.draw.rect(surf, (80, 80, 90), (18, 10, 14, 26), 2, border_radius=4)
    # Embout
    pygame.draw.polygon(surf, (160, 160, 170), [(16, 36), (34, 36), (30, 44), (20, 44)])
    pygame.draw.line(surf, (60, 60, 70), (20, 40), (30, 40), 2)
    return surf


def make_shampoing_sprite():
    surf = _blank()
    # Flacon
    pygame.draw.rect(surf, (90, 180, 220), (16, 16, 16, 26), border_radius=4)
    pygame.draw.rect(surf, (60, 140, 190), (16, 16, 16, 26), 2, border_radius=4)
    # Bouchon
    pygame.draw.rect(surf, (240, 240, 245), (18, 8, 12, 10), border_radius=2)
    # Étiquette
    pygame.draw.rect(surf, (255, 255, 255), (18, 22, 12, 10), border_radius=2)
    pygame.draw.line(surf, (200, 200, 210), (20, 26), (28, 26), 1)
    # Bulles
    pygame.draw.circle(surf, (255, 255, 255), (22, 34), 2)
    pygame.draw.circle(surf, (255, 255, 255), (28, 36), 3)
    return surf


def make_cage_sprite():
    surf = _blank()
    # Base
    pygame.draw.rect(surf, (100, 100, 110), (8, 30, 32, 14), border_radius=3)
    # Grille
    pygame.draw.rect(surf, (180, 190, 200), (10, 10, 28, 22), border_radius=4)
    pygame.draw.rect(surf, (70, 70, 80), (10, 10, 28, 22), 2, border_radius=4)
    for x in (16, 22, 28, 34):
        pygame.draw.line(surf, (70, 70, 80), (x, 12), (x, 30), 2)
    for y in (16, 22, 28):
        pygame.draw.line(surf, (70, 70, 80), (12, y), (36, y), 2)
    # Poignée
    pygame.draw.arc(surf, (90, 90, 100), (18, 4, 12, 10), 0, 3.14, 3)
    return surf


def make_collier_sprite():
    surf = _blank()
    # Collier courbe
    pygame.draw.arc(surf, (200, 50, 50), (8, 18, 32, 20), 3.4, 6.0, 5)
    # Boucle
    pygame.draw.rect(surf, (180, 180, 190), (20, 14, 8, 6), border_radius=2)
    # Clochette
    pygame.draw.polygon(surf, (255, 210, 60), [(22, 34), (26, 34), (28, 42), (20, 42)])
    pygame.draw.circle(surf, (255, 230, 120), (24, 38), 2)
    return surf


def load_object_sprites():
    return {
        "brosse": make_brosse_sprite(),
        "reveil": make_reveil_sprite(),
        "seringue": make_seringue_sprite(),
        "croquettes": make_croquettes_sprite(),
        "laser": make_laser_sprite(),
        "aspirateur": make_aspirateur_sprite(),
        "shampoing": make_shampoing_sprite(),
        "cage": make_cage_sprite(),
        "collier": make_collier_sprite(),
    }
