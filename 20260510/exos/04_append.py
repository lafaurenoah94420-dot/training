# ============================================================
# Hearts of Iron IV — liste des divisions engagées
# ============================================================
# Tu pars d'une liste vide et tu y ajoutes trois codes de division un par un
# avec append, dans l'ordre indiqué.
#
# Lance : python3 04_append.py
# ============================================================

divisions = []

# Ajoute dans divisions, dans cet ordre : "INF-1", puis "ARM-2", puis "AIR-3".
#
# Déroulé :
#   après 1er append  →  ["INF-1"]
#   après 2e append   →  ["INF-1", "ARM-2"]
#   après 3e append   →  ["INF-1", "ARM-2", "AIR-3"]
#
# Résultat attendu : divisions == ["INF-1", "ARM-2", "AIR-3"]
#
# Indice : divisions.append("...") trois fois

# À toi :
divisions.append("INF-1")
divisions.append("ARM-2")
divisions.append("AIR-3")
# --- Vérification (ne pas modifier) ---
assert divisions == ["INF-1", "ARM-2", "AIR-3"], f"Obtenu : {divisions}"
print("✅ Correct !")
