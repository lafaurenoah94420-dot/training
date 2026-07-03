# ============================================================
# The Last of Us — munitions de Joel
# ============================================================
# Joel part avec 30 balles. Il en tire 7 sur des infectés.
# Il fouille un cadavre et récupère 3 balles supplémentaires.
# Combien lui en reste-t-il ?
#
# Lance : python3 01_calcul.py
# ============================================================

balles_restantes = 0

# Calcule les balles restantes avec une seule expression.
#
# 30 - 7 = 23   (après les tirs)
# 23 + 3 = 26   (après avoir récupéré des balles)
#
# Résultat attendu : balles_restantes == 26
#
# Indice : une expression avec - et +

# À toi :
balles_restantes = 30 - 7 + 3

# --- Vérification (ne pas modifier) ---
assert balles_restantes == 26, "Recompte : 30 - 7 + 3 = ?"
print("✅ Correct !")
