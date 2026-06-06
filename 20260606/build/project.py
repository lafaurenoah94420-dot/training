# ============================================================
# The Last of Us — Décodage radio (build)
# ============================================================
# Implémente les 5 fonctions ci-dessous pour que main.py fonctionne.
# Lance : python3 main.py
# Implémente-les dans l'ordre — commence par TODO 1.
# ============================================================


# ------------------------------------------------------------
# TODO 1 — Décoder un message radio
# ------------------------------------------------------------
# Les relais préfixent leurs messages avec "XP_". Joel enlève ce
# préfixe pour lire le vrai nom du point de passage.
#
#   coded_message   : message reçu (str)
#
# decode_radio_code("XP_RELAIS_NORD")   =>   "RELAIS_NORD"
#
# decode_radio_code("XP_BUNKER_EST")   =>   "BUNKER_EST"
#
# Indice : .replace()
# ------------------------------------------------------------
def decode_radio_code(coded_message):
    return coded_message.replace("XP_", "")


# ------------------------------------------------------------
# TODO 2 — Munitions restantes après les tirs
# ------------------------------------------------------------
# Joel tire. Soustrais shots_fired de start_ammo. Le stock ne peut
# pas descendre en dessous de 0.
#
#   start_ammo    : munitions au départ (int)
#   shots_fired   : nombre de tirs (int)
#
# ammo_remaining(30, 12)   =>   18
#
# ammo_remaining(5, 20)   =>   0   (pas assez de balles, plafond à 0)
#
# Indice : soustraction + if pour ne pas aller sous 0 (ou max(0, ...))
# ------------------------------------------------------------
def ammo_remaining(start_ammo, shots_fired):
    return max(0, start_ammo - shots_fired)


# ------------------------------------------------------------
# TODO 3 — Carnet des jours de marche
# ------------------------------------------------------------
# Joel note chaque jour de first_day à last_day inclus dans une liste.
# Retourne la liste complète.
#
#   first_day   : premier jour (int)
#   last_day    : dernier jour inclus (int)
#
# log_march_days(1, 5)   =>   [1, 2, 3, 4, 5]
#
# log_march_days(3, 6)   =>   [3, 4, 5, 6]
#
# Indice : for + range() + .append()
# ------------------------------------------------------------
def log_march_days(first_day, last_day):
    days = []
    for i in range(first_day, last_day + 1):
        days.append(i)
    return days


# ------------------------------------------------------------
# TODO 4 — Lire les munitions dans le plan de ravitaillement
# ------------------------------------------------------------
# Le plan est un dictionnaire : chaque arme a une quantité de munitions.
# Renvoie la valeur associée à weapon_key.
#
#   stash         : dict arme → quantité (dict)
#   weapon_key    : nom de l'arme (str)
#
# plan = {"fusil": 24, "pistolet": 12}
# read_stash_ammo(plan, "fusil")   =>   24
#
# read_stash_ammo(plan, "pistolet")   =>   12
#
# Indice : stash[weapon_key]
# ------------------------------------------------------------
def read_stash_ammo(stash, weapon_key):
    return stash[weapon_key]


# ------------------------------------------------------------
# TODO 5 — Le groupe peut-il partir ?
# ------------------------------------------------------------
# Avant de quitter le camp, Joel vérifie qu'il a assez de munitions.
# Renvoie True si ammo_count >= minimum, False sinon.
#
#   ammo_count   : munitions disponibles (int)
#   minimum      : seuil minimum pour partir (int)
#
# departure_ok(20, 15)   =>   True
#
# departure_ok(8, 15)   =>   False
#
# Indice : if / return True / return False
# ------------------------------------------------------------
def departure_ok(ammo_count, minimum):
    if ammo_count >= minimum:
        return True
    else:
        return False
