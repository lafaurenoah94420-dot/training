# ============================================================
# GTA — braquage du magasin
# ============================================================
# Franklin commence avec 500$. Il vole 1200$ au caissier.
# La police lui prend 350$ d'amende en le rattrapant.
# Combien lui reste-t-il ?
#
# Lance : python3 01_calcul.py
# ============================================================

argent = 0

# Calcule l'argent restant avec une seule expression.
#
# 500 + 1200 = 1700   (après le braquage)
# 1700 - 350 = 1350   (après l'amende)
#
# Résultat attendu : argent == 1350
#
# Indice : une expression avec + et -

# À toi :
argent = 500 + 1200 - 350

# --- Vérification (ne pas modifier) ---
assert argent == 1350, "Recompte : 500 + 1200 - 350 = ?"
print("✅ Correct !")
