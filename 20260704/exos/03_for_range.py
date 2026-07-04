# ============================================================
# Resident Evil — salles explorées
# ============================================================
# Leon parcourt les salles numérotées de 1 à 6 dans le commissariat.
# Le jeu compte combien de salles il a visitées.
#
# Lance : python3 03_for_range.py
# ============================================================

salles_visitees = 0

# Utilise for et range pour compter de 1 à 6 inclus.
# À chaque tour, ajoute 1 à salles_visitees.
#
# tour 1 → 1, tour 2 → 2, ... tour 6 → 6
#
# Résultat attendu : salles_visitees == 6
#
# Indice : for s in range(1, 7): et +=

# À toi :
for s in range(1, 7):
    salles_visitees += 1

# --- Vérification (ne pas modifier) ---
assert salles_visitees == 6, f"Obtenu : {salles_visitees}, attendu : 6"
print("✅ Correct !")
