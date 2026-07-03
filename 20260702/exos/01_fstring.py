# ============================================================
# The Last of Us — statut de Joel
# ============================================================
# L'interface affiche les PV de Joel dans une phrase formatée.
# Joel a 73 points de vie. Affiche le message complet.
#
# Lance : python3 01_fstring.py
# ============================================================

vie = 73
message = f"Joel a {vie} points de vie"

# Crée le message avec une f-string.
#
# vie = 73  →  message = "Joel a 73 points de vie"
#
# Résultat attendu : message == "Joel a 73 points de vie"
#
# Indice : f"Joel a {vie} points de vie"

# À toi :


# --- Vérification (ne pas modifier) ---
assert message == "Joel a 73 points de vie", f"Obtenu : '{message}'"
print("✅ Correct !")
