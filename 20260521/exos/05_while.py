# ============================================================
# GTA — évasion des étoiles
# ============================================================
# Franklin est poursuivi. Tant qu'il a au moins 1 étoile de wanted,
# il roule pour semer la police. Chaque tour de boucle enlève 1 étoile.
# Il part avec 4 étoiles.
#
# Lance : python3 05_while.py
# ============================================================

etoiles = 4
tours_fuite = 0

# Tant que etoiles >= 1 : enlève 1 étoile et ajoute 1 à tours_fuite.
#
# départ : etoiles = 4, tours_fuite = 0
# tour 1 : etoiles = 3, tours_fuite = 1
# tour 2 : etoiles = 2, tours_fuite = 2
# tour 3 : etoiles = 1, tours_fuite = 3
# tour 4 : etoiles = 0, tours_fuite = 4  →  0 >= 1 ? non, on sort
#
# Résultat attendu : tours_fuite == 4  et  etoiles == 0
#
# Indice : while + -= et +=

# À toi :
while etoiles > 0:
    etoiles -= 1
    tours_fuite += 1

# --- Vérification (ne pas modifier) ---
assert tours_fuite == 4, f"tours_fuite : {tours_fuite}, attendu : 4"
assert etoiles == 0, f"etoiles : {etoiles}, attendu : 0"
print("✅ Correct !")
