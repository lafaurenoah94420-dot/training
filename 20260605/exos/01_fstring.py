# ============================================================
# The Last of Us — affichage des munitions
# ============================================================
# Joel a 24 balles dans son chargeur. Le jeu doit afficher une
# phrase du type : "Joel a 24 balles."
#
# Lance : python3 01_fstring.py
# ============================================================

balles = 24
message = f"Joel a {balles} balles."

# Mets dans message une f-string : "Joel a 24 balles."
# (utilise la variable balles, pas le nombre en dur)
#
# Résultat attendu : message == "Joel a 24 balles."
#
# Indice : f"... {balles} ..."

# À toi :


# --- Vérification (ne pas modifier) ---
assert message == "Joel a 24 balles.", f"Obtenu : '{message}'"
print("✅ Correct !")
