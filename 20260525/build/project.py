# ============================================================
# Hearts of Iron IV — Rapport de moral (build)
# ============================================================
# Implémente les 5 fonctions ci-dessous pour que main.py fonctionne.
# Lance : python3 main.py
# Implémente-les dans l'ordre — commence par TODO 1.
# ============================================================


# ------------------------------------------------------------
# TODO 1 — Numéro de secteur
# ------------------------------------------------------------
# Le rapport radio envoie un code comme "ARM-7-F". Le jeu affiche
# le numéro du secteur (partie du milieu) pour la carte.
#
#   report_code   : code complet (str), ex. "ARM-7-F"
#
# sector_number("ARM-7-F")   =>   "7"
#
# sector_number("EST-12-N")   =>   "12"
#
# Indice : .split("-")  puis  [1]
# ------------------------------------------------------------
def sector_number(report_code):
    return report_code.split("-")[1]


# ------------------------------------------------------------
# TODO 2 — Statut de moral
# ------------------------------------------------------------
# Selon le moral actuel d'une division, l'interface affiche un texte.
#
#   morale   : moral sur 100 (int)
#
# morale_status(85)   =>   "Haute"
# morale_status(60)   =>   "Stable"
# morale_status(35)   =>   "Faible"
# morale_status(10)   =>   "Effondrement"
#
# Règles :
#   >= 80  →  "Haute"
#   >= 50  →  "Stable"
#   >= 20  →  "Faible"
#   sinon  →  "Effondrement"
#
# Indice : if / elif / else
# ------------------------------------------------------------
def morale_status(morale):
    if morale >= 80:
        statut = "Haute"
    elif morale >= 50:
        statut = "Stable"
    elif morale >= 20:
        statut = "Faible"
    else:
        statut = "Effondrement"
    return statut


# ------------------------------------------------------------
# TODO 3 — Moral après une bataille
# ------------------------------------------------------------
# Chaque bataille enlève 2 points de base plus les pertes indiquées.
# Un malus extra optionnel s'ajoute (par défaut 0).
# Le moral ne descend jamais sous 0.
#
#   morale        : moral avant combat (int)
#   loss          : pertes de la bataille (int)
#   extra_loss    : malus en plus (int, par défaut 0)
#
# morale_after_battle(60, 15)      =>   43
# morale_after_battle(60, 15, 5)   =>   38
# morale_after_battle(5, 10)        =>   0
#
# Indice : return max(0, morale - 2 - loss - extra_loss)
# ------------------------------------------------------------
def morale_after_battle(morale, loss, extra_loss=0):
    return max(0, morale - 2 - loss - extra_loss)


# ------------------------------------------------------------
# TODO 4 — Le front peut-il attaquer ?
# ------------------------------------------------------------
# Le général n'ordonne l'assaut que si le moral est suffisant ET
# le ravitaillement est OK ET les ordres sont reçus.
#
#   morale       : moral de la division (int)
#   supply_ok    : ravitaillement en place (bool)
#   orders_ok    : ordres reçus (bool)
#
# front_can_attack(45, True, True)    =>   True
# front_can_attack(45, False, True)   =>   False
# front_can_attack(25, True, True)    =>   False
#
# Indice : return True ou False avec  morale >= 30 and supply_ok and orders_ok
# ------------------------------------------------------------
def front_can_attack(morale, supply_ok, orders_ok):
    if morale >= 30 and supply_ok == True and orders_ok == True:
        return True
    else:
        return False    


# ------------------------------------------------------------
# TODO 5 — Batailles d'infanterie très sanglantes
# ------------------------------------------------------------
# Tu parcours la liste des batailles du jour. Compte combien concernent
# l'infanterie avec au moins 100 pertes.
#
#   battles   : liste de dict avec "branche" (str) et "pertes" (int)
#
# count_heavy_losses([
#     {"branche": "infanterie", "pertes": 120},
#     {"branche": "infanterie", "pertes": 40},
#     {"branche": "artillerie", "pertes": 200},
# ])   =>   1
#
# Indice : for b in battles:  puis  if b["branche"] == "infanterie" and ...
# ------------------------------------------------------------
def count_heavy_losses(battles):
    nombre = 0
    for b in battles:
        if b["branche"] == "infanterie" and b["pertes"] >= 100:
            nombre += 1
    return nombre

