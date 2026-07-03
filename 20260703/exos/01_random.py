# ============================================================
# Project Zomboid — dé de survie
# ============================================================
# Tu lances un dé à 6 faces pour savoir combien de zombies
# apparaissent dans le quartier. Le jeu tire un nombre entre 1 et 6.
#
# Lance : python3 01_random.py
# ============================================================

import random

nb_zombies = 0

# Tire un nombre aléatoire entre 1 et 6 (inclus) et stocke-le dans nb_zombies.
#
# Exemple possible : random tire 4  →  nb_zombies = 4
# (la valeur exacte change à chaque lancement — c'est normal)
#
# Résultat attendu : nb_zombies est entre 1 et 6
#
# Indice : random.randint(1, 6)

# À toi :
nb_zombies = random.randint(1, 6)

# --- Vérification (ne pas modifier) ---
assert 1 <= nb_zombies <= 6, f"Obtenu : {nb_zombies} — doit être entre 1 et 6"
print("✅ Correct !")
