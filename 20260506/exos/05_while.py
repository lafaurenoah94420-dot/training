# ============================================================
# Project Zomboid — réserve d'eau du robinet
# ============================================================
# Tu as une mesure d'eau en litres. Chaque jour tu verses 7 litres pour cuisiner.
# Compte combien de jours complets tu tiens tant qu'il reste au moins 10 litres
# avant le prochain prélèvement (la boucle s'arrête quand il resterait moins de 10).
#
# Lance : python3 05_while.py
# ============================================================

litres = 50
jours = 0

# Tant que litres >= 10 :
#   retire 7 litres
#   ajoute 1 à jours
#
# Déroulé avec litres qui commence à 50 :
#   jour 1 : 50 - 7 = 43  → jours = 1
#   jour 2 : 43 - 7 = 36  → jours = 2
#   jour 3 : 36 - 7 = 29  → jours = 3
#   jour 4 : 29 - 7 = 22  → jours = 4
#   jour 5 : 22 - 7 = 15  → jours = 5
#   jour 6 : 15 - 7 = 8   → jours = 6 → 8 < 10 donc stop (on ne retire pas un 7ème jour)
#
# Résultat attendu : jours == 6 et litres == 8 à la fin
#
# Indice : while litres >= 10:

# À toi :
while litres >= 10:
    litres -= 7
    jours += 1

# --- Vérification (ne pas modifier) ---
assert jours == 6, f"Obtenu : {jours} — recompte les jours à partir de 50."
assert litres == 8, f"Après la boucle, litres doit valoir 8, pas {litres}."
print("✅ Correct !")
