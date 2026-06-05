# ============================================================
# Nahla — Où dormir ?
# ============================================================
# Nahla choisit un endroit pour sa sieste. Tu enregistres les spots
# possibles, puis le programme tire au hasard où elle va dormir.
#
# Exemple d'exécution :
#   Nom du spot : canapé
#   Encore un spot ? (o/n) : o
#   Nom du spot : radiateur
#   Encore un spot ? (o/n) : o
#   Nom du spot : lit
#   Encore un spot ? (o/n) : n
#   Spots : ['canapé', 'radiateur', 'lit']
#   Nahla dort sur : radiateur
# ============================================================
import random

spots = []

réponse = "o"

while réponse == "o":
    nom_du_spot = input("Spot ? ")
    spots.append(nom_du_spot)
    print(spots)
    réponse = input("Encore un spot ? (o/n) : ")
print(random.choice(spots))
