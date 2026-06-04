# ============================================================
# Resident Evil — inventaire de Leon
# ============================================================
# Leon ramasse des munitions. L'inventaire est un dictionnaire :
# la clé est le nom de l'objet, la valeur est la quantité.
# Ajoute 4 cartouches à l'entrée "munitions".
#
# Lance : python3 02_dict.py
# ============================================================

inventaire = {"munitions": 6, "herb": 2}

# inventaire["munitions"] vaut 6 au départ.
# Ajoute 4 à cette quantité (une seule ligne).
#
#   6 + 4 = 10
#
# Résultat attendu : inventaire["munitions"] == 10
#
# Indice : inventaire["munitions"] = inventaire["munitions"] + 4

# À toi :
inventaire["munitions"] += 4

# --- Vérification (ne pas modifier) ---
assert inventaire["munitions"] == 10, f"Obtenu : {inventaire['munitions']}, attendu : 10"
print("✅ Correct !")
