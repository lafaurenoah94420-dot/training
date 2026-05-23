# ============================================================
# HOI4 — Nom du général
# ============================================================
# Tu prépares une division. L'interface affiche le nombre de
# lettres dans le nom du général pour vérifier qu'il tient
# dans le bandeau du jeu.
#
# Lance : python3 01_len.py
# ============================================================

general = "Philippe Pétain"
longueur = 0

# Compte le nombre de caractères dans general (espaces inclus)
# et stocke le résultat dans longueur.
#
# "Philippe Pétain"  →  15 caractères au total
#
# Résultat attendu : longueur == 15
#
# Indice : len()

# À toi :
longueur = len(general)

# --- Vérification (ne pas modifier) ---
assert longueur == 15, f"Obtenu : {longueur}, attendu : 15"
print("✅ Correct !")
