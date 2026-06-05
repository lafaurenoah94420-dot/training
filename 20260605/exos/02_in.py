# ============================================================
# Resident Evil — arme autorisée ?
# ============================================================
# Leon ne peut tirer qu'avec une arme de la liste autorisée.
# Vérifie si son arme actuelle est dans la liste.
#
# Lance : python3 02_in.py
# ============================================================

armes_ok = ["pistolet", "fusil à pompe", "couteau"]
arme = "fusil à pompe"
autorise = False

# autorise doit valoir True si arme est dans armes_ok.
#
# arme = "fusil à pompe"  →  True
# arme = "lance-flammes"  →  False  (exemple si tu changes arme)
#
# Résultat attendu ici : autorise == True
#
# Indice : if arme in armes_ok:

# À toi :
if arme in armes_ok:
    autorise = True

# --- Vérification (ne pas modifier) ---
assert autorise is True, f"Obtenu : {autorise}, attendu : True"
print("✅ Correct !")
