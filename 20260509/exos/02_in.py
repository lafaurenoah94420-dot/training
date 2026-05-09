# ============================================================
# Resident Evil — objet critique dans la sacoche
# ============================================================
# Claire fouille rapidement sa liste d’objets pour savoir si elle transporte
# déjà la « crimson herb » avant d’en ramasser une nouvelle au sol.
#
# Lance : python3 02_in.py
# ============================================================

objet_cherche = "crimson herb"

items = ["green herb", "ammo box", "crimson herb", "key"]

possede_deja = False

# Mets True dans possede_deja si objet_cherche est présent dans la liste items.
#
# "crimson herb" est bien dans items  →  possede_deja doit être True
#
# Résultat attendu : possede_deja == True
#
# Indice : mot-clé in entre une chaîne et une liste

# À toi :
if objet_cherche in items:
    possede_deja = True

# --- Vérification (ne pas modifier) ---
assert possede_deja is True, (
    "La liste contient bien 'crimson herb' — possede_deja doit être True."
)
print("✅ Correct !")
