# ============================================================
# The Last of Us — Kit de soin
# ============================================================
# Joel ouvre sa sacoche. Le jeu regarde combien de bandages il
# reste dans l'inventaire pour afficher un message.
#
# Lance : python3 04_dict_if.py
# ============================================================

sacoche = {
    "bandages": 0,
    "munitions": 12,
}

message = ""

# Si sacoche["bandages"] est supérieur à 0, message = "Tu peux te soigner"
# Sinon, message = "Plus de bandages"
#
# sacoche["bandages"] vaut 0  →  0 > 0 ? non  →  "Plus de bandages"
#
# Résultat attendu : message == "Plus de bandages"
#
# Indice : dict["cle"] puis if / else

# À toi :
if sacoche["bandages"] > 0:
    message = "Tu peux te soigner" 
else:
    message = "Plus de bandages"

# --- Vérification (ne pas modifier) ---
assert message == "Plus de bandages", f"Obtenu : '{message}'"
print("✅ Correct !")
