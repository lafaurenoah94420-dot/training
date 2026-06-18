# ============================================================
# GTA — étoiles de wanted
# ============================================================
# Franklin se fait repérer par la police. À chaque témoin qui
# appelle le 911, le niveau de recherche monte de 1 étoile.
# 4 témoins appellent — combien d'étoiles au total ?
#
# Lance : python3 03_for_range.py
# ============================================================

etoiles = 0

# Répète 4 fois : ajoute 1 à etoiles à chaque tour.
#
# range(4) donne 4 tours (0, 1, 2, 3)
#
# tour 1 : etoiles = 0 + 1 = 1
# tour 2 : etoiles = 1 + 1 = 2
# tour 3 : etoiles = 2 + 1 = 3
# tour 4 : etoiles = 3 + 1 = 4
#
# Résultat attendu : etoiles == 4
#
# Indice : for ... in range(4) + +=

# À toi :
for temoins in range(4):
    etoiles += 1

# --- Vérification (ne pas modifier) ---
assert etoiles == 4, f"Obtenu : {etoiles}, attendu : 4"
print("✅ Correct !")
