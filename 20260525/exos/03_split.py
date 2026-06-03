# ============================================================
# Resident Evil — Code de la porte
# ============================================================
# Leon trouve un code sur un bout de papier : "A-12-B".
# Le jeu sépare les morceaux pour afficher la partie centrale (le chiffre).
#
# Lance : python3 03_split.py
# ============================================================

code_brut = "A-12-B"
partie_centrale = ""

# Utilise .split("-") pour découper la chaîne en liste,
# puis récupère l'élément du milieu (index 1) dans partie_centrale.
#
# "A-12-B".split("-")  →  ["A", "12", "B"]
# index 1  →  "12"
#
# Résultat attendu : partie_centrale == "12"
#
# Indice : .split("-")  puis  [1]

# À toi :
partie_centrale = code_brut.split("-")[1]

# --- Vérification (ne pas modifier) ---
assert partie_centrale == "12", f"Obtenu : '{partie_centrale}'"
print("✅ Correct !")
