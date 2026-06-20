# ============================================================
# GTA — Casier de Franklin (build)
# ============================================================
# Implémente les 5 fonctions ci-dessous pour que main.py fonctionne.
# Lance depuis exos/ ou n'importe où dans 20260619/ :
#   python3 ../run_build.py
# Ou si tu es déjà dans build/ :
#   python3 main.py
# Implémente-les dans l'ordre — commence par TODO 1.
# ============================================================


# ------------------------------------------------------------
# TODO 1 — Montant de l'amende
# ------------------------------------------------------------
# Chaque crime coûte 250$ d'amende fixe. La fonction calcule
# le total pour un nombre de crimes commis.
#
#   crimes   : nombre de crimes (int)
#
# fine_amount(3)   =>  3 × 250 = 750   →  retourne 750
# fine_amount(0)   =>  0 × 250 = 0    →  retourne 0
#
# Indice : return + ×
# ------------------------------------------------------------
def fine_amount(crimes):
    crimes = crimes * 250
    return crimes


# ------------------------------------------------------------
# TODO 2 — Dette restante après paiement
# ------------------------------------------------------------
# Franklin paie une partie de sa dette au commissariat.
# Le reste ne peut pas être négatif.
#
#   total_debt   : dette totale en dollars (int)
#   paid         : montant payé (int)
#
# debt_remaining(5000, 3200)   =>  5000 - 3200 = 1800   →  retourne 1800
# debt_remaining(1000, 1500)   =>  trop payé  →  retourne 0
#
# Indice : return + max(0, total_debt - paid)
# ------------------------------------------------------------
def debt_remaining(total_debt, paid):
    return max(0, total_debt - paid)


# ------------------------------------------------------------
# TODO 3 — Est-il recherché ?
# ------------------------------------------------------------
# Retourne True si Franklin a au moins 1 étoile de wanted,
# False s'il est à 0 étoile (clean).
#
#   stars   : niveau de wanted (int)
#
# is_wanted(2)   =>  True
# is_wanted(0)   =>  False
#
# Indice : if / else + return True ou return False
# ------------------------------------------------------------
def is_wanted(stars):
    if stars > 0:
        return True
    else: 
        return False


# ------------------------------------------------------------
# TODO 4 — Total des amendes sur une liste
# ------------------------------------------------------------
# La police additionne toutes les amendes enregistrées.
#
#   amounts   : liste de montants en dollars (list)
#
# total_fines([200, 500, 150])   =>  200 + 500 + 150 = 850   →  retourne 850
# total_fines([])                =>  retourne 0
#
# Indice : def + for + accumulateur += + return
# ------------------------------------------------------------
def total_fines(amounts):
    total = 0
    for i in amounts:
        total += i
    return total


# ------------------------------------------------------------
# TODO 5 — Compter les infractions graves
# ------------------------------------------------------------
# Une infraction est "grave" si le montant de l'amende est >= au seuil.
#
#   amounts    : liste de montants (list)
#   threshold  : seuil en dollars (int)
#
# count_serious([200, 500, 150, 800, 300], 400)
#   200 >= 400 ? non
#   500 >= 400 ? oui  →  compteur 1
#   150 >= 400 ? non
#   800 >= 400 ? oui  →  compteur 2
#   300 >= 400 ? non
#   →  retourne 2
#
# count_serious([100, 200], 500)   =>  retourne 0
#
# Indice : def + for + if + compteur + return
# ------------------------------------------------------------
def count_serious(amounts, threshold):
    conteur = 0
    for i in amounts:
        if i >= threshold:
            conteur += 1
    return conteur

