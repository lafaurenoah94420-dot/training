# ============================================================
# Project Zomboid — fouille d'armoire
# ============================================================
# Tu fouilles une armoire au hasard. Le jeu tire un objet dans
# la liste et tu dois le stocker dans la variable trouve.
#
# Lance : python3 01_random_choice.py
# ============================================================

import random

loot_possible = ["clou", "marteau", "boite_conserves", "bandage", "cle"]

trouve = ""

# Tire un objet au hasard dans loot_possible et mets-le dans trouve.
# (une seule ligne avec random.choice)
#
# Exemple si le tirage donne "marteau" :
#   trouve == "marteau"
#
# Résultat attendu : trouve est une des 5 chaînes de la liste
#
# Indice : random.choice(loot_possible)

# À toi :
trouve = random.choice(loot_possible)

# --- Vérification (ne pas modifier) ---
assert trouve in loot_possible, f"'{trouve}' n'est pas dans la liste de loot"
print("✅ Correct !")
