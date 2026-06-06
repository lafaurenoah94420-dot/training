# ============================================================
# The Last of Us — inventaire rapide
# ============================================================
# Joel a un sac avec des objets. Le jeu doit lire et mettre à jour
# la quantité de munitions dans le dictionnaire inventaire.
#
# Lance : python3 05_dict.py
# ============================================================

inventaire = {"munitions": 12, "bandages": 2, "nourriture": 1}

# 1. Lis la valeur de "munitions" et stocke-la dans munitions_avant.
# 2. Ajoute 8 munitions : inventaire["munitions"] = munitions_avant + 8
# 3. Stocke la nouvelle valeur dans munitions_apres.
#
# munitions_avant  →  inventaire["munitions"] vaut 12  →  12
# inventaire["munitions"] = 12 + 8 = 20
# munitions_apres  →  20
#
# Résultat attendu : munitions_avant == 12  et  munitions_apres == 20
#
# Indice : dict["cle"] pour lire et écrire

munitions_avant = 0
munitions_apres = 0

# À toi :
munitions_avant = inventaire["munitions"]
inventaire["munitions"] = munitions_avant + 8
munitions_apres = inventaire["munitions"]
# --- Vérification (ne pas modifier) ---
assert munitions_avant == 12, f"munitions_avant : {munitions_avant}, attendu : 12"
assert munitions_apres == 20, f"munitions_apres : {munitions_apres}, attendu : 20"
assert inventaire["munitions"] == 20, "inventaire['munitions'] doit valoir 20"
print("✅ Correct !")
