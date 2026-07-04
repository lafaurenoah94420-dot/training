# ============================================================
# Project Zomboid — stock de conserve
# ============================================================
# Tu as 12 boîtes de soupe, tu en manges 4, puis tu en trouves 7
# en fouillant une maison. Combien en reste-t-il ?
#
# Lance : python3 01_calcul.py
# ============================================================

conserves = 12 - 4 + 7

# Calcule le stock final en une expression.
#
# 12 - 4 = 8   (après avoir mangé)
# 8 + 7 = 15   (après la fouille)
#
# Résultat attendu : conserves == 15
#
# Indice : une expression avec - et +

# À toi :


# --- Vérification (ne pas modifier) ---
assert conserves == 15, "Recompte : 12 - 4 + 7 = ?"
print("✅ Correct !")
