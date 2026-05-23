# ============================================================
# Project Zomboid — Butin du placard
# ============================================================
# Tu fouilles un placard dans une maison abandonnée. Le jeu tire
# au sort un objet parmi ceux possibles dans ce type de meuble.
#
# Lance : python3 02_random.py
# ============================================================

import random

butin_possible = ["clou", "marteau", "boite_conserve", "bandage", "bouteille_vide"]
objet_trouve = ""

# Tire un objet au hasard dans butin_possible
# et stocke-le dans objet_trouve.
#
# Le résultat est l'un des 5 objets de la liste (aléatoire).
#
# Résultat attendu : objet_trouve in butin_possible
#
# Indice : random.choice()

# À toi :
objet_trouve = random.choice(butin_possible)

# --- Vérification (ne pas modifier) ---
assert objet_trouve in butin_possible, f"Objet invalide : '{objet_trouve}'"
print("✅ Correct !")
