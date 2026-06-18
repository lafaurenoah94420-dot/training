# ============================================================
# Project Zomboid — Veille de nuit (build)
# ============================================================
# Implémente les 5 fonctions ci-dessous pour que main.py fonctionne.
# Lance : python3 main.py
# Implémente-les dans l'ordre — commence par TODO 1.
# ============================================================


# ------------------------------------------------------------
# TODO 1 — Message d'alerte pour une zone
# ------------------------------------------------------------
# La radio du toit diffuse un message par zone surveillée.
# Tu dois le formater en une seule phrase.
#
#   zone_name      : nom de la zone (str)
#   danger_level   : niveau de danger de 1 à 5 (int)
#   zombies        : nombre d'infectés repérés (int)
#
# format_zone_alert("Garage", 3, 12)
#   =>  "Zone Garage — danger 3/5 — 12 infectés repérés"
#
# format_zone_alert("Cuisine", 1, 2)
#   =>  "Zone Cuisine — danger 1/5 — 2 infectés repérés"
#
# Indice : f-string + return
# ------------------------------------------------------------
def format_zone_alert(zone_name, danger_level, zombies):
    message = f"Zone {zone_name} — danger {danger_level}/5 — {zombies} infectés repérés"
    return message
# ------------------------------------------------------------
# TODO 2 — Étiquette de menace selon les infectés vus
# ------------------------------------------------------------
# L'HUD affiche un mot selon le nombre de zombies repérés :
#   5 ou moins   →  "Calme"
#   16 ou moins  →  "Tendu"
#   sinon        →  "Critique"
#
#   zombies_seen   : nombre d'infectés repérés (int)
#
# threat_label(3)    =>  "Calme"
# threat_label(12)   =>  "Tendu"
# threat_label(22)   =>  "Critique"
#
# Indice : if / elif / else + return
# ------------------------------------------------------------
def threat_label(zombies_seen):
    if zombies_seen <= 5:
        rique = "Calme"
    elif zombies_seen > 5 and zombies_seen <= 16:
        rique = "Tendu"
    else:
        rique = "Critique"
    return rique

# ------------------------------------------------------------
# TODO 3 — Total d'infectés apparus pendant la nuit
# ------------------------------------------------------------
# Chaque heure de veille, une vague de 3 infectés frappe la barricade.
# Compte le total sur toutes les heures de la nuit.
#
#   hours   : nombre d'heures de veille (int)
#
# total_spawned(5)
#   range(5) → 5 tours, +3 à chaque tour  →  15
#
# total_spawned(0)   =>  0   (aucune heure, aucune vague)
#
# Indice : for ... in range(hours) + compteur += 3
# ------------------------------------------------------------
def total_spawned(hours):
    tours = 0
    vague = 3
    for i in range(hours):
        tours += vague
    return tours


# ------------------------------------------------------------
# TODO 4 — État du stock dans le placard
# ------------------------------------------------------------
# Avant la nuit, tu vérifies une ressource dans le placard.
# S'il en reste au moins 2, le stock est suffisant. Sinon, alerte basse.
#
#   supplies   : dict nom → quantité (dict)
#   item       : nom de la ressource cherchée (str)
#
# supply_status({"eau": 4, "bandage": 0}, "eau")
#   supplies["eau"] = 4  →  4 >= 2  →  "Stock suffisant"
#
# supply_status({"bandage": 0}, "bandage")
#   supplies["bandage"] = 0  →  0 >= 2  →  "Stock bas"
#
# Indice : supplies[item] puis if / else + return
# ------------------------------------------------------------
def supply_status(supplies, item):
    quantité = supplies[item]
    if quantité >= 2:
        message = "Stock suffisant"
    else:
        message = "Stock bas"
    return message



# ------------------------------------------------------------
# TODO 5 — Dégâts à la barricade après une attaque
# ------------------------------------------------------------
# Les zombies frappent la barricade. Les dégâts finaux suivent :
#   coups × force + bonus (dégâts supplémentaires si la barricade est vieille)
#
#   hits     : nombre de coups portés (int)
#   strength : force par coup (int)
#   bonus    : dégâts supplémentaires (int)
#
# barricade_damage(10, 3, 5)
#   10 × 3 = 30
#   30 + 5 = 35  →  retourne 35
#
# barricade_damage(4, 2, 0)
#   4 × 2 = 8
#   8 + 0 = 8  →  retourne 8
#
# Indice : return avec × et +
# ------------------------------------------------------------
def barricade_damage(hits, strength, bonus):
    combat = hits * strength + bonus
    return combat
