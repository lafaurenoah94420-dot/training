# ============================================================
# GTA — course-poursuite avec Franklin
# ============================================================
# Franklin accumule des étoiles de wanted en commettant des crimes
# pendant la poursuite. La boucle s'arrête quand il atteint 4 étoiles.
#
# Lance : python3 05_while_if.py
# ============================================================

etoiles = 0
crimes = 0

# Tant que etoiles est strictement inférieur à 4 :
#   - ajoute 1 à crimes
#   - ajoute 1 à etoiles
#
# départ : etoiles = 0, crimes = 0
# tour 1 : crimes = 1, etoiles = 1
# tour 2 : crimes = 2, etoiles = 2
# tour 3 : crimes = 3, etoiles = 3
# tour 4 : crimes = 4, etoiles = 4  →  etoiles < 4 ? non  →  stop
#
# Résultat attendu : crimes == 4  et  etoiles == 4
#
# Indice : while etoiles < 4

# À toi :
while etoiles < 4:
    crimes += 1
    etoiles += 1


# --- Vérification (ne pas modifier) ---
assert crimes == 4, f"crimes = {crimes}, attendu : 4"
assert etoiles == 4, f"etoiles = {etoiles}, attendu : 4"
print("✅ Correct !")
