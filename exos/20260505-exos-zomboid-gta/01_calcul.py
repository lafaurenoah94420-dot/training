# ============================================================
# Project Zomboid — inventaire de survie
# ============================================================
# Chris sort du supermarché avec 28 unités de nourriture.
# Il en consomme 9 pour le petit-déjeuner. En fouillant un
# placard abandonné, il récupère 4 unités supplémentaires.
# Combien lui en reste-t-il exactement ?
#
# Lance : python 01_calcul.py
# ============================================================

# Calcule le nombre d'unités restantes
#
# unites_restantes = 28 - 9 + 4
# => 23
#
# Indice : une seule expression avec - et +

unites_restantes = 28 - 9 + 4


# --- Vérification (ne pas modifier) ---
assert unites_restantes == 23, "Recompte : 28 - 9 + 4 = ?"
print("✅ Correct !")
