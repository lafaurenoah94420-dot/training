# ============================================================
# Project Zomboid — ration du matin
# ============================================================
# Tu as 28 unités de nourriture en poche. Tu en consommes 9 pour le petit-déjeuner.
# En fouillant un placard, tu récupères encore 4 unités.
#
# Résultat attendu quand tu lances ce fichier :
#   ✅ Correct !
# ============================================================
unites_restantes = 28 - 9 + 4


# --- Vérification (ne pas modifier) ---
assert unites_restantes == 23, "Recompte : 28 - 9 + 4 = ?"
print("✅ Correct !")
