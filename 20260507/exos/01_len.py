# ============================================================
# GTA — plaque du véhicule volé
# ============================================================
# Un témoin note la plaque "LS-17" pour le dépôt de plainte. Le central veut
# vérifier que la longueur lue correspond bien au format attendu.
#
# Lance : python3 01_len.py
# ============================================================

plaque = "LS-17"

longueur = len(plaque)

# Renseigne longueur avec le nombre de caractères de plaque (espaces et tirets
# comptent comme des caractères).
#
# Déroulé :
#   plaque vaut "LS-17"  →  L, S, -, 1, 7  →  5 caractères
#
# Résultat attendu : longueur == 5
#
# Indice : len(...)

# À toi :



# --- Vérification (ne pas modifier) ---
assert longueur == 5, "Compte les caractères un par un, le tiret compte."
print("✅ Correct !")
