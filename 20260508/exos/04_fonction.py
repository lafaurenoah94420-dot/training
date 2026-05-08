# ============================================================
# Resident Evil — chargeur combiné
# ============================================================
# Claire additionne les balles restantes dans deux chargeurs pour savoir si elle peut
# tenir une salve complète.
#
# Lance : python3 04_fonction.py
# ============================================================


def total_balles(chargeur_a, chargeur_b):
    return chargeur_a + chargeur_b


# Implémente total_balles pour renvoyer chargeur_a + chargeur_b.
#
# total_balles(12, 8)   =>   20
#
# Déroulé :
#   12 + 8 = 20
#
# Indice : return avec +

# À toi : remplace raise NotImplementedError


# --- Vérification (ne pas modifier) ---
assert total_balles(12, 8) == 20, "12 + 8 doit faire 20 balles."
assert total_balles(5, 0) == 5, "Si un chargeur est vide, la somme doit rester correcte."
print("✅ Correct !")
