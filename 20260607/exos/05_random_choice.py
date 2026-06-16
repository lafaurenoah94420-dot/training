# ============================================================
# The Last of Us — Cache de ravitaillement
# ============================================================
# Joel arrive à un point de loot. Trois caches possibles — le jeu
# tire au hasard laquelle contient encore des munitions.
#
# Lance : python3 05_random_choice.py
# ============================================================

import random

random.seed(42)

caches = ["armoire", "placard", "carton"]
cache_choisie = random.choice(caches)

# Tire au hasard un élément de caches avec random.choice()
# et stocke-le dans cache_choisie.
#
# Avec seed 42, le résultat sera toujours le même :
# cache_choisie == "carton"
#
# Résultat attendu : cache_choisie == "carton"
#
# Indice : random.choice(caches)

# À toi :


# --- Vérification (ne pas modifier) ---
assert cache_choisie == "carton", f"Obtenu : '{cache_choisie}', attendu : 'carton'"
print("✅ Correct !")
