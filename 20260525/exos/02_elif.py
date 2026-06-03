# ============================================================
# The Last of Us — Niveau d'alerte infectés
# ============================================================
# Selon le nombre d'infectés autour de Joel, l'interface affiche
# un niveau d'alerte différent.
#
# Lance : python3 02_elif.py
# ============================================================

infectes = 7
alerte = ""

# Définis alerte avec if / elif / else :
#   infectes == 0        →  "Zone calme"
#   infectes entre 1 et 3  →  "Prudence"
#   infectes entre 4 et 7  →  "Danger"
#   sinon (8 ou plus)    →  "Fuir"
#
# Ici infectes = 7  →  alerte = "Danger"
#
# Résultat attendu : alerte == "Danger"
#
# Indice : if ... elif ... elif ... else

# À toi :
if infectes == 0:
    alerte = "Zone calme"
elif infectes > 0 and infectes <= 3:
    alerte = "Prudence"
elif infectes > 3 and infectes <= 7:
    alerte = "Danger"
else:
    alerte = "Fuir"
# --- Vérification (ne pas modifier) ---
assert alerte == "Danger", f"Obtenu : '{alerte}'"
print("✅ Correct !")
