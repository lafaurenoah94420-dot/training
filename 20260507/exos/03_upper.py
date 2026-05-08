# ============================================================
# The Last of Us — nom radio « crié »
# ============================================================
# Ellie doit hurler son alias par radio pour couvrir un drone : elle passe tout en
# majuscules pour être lisible dans le bruit.
#
# Lance : python3 03_upper.py
# ============================================================

alias = "feuille"

alias_crie = alias.upper()

# Mets dans alias_crie la version en MAJUSCULES de alias.
#
# Déroulé :
#   alias vaut "feuille"
#   en majuscules → "FEUILLE"
#
# Résultat attendu : alias_crie == "FEUILLE"
#
# Indice : méthode .upper() sur une chaîne

# À toi :


# --- Vérification (ne pas modifier) ---
assert alias_crie == "FEUILLE", f"Obtenu : {repr(alias_crie)} — attendu : 'FEUILLE'."
print("✅ Correct !")
