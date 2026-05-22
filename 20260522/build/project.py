# ============================================================
# GTA — Bilan d'amendes de Franklin (build)
# ============================================================
# Implémente les 5 fonctions ci-dessous pour que main.py fonctionne.
# Lance : python3 main.py
# Implémente-les dans l'ordre — commence par TODO 1.
# ============================================================


# ------------------------------------------------------------
# TODO 1 — Libellé d'une amende pour l'écran
# ------------------------------------------------------------
# Le poste de police affiche une ligne par infraction. Construis le texte
# exact avec le type et le montant en euros.
#
#   fine_type   : nom de l'infraction (str)
#   amount      : montant en euros (int)
#
# format_fine_label("Feu rouge", 200)   =>   "Feu rouge : 200 €"
#
# format_fine_label("Stationnement", 75)   =>   "Stationnement : 75 €"
#
# Indice : f-string
# ------------------------------------------------------------
def format_fine_label(fine_type, amount):
    return f"{fine_type} : {amount} €"


# ------------------------------------------------------------
# TODO 2 — Ajouter une amende au dossier
# ------------------------------------------------------------
# Franklin reçoit une nouvelle contravention. Ajoute le montant à la fin
# de la liste fines (la liste est modifiée sur place).
#
#   fines    : liste des montants déjà enregistrés (list)
#   amount   : nouveau montant à ajouter (int)
#
# fines = [200]  puis  add_fine(fines, 150)  →  fines vaut [200, 150]
#
# Indice : .append()
# ------------------------------------------------------------
def add_fine(fines, amount):
    fines.append(amount)


# ------------------------------------------------------------
# TODO 3 — Total des amendes
# ------------------------------------------------------------
# Le guichet doit afficher la somme de toutes les amendes en attente.
# Parcours la liste et additionne chaque montant.
#
#   fines   : liste de montants en euros (list d'int)
#
# total_fines([150, 500, 75, 1200, 300])   =>   2225
#
# total_fines([100])   =>   100
#
# Indice : for ... in fines  et  +=
# ------------------------------------------------------------
def total_fines(fines):
    total = 0
    for i in fines:
        total += i
    return total


# ------------------------------------------------------------
# TODO 4 — Compter les grosses amendes
# ------------------------------------------------------------
# Le juge compte combien d'amendes dépassent un seuil (ex. 500 €).
# À chaque montant strictement supérieur au seuil, ajoute 1 au compteur.
#
#   fines     : liste de montants (list)
#   minimum   : seuil en euros (int)
#
# count_over_amount([150, 500, 75, 1200, 300], 500)   =>   1
#   (seule 1200 est > 500 — 500 lui-même ne compte pas)
#
# count_over_amount([600, 800, 100], 500)   =>   2
#
# Indice : for + if (>) + +=
# ------------------------------------------------------------
def count_over_amount(fines, minimum):
    count = 0
    for i in fines:
        if i > minimum:
            count += 1
    return count


# ------------------------------------------------------------
# TODO 5 — Dette après pot-de-vin
# ------------------------------------------------------------
# Franklin paie une partie de sa dette au LSPD. Renvoie ce qu'il reste
# à payer. La dette ne peut pas devenir négative.
#
#   total_debt   : dette totale avant paiement (int)
#   payment      : montant payé (int)
#
# debt_after_payment(800, 250)   =>   550
#
# debt_after_payment(100, 200)   =>   0
#
# Indice : return max(0, total_debt - payment)
# ------------------------------------------------------------
def debt_after_payment(total_debt, payment):
    soustraction = total_debt - payment
    return max(0, soustraction)
