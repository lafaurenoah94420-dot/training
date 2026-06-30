# ============================================================
# Project Zomboid — Garde-manger de la safehouse (build)
# ============================================================
# Implémente les 5 fonctions ci-dessous pour que main.py fonctionne.
# Lance : python3 main.py
# Implémente-les dans l'ordre — commence par TODO 1.
# ============================================================


# ------------------------------------------------------------
# TODO 1 — Lire une quantité dans le garde-manger
# ------------------------------------------------------------
# Tu ouvres l'étagère et tu veux savoir combien il reste d'un type
# précis de nourriture. Le garde-manger est un dictionnaire : chaque
# clé est un aliment, chaque valeur est la quantité restante.
#
#   pantry   : dict aliment → quantité (int)
#   item     : nom de l'aliment à consulter (str)
#
# ration_count({"conserves": 4, "eau": 6}, "conserves")   =>   4
#
# ration_count({"conserves": 4, "eau": 6}, "eau")   =>   6
#
# Indice : pantry[item]
# ------------------------------------------------------------
def ration_count(pantry, item):
    return pantry[item]


# ------------------------------------------------------------
# TODO 2 — Mettre à jour une quantité
# ------------------------------------------------------------
# Tu reviens de Louisville avec un sac plein. Tu mets à jour le stock
# d'un aliment : la nouvelle quantité remplace l'ancienne dans le dict.
# La fonction modifie pantry sur place (pas besoin de return).
#
#   pantry      : dict aliment → quantité (int)
#   item        : nom de l'aliment à mettre à jour (str)
#   quantity    : nouvelle quantité (int)
#
# restock_food({"pates": 2}, "pates", 5)   =>   pantry devient {"pates": 5}
#
# restock_food({"eau": 1}, "eau", 0)   =>   pantry devient {"eau": 0}
#
# Indice : pantry[item] = quantity
# ------------------------------------------------------------
def restock_food(pantry, item, quantity):
    pantry[item] = quantity

# ------------------------------------------------------------
# TODO 3 — Vérifier si un aliment est dans le stock
# ------------------------------------------------------------
# Avant de préparer le dîner, tu veux savoir si un aliment est encore
# enregistré dans le garde-manger — peu importe la quantité.
#
#   pantry   : dict aliment → quantité (int)
#   item     : nom de l'aliment à chercher (str)
#
# has_food({"conserves": 4, "eau": 6}, "eau")   =>   True
#
# has_food({"conserves": 4, "eau": 6}, "chips")   =>   False
#
# Indice : item in pantry
# ------------------------------------------------------------
def has_food(pantry, item):
    if item in pantry:
        return True
    else:
        return False



# ------------------------------------------------------------
# TODO 4 — Compter toutes les rations
# ------------------------------------------------------------
# Tu additionnes toutes les quantités du garde-manger pour savoir
# combien de rations il reste au total avant la nuit.
#
#   pantry   : dict aliment → quantité (int)
#
# total_rations({"conserves": 4, "pates": 2, "eau": 6})   =>   12
#
# total_rations({"pain": 1})   =>   1
#
# Indice : for key in pantry:  puis  pantry[key]  et  +=
# ------------------------------------------------------------
def total_rations(pantry):
    total = 0
    for key in pantry:
        total += pantry[key]
    return total



# ------------------------------------------------------------
# TODO 5 — Résumé du garde-manger
# ------------------------------------------------------------
# Tu affiches un rapport pour la bande : combien de types différents
# et combien de rations au total. Retourne une f-string exactement
# dans ce format (même avec 1 seul type).
#
#   pantry   : dict aliment → quantité (int)
#
# pantry_status({"conserves": 4, "pates": 5, "eau": 6})
#   =>   "Garde-manger : 3 types, 15 rations"
#
# pantry_status({"pain": 1})
#   =>   "Garde-manger : 1 types, 1 rations"
#
# Indice : len(pantry), une boucle for pour le total, et une f-string
# ------------------------------------------------------------
def pantry_status(pantry):
    total = 0
    len_pantry = len(pantry)
    for i in pantry:
        total += pantry[i]
    return f"Garde-manger : {len_pantry} types, {total} rations"
