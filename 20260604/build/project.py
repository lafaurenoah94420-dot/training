# ============================================================
# GTA — Partage du butin (build)
# ============================================================
# Implémente les 5 fonctions ci-dessous pour que main.py fonctionne.
# Lance : python3 main.py
# Implémente-les dans l'ordre — commence par TODO 1.
# ============================================================

import random


# ------------------------------------------------------------
# TODO 1 — Tirer le type de butin
# ------------------------------------------------------------
# Le braquage peut rapporter différentes marchandises. Le jeu tire
# une entrée au hasard dans la liste loot_types.
#
#   loot_types   : liste de noms de butin (list de str)
#
# pick_loot_type(["liasses", "bijoux", "or"])   =>   une des trois chaînes
#
# pick_loot_type(["cash"])   =>   "cash"
#
# Indice : random.choice(loot_types)
# ------------------------------------------------------------
def pick_loot_type(loot_types):
    return random.choice(loot_types)


# ------------------------------------------------------------
# TODO 2 — Ajouter la part d'un membre d'équipe
# ------------------------------------------------------------
# Franklin note combien chaque complice emporte. Ajoute amount à la
# part déjà enregistrée pour member dans le dictionnaire crew_shares.
#
#   crew_shares   : dict nom → dollars déjà attribués (dict)
#   member        : nom du complice (str)
#   amount        : dollars à ajouter (int)
#
# parts = {"Lamar": 200}  puis  add_crew_cut(parts, "Lamar", 300)
#   =>  parts["Lamar"] vaut 500
#
# parts = {"Franklin": 0}  puis  add_crew_cut(parts, "Trevor", 100)
#   =>  parts["Trevor"] vaut 100
#
# Indice : crew_shares[member] = crew_shares[member] + amount
# ------------------------------------------------------------
def add_crew_cut(crew_shares, member, amount):
    crew_shares[member] = crew_shares[member] + amount
    return crew_shares


# ------------------------------------------------------------
# TODO 3 — Part de Franklin en pourcentage
# ------------------------------------------------------------
# Franklin prend un pourcentage du butin total. Calcule combien
# il garde (division entière).
#
#   total      : montant total du butin (int)
#   percent    : pourcentage pour Franklin (int, ex. 40 pour 40 %)
#
# franklin_percent(10000, 40)   =>   4000
#
# franklin_percent(500, 10)   =>   50
#
# Indice : return total * percent // 100
# ------------------------------------------------------------
def franklin_percent(total, percent):
    return total * percent // 100


# ------------------------------------------------------------
# TODO 4 — Total des liasses comptées
# ------------------------------------------------------------
# Compte toutes les liasses trouvées dans le coffre. Additionne
# chaque montant de la liste payouts.
#
#   payouts   : liste de montants en dollars (list d'int)
#
# sum_payouts([1500, 2200, 900, 400])   =>   5000
#
# sum_payouts([100])   =>   100
#
# Indice : for ... in payouts  et  +=
# ------------------------------------------------------------
def sum_payouts(payouts):
    total = 0
    for i in payouts:
        total += i
    return total


# ------------------------------------------------------------
# TODO 5 — Compte à rebours avant la police
# ------------------------------------------------------------
# Il reste seconds_before_cops secondes. À chaque "vague" de loot,
# on enlève tick_seconds. Répète tant que le temps restant est
# strictement supérieur à tick_seconds, puis renvoie le temps restant.
#
#   seconds_before_cops   : temps de départ (int)
#   tick_seconds          : secondes perdues par vague (int)
#
# countdown_police(120, 25)   =>   20
#   (120→95→70→45→20, on s'arrête car 20 > 25 est faux)
#
# countdown_police(30, 25)   =>   30
#   (la boucle ne tourne pas)
#
# Indice : while seconds_before_cops > tick_seconds:
# ------------------------------------------------------------
def countdown_police(seconds_before_cops, tick_seconds):
    while seconds_before_cops > tick_seconds:
        seconds_before_cops = seconds_before_cops - tick_seconds
    return seconds_before_cops
