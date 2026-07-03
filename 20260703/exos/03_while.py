# ============================================================
# Resident Evil — compte à rebours
# ============================================================
# Leon doit quitter le bâtiment avant l'explosion. Un compte à rebours
# part de 5 secondes et descend de 1 à chaque tour jusqu'à 0.
#
# Lance : python3 03_while.py
# ============================================================

secondes = 5
tours = 0

# Tant que secondes est strictement supérieur à 0 :
#   retire 1 à secondes
#   ajoute 1 à tours
#
# tour 1 : secondes = 5  →  secondes = 4, tours = 1
# tour 2 : secondes = 4  →  secondes = 3, tours = 2
# tour 3 : secondes = 3  →  secondes = 2, tours = 3
# tour 4 : secondes = 2  →  secondes = 1, tours = 4
# tour 5 : secondes = 1  →  secondes = 0, tours = 5
# (secondes vaut 0 → la boucle s'arrête)
#
# Résultat attendu : secondes == 0  et  tours == 5
#
# Indice : while + -= et +=

# À toi :
while secondes > 0:
    secondes -= 1
    tours += 1

# --- Vérification (ne pas modifier) ---
assert secondes == 0, f"secondes doit valoir 0, obtenu : {secondes}"
assert tours == 5, f"tours doit valoir 5, obtenu : {tours}"
print("✅ Correct !")
