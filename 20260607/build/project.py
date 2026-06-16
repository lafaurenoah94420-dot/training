# ============================================================
# Project Zomboid — Nuit de survie (build)
# ============================================================
# Implémente les 5 fonctions ci-dessous pour que main.py fonctionne.
# Lance : python3 main.py
# Implémente-les dans l'ordre — commence par TODO 1.
# ============================================================


# ------------------------------------------------------------
# TODO 1 — Alerte à l'écran en majuscules
# ------------------------------------------------------------
# L'interface affiche les statuts en majuscules pour alerter le joueur.
#
#   status   : texte du statut (str)
#
# format_status("faim critique")   =>   "FAIM CRITIQUE"
#
# format_status("ok")   =>   "OK"
#
# Indice : .upper() + return
# ------------------------------------------------------------
def format_status(status):
    return status.upper()


# ------------------------------------------------------------
# TODO 2 — Le sac contient-il cet objet ?
# ------------------------------------------------------------
# Vérifie si food_name est présent dans pantry (liste de noms).
#
#   pantry      : liste d'objets (list)
#   food_name   : nom cherché (str)
#
# has_food(["conserve", "eau"], "eau")   =>   True
#
# has_food(["conserve"], "fusil")   =>   False
#
# Indice : return food_name in pantry
# ------------------------------------------------------------
def has_food(pantry, food_name):
    if food_name in pantry:
        return food_name in pantry
    else:
        return False


# ------------------------------------------------------------
# TODO 3 — Manger tant que la faim est positive
# ------------------------------------------------------------
# Tant que hunger > 0 ET qu'il reste de la food :
#   - enlève 2 à food
#   - enlève 4 à hunger
# Quand hunger tombe à 0 ou food à 0, arrête et retourne food restante.
#
#   food     : stock de nourriture (int)
#   hunger   : niveau de faim (int)
#
# eat_while_hungry(14, 10)   =>   8
#   tour 1 : food 14→12, hunger 10→6
#   tour 2 : food 12→10, hunger 6→2
#   tour 3 : food 10→8, hunger 2→0  →  stop, retourne 8
#
# eat_while_hungry(3, 20)   =>   0   (plus de nourriture avant fin de faim)
#
# Indice : while + -= + return food
# ------------------------------------------------------------
def eat_while_hungry(food, hunger):
    while hunger > 0 and food > 0:
        food -= 2
        hunger -= 4
    return food


# ------------------------------------------------------------
# TODO 4 — Total des dégâts de la nuit
# ------------------------------------------------------------
# Additionne tous les nombres de la liste hits.
#
#   hits   : liste de dégâts (list d'int)
#
# total_damage([5, 12, 3, 8])   =>   28
#
# total_damage([0])   =>   0
#
# Indice : for + +=
# ------------------------------------------------------------
def total_damage(hits):
    total = 0
    for hit in hits:
        total += hit
    return total


# ------------------------------------------------------------
# TODO 5 — Événement aléatoire de la nuit
# ------------------------------------------------------------
# Tire au hasard un événement dans la liste events.
#
#   events   : liste de noms d'événements (list)
#
# random_night_event(["horde", "pluie", "silence"])   =>   un des trois
# (avec seed(7) dans main : "cauchemar" pour la liste du main)
#
# Indice : import random + random.choice(events)
# ------------------------------------------------------------
def random_night_event(events):
    import random
    return random.choice(events)
