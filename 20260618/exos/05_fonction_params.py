# ============================================================
# The Last of Us — dégâts au corps à corps
# ============================================================
# Joel frappe un infecté. Les dégâts finaux dépendent de
# l'attaque de base, d'un multiplicateur de rage, et d'un
# bonus si la cible est déjà blessée.
#
# Formule : attaque × multiplicateur + bonus
#
# Lance : python3 05_fonction_params.py
# ============================================================

# corps_a_corps(20, 2, 5)
#   20 × 2 = 40
#   40 + 5 = 45  →  retourne 45
#
# corps_a_corps(10, 3, 0)
#   10 × 3 = 30
#   30 + 0 = 30  →  retourne 30
#
# Résultat attendu :
#   corps_a_corps(20, 2, 5) == 45
#   corps_a_corps(10, 3, 0) == 30
#
# Indice : def avec 3 paramètres + return

def corps_a_corps(attaque, multiplicateur, bonus):
    combat = attaque * multiplicateur + bonus
    return combat


# --- Vérification (ne pas modifier) ---
assert corps_a_corps(20, 2, 5) == 45, "20 × 2 + 5 devrait donner 45"
assert corps_a_corps(10, 3, 0) == 30, "10 × 3 + 0 devrait donner 30"
print("✅ Correct !")
