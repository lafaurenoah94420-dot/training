# ============================================================
# Resident Evil — fouille d'armoire
# ============================================================
# Leon fouille une armoire au hasard. Le jeu pioche un objet
# dans la table de loot. Le tirage est déjà fixé pour ce test.
#
# Lance : python3 03_random_choice.py
# ============================================================

import random

random.seed(42)

loot_table = ["herbe verte", "herbe rouge", "munitions", "spray"]
objet_trouve = random.choice(loot_table)

# Pioche un objet au hasard dans loot_table avec random.choice()
# et stocke-le dans objet_trouve.
#
# avec seed(42), le résultat sera toujours "herbe verte"
#
# Résultat attendu : objet_trouve == "herbe verte"
#
# Indice : random.choice(loot_table)

# À toi :


# --- Vérification (ne pas modifier) ---
assert objet_trouve == "herbe verte", f"Obtenu : '{objet_trouve}'"
print("✅ Correct !")
