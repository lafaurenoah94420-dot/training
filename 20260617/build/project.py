# ============================================================
# Resident Evil — Inventaire du commissariat (build)
# ============================================================
# Implémente les 5 fonctions ci-dessous pour que main.py fonctionne.
# Lance : python3 main.py
# Implémente-les dans l'ordre — commence par TODO 1.
# ============================================================


# ------------------------------------------------------------
# TODO 1 — Ajouter une arme à l'armurerie
# ------------------------------------------------------------
# Leon récupère une arme. Ajoute weapon à la liste armory
# avec append(), puis retourne le nombre total d'armes.
#
#   armory   : liste d'armes (list)
#   weapon   : nom de l'arme à ajouter (str)
#
# armory = ["couteau"]
# add_weapon(armory, "pistolet")   =>   2
#   armory devient ["couteau", "pistolet"]
#
# add_weapon(armory, "fusil")   =>   3
#
# Indice : append() + len() + return
# ------------------------------------------------------------
def add_weapon(armory, weapon):
    armory.append(weapon)
    return len(armory)


# ------------------------------------------------------------
# TODO 2 — L'arme est-elle dans l'armurerie ?
# ------------------------------------------------------------
# Vérifie si weapon_name est présent dans armory.
#
#   armory        : liste d'armes (list)
#   weapon_name   : nom cherché (str)
#
# has_weapon(["couteau", "pistolet"], "pistolet")   =>   True
#
# has_weapon(["couteau"], "lance-roquettes")   =>   False
#
# Indice : return ... in ...
# ------------------------------------------------------------
def has_weapon(armory, weapon_name):
    return weapon_name in armory


# ------------------------------------------------------------
# TODO 3 — Total des munitions
# ------------------------------------------------------------
# Additionne tous les nombres de la liste ammo_boxes.
#
#   ammo_boxes   : liste de quantités (list d'int)
#
# total_ammo([12, 8, 30, 5])   =>   55
#
# total_ammo([0])   =>   0
#
# Indice : for + += + return
# ------------------------------------------------------------
def total_ammo(ammo_boxes):
    total = 0
    for a in ammo_boxes:
        total += a
    return total



# ------------------------------------------------------------
# TODO 4 — Compter les armes puissantes
# ------------------------------------------------------------
# Compte combien de valeurs dans damages sont strictement
# supérieures à threshold.
#
#   damages     : liste de dégâts (list d'int)
#   threshold   : seuil minimum (int)
#
# count_powerful([5, 15, 8, 20, 12], 10)   =>   2
#   15 > 10 oui, 20 > 10 oui  →  2 armes
#
# count_powerful([3, 4, 5], 10)   =>   0
#
# Indice : for + if + +=
# ------------------------------------------------------------
def count_powerful(damages, threshold):
    total = 0
    for i in damages:
        if i > threshold:
            total += 1
    return total



# ------------------------------------------------------------
# TODO 5 — Poids total du sac
# ------------------------------------------------------------
# Fonction qui reçoit une liste de poids (en kg) et retourne
# la somme de tous les éléments avec une boucle for.
#
#   weights   : liste de poids (list d'int ou float)
#
# total_weight([6, 4, 2, 8])   =>   20
#
# total_weight([])   =>   0
#
# Indice : total = 0, for, +=, return (comme l'exo 05)
# ------------------------------------------------------------
def total_weight(weights):
    total = 0
    for w in weights:
        total += w
    return total
