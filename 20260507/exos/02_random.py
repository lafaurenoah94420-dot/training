# ============================================================
# Resident Evil — esquive imprévisible
# ============================================================
# Claire relance un jet pour déterminer si elle évite un coup. Pour rendre le test
# du fichier stable, le tirage est « fixé » par une graine aléatoire juste en dessous.
#
# Lance : python3 02_random.py
# ============================================================

import random

random.seed(42)

jet = random.randint(1, 6)

# Remplace la valeur de jet par un entier aléatoire entre 1 et 6 inclus.
#
# Déroulé avec la graine fixée à 42 :
#   le tirage obtenu doit être 6 pour passer la vérification ci-dessous
#
# Résultat attendu : jet == 6
#
# Indice : random.randint(1, 6)

# À toi :


# --- Vérification (ne pas modifier) ---
assert jet == 6, "Avec random.seed(42), randint(1, 6) doit donner 6."
print("✅ Correct !")
