# ============================================================
# GTA — Plaque du véhicule
# ============================================================
# Franklin vole une voiture. L'afficheur montre la plaque en
# majuscules pour le signalement police.
#
# Lance : python3 01_upper.py
# ============================================================

plaque = "ls_492"
plaque_affichee = plaque.upper()

# Transforme plaque en majuscules et stocke dans plaque_affichee.
#
# "ls_492"  →  "LS_492"
#
# Résultat attendu : plaque_affichee == "LS_492"
#
# Indice : .upper()

# À toi :


# --- Vérification (ne pas modifier) ---
assert plaque_affichee == "LS_492", f"Obtenu : '{plaque_affichee}'"
print("✅ Correct !")
