# ============================================================
# GTA — plaque d'immatriculation
# ============================================================
# Franklin vole une voiture. Il doit changer la plaque pour éviter
# la police : remplace "LS" par "SA" dans la plaque actuelle.
#
# Lance : python3 02_replace.py
# ============================================================

plaque = "LS-4829"
plaque_modifiee = ""

# Remplace "LS" par "SA" dans plaque et stocke le résultat dans plaque_modifiee.
#
# "LS-4829"  →  remplace LS par SA  →  "SA-4829"
#
# Résultat attendu : plaque_modifiee == "SA-4829"
#
# Indice : .replace() — et n'oublie pas de stocker le résultat

# À toi :
plaque_modifiee = plaque.replace("LS", "SA")

# --- Vérification (ne pas modifier) ---
assert plaque_modifiee == "SA-4829", f"Obtenu : '{plaque_modifiee}'"
print("✅ Correct !")
