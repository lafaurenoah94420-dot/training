# ============================================================
# The Last of Us — dégâts cumulés
# ============================================================
# Additionne tous les dégâts infligés dans la liste pour obtenir un total de combat.
#
# Lance : python3 03_for_liste.py
# ============================================================

degats = [6, 14, 5, 11]

total_degats = 0

# Parcourt degats avec une boucle for et accumule dans total_degats.
#
# Déroulé :
#   tour 1 : +6  → total 6
#   tour 2 : +14 → total 20
#   tour 3 : +5  → total 25
#   tour 4 : +11 → total 36
#
# Résultat attendu : total_degats == 36
#
# Indice : for x in degats puis +=

# À toi :
for tour in degats:
    total_degats += tour


# --- Vérification (ne pas modifier) ---
assert total_degats == 36, (
    f"Obtenu : {total_degats} — attendu : 36 (somme de 6+14+5+11)."
)
print("✅ Correct !")
