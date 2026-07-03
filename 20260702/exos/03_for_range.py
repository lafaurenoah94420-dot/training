# ============================================================
# GTA — compteur de missions
# ============================================================
# Franklin doit compter de 1 à 5 pour savoir combien de missions
# il a enchaînées cette nuit. Utilise range() pour compter.
#
# Lance : python3 03_for_range.py
# ============================================================

total_missions = 0

# Compte combien de tours fait une boucle for i in range(1, 6).
# À chaque tour, ajoute 1 à total_missions.
#
# tour 1 : i = 1  →  total_missions = 1
# tour 2 : i = 2  →  total_missions = 2
# tour 3 : i = 3  →  total_missions = 3
# tour 4 : i = 4  →  total_missions = 4
# tour 5 : i = 5  →  total_missions = 5
#
# Résultat attendu : total_missions == 5
#
# Indice : for i in range(1, 6) + +=

# À toi :
for i in range(1, 6):
    total_missions += 1

# --- Vérification (ne pas modifier) ---
assert total_missions == 5, f"Obtenu : {total_missions}, attendu : 5"
print("✅ Correct !")
