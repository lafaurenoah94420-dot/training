# ============================================================
# Hearts of Iron IV — Quartier sous tension (build)
# ============================================================
# Implémente les 5 fonctions ci-dessous pour que main.py fonctionne.
# Lance : python3 main.py
# Implémente-les dans l'ordre — commence par TODO 1.
# ============================================================


# ------------------------------------------------------------
# TODO 1 — Litres qui ne rentrent pas dans les jerricans
# ------------------------------------------------------------
# Tu verses du carburant dans des jerricans pleins de taille fixe. Ce qui ne peut
# pas compléter un dernier jerrican reste au sol : c'est le reste de la division
# entière entre le total disponible et la contenance d'un jerrican.
#
#   total_litres : litres à répartir (int)
#   jug_litres   : contenance d'un jerrican plein (int)
#
# spare_litres(47, 15)   =>   2   (47 = 15 × 3 + 2)
#
# spare_litres(30, 10)   =>   0   (pile parfaite)
#
# Indice : opérateur %
# ------------------------------------------------------------
def spare_litres(total_litres, jug_litres):
    litres = total_litres % jug_litres
    return litres


# ------------------------------------------------------------
# TODO 2 — Ordre présent sur la table à cartes
# ------------------------------------------------------------
# Les télégrammes empilés portent des étiquettes courtes. Tu dois répondre si une
# étiquette précise figure bien dans la liste proposée — sans modifier les listes.
#
#   tag    : mot-clé cherché (str)
#   stack  : liste d'étiquettes (list de str)
#
# order_tag_present("HOLD", ["ATTACK", "HOLD", "PUSH"])   =>   True
#
# order_tag_present("RETREAT", ["ATTACK", "HOLD"])   =>   False
#
# Indice : mot-clé in
# ------------------------------------------------------------
def order_tag_present(tag, stack):
    if tag in stack:
        return True
    else:
        return False


# ------------------------------------------------------------
# TODO 3 — Chaîne d'usine sur plusieurs tours de production
# ------------------------------------------------------------
# Chaque jour ouvré sort le même nombre d'unités. Tu additionnes la production sur
# une série de jours avec une boucle et une variable cumulée qui part de zéro.
#
#   daily_units : unités produites par jour (int)
#   days        : nombre de jours à simuler (int)
#
# gear_over_days(14, 5)   =>   70   (14 × 5)
#
# gear_over_days(10, 1)   =>   10
#
# Indice : for ... in range(days) puis +=
# ------------------------------------------------------------
def gear_over_days(daily_units, days):
    total = 0
    for i in range(days):
        total += daily_units
    return total



# ------------------------------------------------------------
# TODO 4 — Rapports au-dessus du seuil critique
# ------------------------------------------------------------
# La radio locale envoie une série de niveaux d'alerte entiers. Tu comptes combien
# sont strictement supérieurs au seuil fixé — pas les égalités.
#
#   readiness_levels : liste d'entiers (scores)
#   threshold        : seuil à dépasser strictement (int)
#
# fronts_above_threshold([22, 65, 38, 71, 40], 40)   =>   2
#
# fronts_above_threshold([10, 20], 40)   =>   0
#
# Indice : boucle for sur readiness_levels, if avec > puis += sur un compteur
# ------------------------------------------------------------
def fronts_above_threshold(readiness_levels, threshold):
    count = 0
    for i in readiness_levels:
        if i > threshold:
            count += 1
    return count



# ------------------------------------------------------------
# TODO 5 — Manivelle jusqu'à tension minimale
# ------------------------------------------------------------
# Le générateur branlant augmente la tension d'un coup fixe à chaque effort. Tu
# répètes tant que la tension reste strictement sous le plancher demandé.
#
#   charge_volts : tension de départ (int)
#   crank_volts  : gain à chaque tour de manivelle (int)
#   floor_live   : tension minimale à atteindre ou dépasser (int)
#
# crank_until_live(9, 18, 60)   =>   63
#
# crank_until_live(60, 5, 60)   =>   60   (déjà au plancher : aucun tour nécessaire)
#
# Indice : while charge_volts < floor_live puis +=
# ------------------------------------------------------------
def crank_until_live(charge_volts, crank_volts, floor_live):
    while charge_volts < floor_live:
        charge_volts += crank_volts
    return charge_volts
