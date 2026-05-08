# ============================================================
# Project Zomboid — ration du soir
# ============================================================
# Tu as 18 barres énergétiques en réserve. Tu en consommes 6 pour tenir une veille.
# Tu récupères encore 4 barres dans une cuisine abandonnée.
#
# Lance : python3 01_calcul.py
# ============================================================

barres_restantes = 0

# Calcule barres_restantes avec une seule expression : départ 18, moins 6, plus 4.
#
# Déroulé :
#   18 - 6 = 12   (après la veille)
#   12 + 4 = 16   (après la fouille)
#
# Résultat attendu : barres_restantes == 16
#
# Indice : une expression avec - et +

# À toi :

barres_restantes = 18 - 6 + 4

# --- Vérification (ne pas modifier) ---
assert barres_restantes == 16, "Recompte : 18 - 6 + 4 = ?"
print("✅ Correct !")
