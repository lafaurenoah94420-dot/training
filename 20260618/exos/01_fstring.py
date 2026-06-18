# ============================================================
# Hearts of Iron 4 — ordre du jour
# ============================================================
# L'écran de guerre affiche une ligne récap pour chaque front.
# Stalin envoie 12 divisions vers l'est — le jeu doit formater
# le message pour le journal de bord.
#
# Lance : python3 01_fstring.py
# ============================================================

general = "Stalin"
divisions = 12
message = ""

# Construis le message avec une f-string :
# "Stalin envoie 12 divisions vers l'est."
#
# general = "Stalin"
# divisions = 12
#   →  message = "Stalin envoie 12 divisions vers l'est."
#
# Résultat attendu : message == "Stalin envoie 12 divisions vers l'est."
#
# Indice : f"... {general} ... {divisions} ..."

# À toi :
message = f"{general} envoie {divisions} divisions vers l'est."

# --- Vérification (ne pas modifier) ---
assert message == "Stalin envoie 12 divisions vers l'est.", f"Obtenu : '{message}'"
print("✅ Correct !")
