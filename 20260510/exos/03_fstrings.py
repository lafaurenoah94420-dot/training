# ============================================================
# The Last of Us — bilan de combat
# ============================================================
# L'interface doit afficher une phrase avec le nom du survivant et ses PV
# dans une seule chaîne construite dynamiquement.
#
# Lance : python3 03_fstrings.py
# ============================================================

nom = "Ellie"
pv = 42

ligne = f"{nom} — {pv} PV"

# Construis ligne pour qu'elle vaille exactement :
# "Ellie — 42 PV"
#
# Déroulé :
#   nom = "Ellie", pv = 42
#   la phrase doit contenir le nom, un tiret, le nombre, et " PV"
#
# Résultat attendu : ligne == "Ellie — 42 PV"
#
# Indice : f-string avec {nom} et {pv}

# À toi :


# --- Vérification (ne pas modifier) ---
assert ligne == "Ellie — 42 PV", f"Obtenu : '{ligne}'"
print("✅ Correct !")
