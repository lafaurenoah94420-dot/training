# ============================================================
# Project Zomboid — sac de loot sans merci (build)
# ============================================================
# Implémente les 5 fonctions ci-dessous pour que main.py fonctionne.
# Lance : python3 main.py
# Implémente-les dans l'ordre — commence par TODO 1.
# ============================================================

import random

random.seed(99)


# ------------------------------------------------------------
# TODO 1 — Longueur du code-barres sur une boîte
# ------------------------------------------------------------
# Tu dois savoir si l'étiquette colle au format attendu par la vieille radio du
# hangar : le nombre de caractères du code suffit pour ce premier contrôle.
#
#   sku_code : chaîne imprimée sous la boîte (str)
#
# sku_length("Z-9C12")   =>   6
#
# sku_length("X")   =>   1   (cas minimal)
#
# Indice : len(...)
# ------------------------------------------------------------
def sku_length(sku_code):
    return len(sku_code)


# ------------------------------------------------------------
# TODO 2 — Sortir des conserves du placard
# ------------------------------------------------------------
# Le dictionnaire pantry mappe ce qu'il reste à la maison. Tu retire simplement
# des conserves sans toucher aux autres clés pour cet appel.
#
#   pantry : dict avec au moins la clé "conserves" (int)
#   eaten  : nombre de boîtes mangées (int)
#
# Si pantry vaut {"conserves": 12, "eau": 4} et eaten vaut 5,
# après l'appel pantry["conserves"] doit valoir 7.
#
# consume_cans({"conserves": 12, "eau": 4}, 5)   =>   effet de bord sur pantry
#
# Indice : pantry["conserves"] -= eaten
# ------------------------------------------------------------
def consume_cans(pantry, eaten):
    pantry["conserves"] -= eaten


# ------------------------------------------------------------
# TODO 3 — Bruit de radio qui attire les infected
# ------------------------------------------------------------
# Tu tires un niveau de grésillement pour savoir si tu dois couper la radio.
# La graine aléatoire est déjà fixée en haut du fichier pour que les tests soient
# stables.
#
# noise_roll()   =>   7   (avec random.seed(99) déjà appelé plus haut)
#
# Indice : random.randint(...)
# ------------------------------------------------------------
def noise_roll():
    return random.randint(1, 10)


# ------------------------------------------------------------
# TODO 4 — Message de toit en majuscules
# ------------------------------------------------------------
# Tu cries ton indicatif par-dessus les toits pour que les survivants t'entendent
# dans la pagaille : tout doit être en majuscules.
#
#   callsign : mot ou pseudo à hurler (str)
#
# shout_callsign("grenier")   =>   "GRENIER"
#
# Indice : .upper()
# ------------------------------------------------------------
def shout_callsign(callsign):
    return callsign.upper()


# ------------------------------------------------------------
# TODO 5 — Énergie après une nuit de loot
# ------------------------------------------------------------
# Tu calcule le stamina restant après une perte : ça ne peut pas passer sous 0.
#
#   base : stamina avant effort (int)
#   loss : perte due au sprint ou au stress (int)
#
# safe_stamina(25, 10)   =>   15
# safe_stamina(8, 10)    =>   0   (pas de stamina négative)
#
# Indice : max(0, base - loss)
# ------------------------------------------------------------
def safe_stamina(base, loss):
    return max(0, base - loss)
