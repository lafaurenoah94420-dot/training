# ============================================================
# Resident Evil — herbes en stock
# ============================================================
# Claire fouille la trousse : elle voit ce qui reste comme ingrédients.
# Elle veut savoir si elle peut faire une mixture qui nécessite une herbe verte,
# sans chercher au hasard dans les placards.
#
# Lance : python3 02_in.py
# ============================================================

stock = ["spray", "herbe verte", "combinaison"]

ingredient_requis = "herbe verte"

peut_craft = False

# Mets peut_craft à True si ingredient_requis est présent dans stock,
# sinon False.
#
# Déroulé avec les valeurs actuelles :
#   stock contient "herbe verte"
#   ingredient_requis vaut "herbe verte"
#   donc « herbe verte » est dans la liste → peut_craft doit être True
#
# Résultat attendu : peut_craft == True
#
# Indice : mot-clé in pour tester la présence dans une liste

# À toi :
if ingredient_requis in stock:
    peut_craft = True

# --- Vérification (ne pas modifier) ---
assert peut_craft is True, (
    "Obtenu : False — 'herbe verte' est bien dans stock pour cet exemple."
)
print("✅ Correct !")
