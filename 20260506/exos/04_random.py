# ============================================================
# Resident Evil — butin aléatoire
# ============================================================
# Le moteur utilise une graine (seed) pour que le tirage soit toujours le
# même pendant ton test. Après avoir fixé la graine à 0, tu tires un
# entier entre 1 et 100 inclus pour les munitions trouvées.
#
# Lance : python 04_random.py
# ============================================================

import random

random.seed(0)
munitions = 0

# Après random.seed(0), affecte à munitions un entier aléatoire entre 1 et 100
# (bornes incluses).
#
# Indispensable : random.seed(0) avant le tirage — déjà fait au-dessus.
#
# Avec seed(0), le tirage randint(1, 100) tombe sur 50 dans cette version de Python.
#
# Résultat attendu : munitions == 50
#
# Indice : random.randint(...)

# À toi :


# --- Vérification (ne pas modifier) ---
assert munitions == 50, f"Obtenu : {munitions}, attendu : 50"
print("✅ Correct !")
