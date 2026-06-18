# ============================================================
# Nahla — Où est la gamelle ?
# ============================================================
# Exemple d'exécution :
#   Pièces : cuisine, salon, chambre
#   Ta réponse ? salon
#   Nahla avait caché la gamelle dans : cuisine
#   Raté. Elle te juge.
# ============================================================
import random

pièces = ["cuisine", "salon", "chambre"]
gamelle = random.choice(pièces)

trouvé = False

print(f"Nahla cache sa gamelle... voici les pièces où Nahla aurait pu la cacher : {pièces}")

while trouvé == False:
    réponse = input("Quelle pièce fouillé ?")
    if réponse == "stop":
        break
    if réponse == gamelle:
        trouvé = True
        print("GAGNÉÉÉÉÉ")
        print(f"Nahla l'a caché dans : {gamelle}")
    else:
        print("raté")
        print(f"Nahla l'a caché dans : {gamelle}")


