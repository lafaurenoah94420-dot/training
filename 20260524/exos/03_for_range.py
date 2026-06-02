# ============================================================
# Project Zomboid — Jours de survie
# ============================================================
# Chaque jour survécu, le jeu ajoute 1 point à ton score de survie.
# Tu viens de finir ta 5e journée sans mourir. Calcule le score.
#
# Lance : python3 03_for_range.py
# ============================================================

jours_survecus = 5
score = 0

# Utilise une boucle for avec range(jours_survecus)
# pour ajouter 1 à score à chaque tour.
#
# tour 0 : score = 0 + 1 = 1
# tour 1 : score = 1 + 1 = 2
# tour 2 : score = 2 + 1 = 3
# tour 3 : score = 3 + 1 = 4
# tour 4 : score = 4 + 1 = 5
#
# Résultat attendu : score == 5
#
# Indice : for i in range(jours_survecus):  puis  score += 1


for i in range(jours_survecus):
    score += 1


# --- Vérification (ne pas modifier) ---
assert score == 5, f"Obtenu : {score}, attendu : 5"
print("✅ Correct !")
