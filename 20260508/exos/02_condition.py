# ============================================================
# GTA — niveau de recherche express
# ============================================================
# Les étoiles valent 4. Si stars >= 3, la radio annonce "Recherché activement".
# Sinon elle annonce "Encore discret".
#
# Lance : python3 02_condition.py
# ============================================================

stars = 4

message = "Recherché activement"

# Assigne message selon la règle ci-dessus (compare stars à 3).
#
# Déroulé avec stars == 4 :
#   4 >= 3 ? oui → message = "Recherché activement"
#
# Résultat attendu : message == "Recherché activement"
#
# Indice : if / else avec >= et des chaînes entre guillemets

# À toi :

if stars >= 3:
    print(message)

# --- Vérification (ne pas modifier) ---
assert message == "Recherché activement", (
    f"Obtenu : '{message}' — avec stars >= 3, le message radio attendu est "
    "'Recherché activement'."
)
print("✅ Correct !")
