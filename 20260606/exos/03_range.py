# ============================================================
# Project Zomboid — jours de survie
# ============================================================
# Tu comptes les jours de 1 à 5 pour afficher un journal de bord.
# Chaque jour ajoute son numéro dans la liste jours.
#
# Lance : python3 03_range.py
# ============================================================

jours = []

# Parcours range(1, 6) et ajoute chaque nombre à jours avec .append().
#
# tour 1 : n = 1  →  jours = [1]
# tour 2 : n = 2  →  jours = [1, 2]
# tour 3 : n = 3  →  jours = [1, 2, 3]
# tour 4 : n = 4  →  jours = [1, 2, 3, 4]
# tour 5 : n = 5  →  jours = [1, 2, 3, 4, 5]
#
# Résultat attendu : jours == [1, 2, 3, 4, 5]
#
# Indice : for + range() + .append()

# À toi :
for n in range(1, 6):
    jours.append(n) 


# --- Vérification (ne pas modifier) ---
assert jours == [1, 2, 3, 4, 5], f"Obtenu : {jours}"
print("✅ Correct !")
