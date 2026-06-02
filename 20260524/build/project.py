# ============================================================
# The Last of Us — Filtration à l'eau (build)
# ============================================================
# Implémente les 5 fonctions ci-dessous pour que main.py fonctionne.
# Lance : python3 main.py
# Implémente-les dans l'ordre — commence par TODO 1.
# ============================================================


# ------------------------------------------------------------
# TODO 1 — Premier flacon de la file
# ------------------------------------------------------------
# Joel aligne ses récipients sur la table. Le jeu affiche d'abord
# celui tout à gauche (index 0) pour commencer la filtration.
#
#   flasks   : liste de noms de récipients (list de str)
#
# first_flask_name(["flacon_A", "flacon_B", "gourde"])   =>   "flacon_A"
#
# first_flask_name(["gourde"])   =>   "gourde"
#
# Indice : flasks[0]
# ------------------------------------------------------------
def first_flask_name(flasks):
    return flasks[0]


# ------------------------------------------------------------
# TODO 2 — Charbon dans le sac
# ------------------------------------------------------------
# Sans charbon, le filtre ne marche pas. Joel vérifie si "charbon"
# est présent dans son sac avant de commencer.
#
#   backpack   : liste d'objets (list de str)
#
# has_charcoal(["corde", "charbon", "tissu"])   =>   True
#
# has_charcoal(["corde", "tissu"])   =>   False
#
# Indice : in  +  return True ou False
# ------------------------------------------------------------
def has_charcoal(backpack):
    if "charbon" in backpack:
        return True
    else:
        return False


# ------------------------------------------------------------
# TODO 3 — Compter les flacons propres
# ------------------------------------------------------------
# Après le passage au filtre, chaque récipient a un statut "propre"
# ou "sale". Joel compte combien sont prêts à boire.
#
#   statuses   : liste de statuts (str), ex. "propre" ou "sale"
#
# count_clean_flasks(["propre", "sale", "propre"])   =>   2
#
# count_clean_flasks(["sale", "sale"])   =>   0
#
# Indice : for  +  if  +  compteur +=
# ------------------------------------------------------------
def count_clean_flasks(statuses):
    nombre = 0
    for statut in statuses:
        if statut == "propre":
            nombre += 1
    return nombre


# ------------------------------------------------------------
# TODO 4 — Cycles pour rendre l'eau potable
# ------------------------------------------------------------
# L'eau est encore sale. Chaque cycle de filtration enlève 15 points
# de saleté. Compte combien de cycles il faut jusqu'à ce que la
# saleté tombe à 0 ou en dessous.
#
#   dirt   : niveau de saleté au départ (int, >= 0)
#
# filter_cycles_needed(47)   =>   4
#   (47→32→17→2→-13 donc 4 tours)
#
# filter_cycles_needed(0)   =>   0
#
# filter_cycles_needed(15)   =>   1
#
# Indice : while dirt > 0:  puis  dirt -= 15  et  cycles += 1
# ------------------------------------------------------------
def filter_cycles_needed(dirt):
    cycles = 0
    while dirt > 0:
        dirt -= 15
        cycles += 1
    return cycles


# ------------------------------------------------------------
# TODO 5 — Litres récupérés après plusieurs cycles
# ------------------------------------------------------------
# À chaque cycle terminé, Joel récupère 2 litres d'eau potable.
# Calcule le total après un nombre de cycles donné.
#
#   cycles   : nombre de cycles effectués (int, >= 0)
#
# liters_from_cycles(4)   =>   8
#
# liters_from_cycles(0)   =>   0
#
# Indice : for i in range(cycles):  puis  total += 2
# ------------------------------------------------------------
def liters_from_cycles(cycles):
    total = 0
    for i in range(cycles):
        total += 2
    return total
