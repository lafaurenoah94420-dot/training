# ============================================================
# Project Zomboid — réparer jusqu'à acceptable
# ============================================================
# Tu tapes sur une porte abîmée : chaque coup ajoute 15 points de
# solidité. Tu continues tant que la solidité est strictement inférieure
# à 100. Compte combien de coups tu as donnés.
#
# Lance : python 05_while.py
# ============================================================

solidite = 40
coups = 0

# Tant que solidite < 100 :
#   ajoute 15 à solidite
#   ajoute 1 à coups
#
# Déroulé attendu :
# départ : solidite = 40,  coups = 0
# coup 1 : solidite = 55,  coups = 1
# coup 2 : solidite = 70,  coups = 2
# coup 3 : solidite = 85,  coups = 3
# coup 4 : solidite = 100, coups = 4  → on s'arrête (plus < 100)
#
# Résultat attendu : solidite == 100  et  coups == 4
#
# Indice : while

# À toi :


# --- Vérification (ne pas modifier) ---
assert solidite == 100, f"solidite devrait être 100, obtenu : {solidite}"
assert coups == 4, f"nombre de coups attendu : 4, obtenu : {coups}"
print("✅ Correct !")
