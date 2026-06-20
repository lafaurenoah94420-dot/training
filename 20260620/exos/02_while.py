# ============================================================
# Project Zomboid — barricade sous attaque
# ============================================================
# Des zombies frappent la barricade. Chaque coup enlève 2 points de solidité.
# Compte combien de coups sont nécessaires pour la détruire (arriver à 0).
#
# Lance : python3 02_while.py
# ============================================================

solidite = 10
coups = 0

# Tant que solidite est supérieure à zéro, enlève 2 à solidite et ajoute 1 à coups.
#
# départ : solidite = 10, coups = 0
# tour 1 : solidite = 8,  coups = 1
# tour 2 : solidite = 6,  coups = 2
# tour 3 : solidite = 4,  coups = 3
# tour 4 : solidite = 2,  coups = 4
# tour 5 : solidite = 0,  coups = 5  →  boucle s'arrête
#
# Résultat attendu : coups == 5  et  solidite == 0
#
# Indice : while + -= et +=

# À toi :
while solidite > 0:
    solidite -= 2
    coups += 1

# --- Vérification (ne pas modifier) ---
assert coups == 5, f"coups = {coups}, attendu : 5"
assert solidite == 0, f"solidite = {solidite}, attendu : 0"
print("✅ Correct !")
