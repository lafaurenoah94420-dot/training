# ============================================================
# Resident Evil — Armoire du commissariat (build)
# ============================================================
# Implémente les 5 fonctions ci-dessous pour que main.py fonctionne.
# Lance : python3 main.py
# Implémente-les dans l'ordre — commence par TODO 1.
# ============================================================

import random


# ------------------------------------------------------------
# TODO 1 — Ouvrir un compartiment au hasard
# ------------------------------------------------------------
# Leon ne sait pas quel compartiment contient encore des supplies.
# Le jeu tire au sort un nom dans la liste des compartiments possibles.
#
#   supplies   : liste de noms d'objets (list de str)
#
# pick_locker_item(["herbe_verte", "spray", "munitions"])
#   => un des trois noms (aléatoire)
#
# Indice : random.choice()
# ------------------------------------------------------------
def pick_locker_item(supplies):
    return random.choice(supplies)


# ------------------------------------------------------------
# TODO 2 — Longueur du code objet
# ------------------------------------------------------------
# L'interface affiche la longueur du code gravé sur l'objet pour
# vérifier qu'il tient dans le bandeau du menu.
#
#   code   : nom de l'objet (str)
#
# supply_code_length("herbe_verte")   =>   11
#
# supply_code_length("spray")   =>   5
#
# Indice : len()
# ------------------------------------------------------------
def supply_code_length(code):
    return len(code)


# ------------------------------------------------------------
# TODO 3 — Points de soin d'une herbe
# ------------------------------------------------------------
# Chaque objet a une valeur de soin stockée dans un dictionnaire.
# Leon consulte la table pour savoir combien de PV une herbe rend.
#
#   herb_name    : nom de l'objet (str)
#   heal_table   : dict nom → points de soin (int)
#
# heal_amount("herbe_verte", {"herbe_verte": 25, "spray": 80})
#   =>   25
#
# heal_amount("spray", {"herbe_verte": 25, "spray": 80})
#   =>   80
#
# Indice : heal_table[herb_name]
# ------------------------------------------------------------
def heal_amount(herb_name, heal_table):
    return heal_table[herb_name]


# ------------------------------------------------------------
# TODO 4 — PV restants après une attaque
# ------------------------------------------------------------
# Un zombie frappe Leon. L'armure absorbe une partie des dégâts avant
# d'affecter les points de vie. Les PV ne descendent jamais sous 0.
#
#   hp       : points de vie actuels (int)
#   damage   : dégâts bruts de l'attaque (int)
#   armor    : points bloqués par l'armure (int)
#
# hp_after_attack(80, 30, 10)   =>   60
#
# hp_after_attack(15, 25, 5)   =>   0
#
# Indice : return max(0, hp - (damage - armor))
# ------------------------------------------------------------
def hp_after_attack(hp, damage, armor):
    return max(0, hp - (damage - armor))


# ------------------------------------------------------------
# TODO 5 — Total des objets dans l'armoire
# ------------------------------------------------------------
# Leon compte combien d'objets il a en stock au total. Le dict indique
# combien il en reste par type ; tu additionnes toutes les quantités.
#
#   cabinet   : dict nom → quantité (int)
#
# total_supplies({"herbe_verte": 3, "spray": 2, "munitions": 5})
#   =>   10
#
# total_supplies({"herbe_bleue": 1})
#   =>   1
#
# Indice : for item in cabinet:  puis  cabinet[item]  et  +=
# ------------------------------------------------------------
def total_supplies(cabinet):
    total = 0
    for item in cabinet:
        total += cabinet[item] 
    return total