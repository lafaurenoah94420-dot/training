# ============================================================
# Project Zomboid — Boire tant qu'il reste de l'eau
# ============================================================
# Tu as des gorgées d'eau dans une bouteille. Chaque gorgée enlève
# 1 à soif. Tu bois tant qu'il reste au moins 1 gorgée.
#
# Lance : python3 03_while.py
# ============================================================

gorgées = 4
soif = 10

# Boucle while : tant que gorgées > 0
#   - enlève 1 à gorgées
#   - enlève 3 à soif
#
# tour 1 : gorgées 4→3, soif 10→7
# tour 2 : gorgées 3→2, soif 7→4
# tour 3 : gorgées 2→1, soif 4→1
# tour 4 : gorgées 1→0, soif 1→-2
# tour 5 : gorgées = 0  →  stop
#
# Résultat attendu : gorgées == 0  et  soif == -2
#
# Indice : while + -=

# À toi :
while gorgées > 0:
    gorgées -= 1
    soif -= 3

# --- Vérification (ne pas modifier) ---
assert gorgées == 0, f"gorgées : {gorgées}, attendu : 0"
assert soif == -2, f"soif : {soif}, attendu : -2"
print("✅ Correct !")
