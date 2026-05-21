# ============================================================
# Project Zomboid — ration du bunker
# ============================================================
# Le groupe a 48 conserves. Ils en mangent 11 à midi et en trouvent
# 6 dans un placard du voisin. Combien reste-t-il pour le soir ?
#
# Lance : python3 01_calcul.py
# ============================================================

conserves_restantes = 0

# Calcule les conserves restantes avec une seule expression.
#
# 48 - 11 = 37   (après le repas de midi)
# 37 + 6  = 43   (après la trouvaille)
#
# Résultat attendu : conserves_restantes == 43
#
# Indice : une expression avec - et +

# À toi :

conserves_restantes = 48 - 11 + 6
# --- Vérification (ne pas modifier) ---
assert conserves_restantes == 43, "Recompte : 48 - 11 + 6 = ?"
print("✅ Correct !")
