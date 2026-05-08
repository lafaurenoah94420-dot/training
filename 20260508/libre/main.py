# ============================================================
# Malik — Détecteur de signal Wi‑Fi humain
# ============================================================
# Exemple d'exécution attendu (à reproduire avec ton code) :
#
# Barres Wi‑Fi ? 1
# Âge affiché sur ton profil ? 16
# Malik : il teste si Internet vit dans les murs.
# Risque social : intermédiaire — quelqu'un va filmer sans comprendre.
# ============================================================
import random

wifi = random.randint(0, 4)


jeux = ["Red Dead", "Call of Duty", "the last of us", "Fifa", "Minecraft"]

if wifi == 0:
    for jeu in range(1):
        print(f"jeu jouable : {jeux[jeu]}")
    print("Malik est partit toucher de l'herbe (il est enfin guéris)")
elif wifi == 1:
    for jeu in range(2):
        print(f"jeu jouable : {jeux[jeu]}")
    print("Malik est au bout de sa vie")
elif wifi == 2:
    for jeu in range(3):
        print(f"jeu jouable : {jeux[jeu]}")
    print("Malik devient fou")
elif wifi == 3:
    for jeu in range(4):
        print(f"jeu jouable : {jeux[jeu]}")
    print("Malik est mécontent")
elif wifi == 4:
    for jeu in range(5):
        print(f"jeu jouable : {jeux[jeu]}")
    print("Session SNK")
else:
    print("Nahla est grosse")