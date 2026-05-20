# ============================================================
# Resident Evil — casier de l'armurerie
# ============================================================
# Leon consulte le casier sécurisé. Chaque compartiment a un code
# et une quantité de munitions. Mets à jour le stock après la fouille.
#
# Lance : python3 02_dict.py
# ============================================================

casier = {"A1": 12, "B2": 0, "C3": 5}

# 1) Lis la quantité du compartiment "A1" et stocke-la dans stock_a1.
# 2) Ajoute 8 munitions au compartiment "B2" (il était vide).
#
# stock_a1 :
#   casier["A1"]  →  12
#
# casier["B2"] après mise à jour :
#   0 + 8  →  8
#
# Résultat attendu : stock_a1 == 12  et  casier["B2"] == 8
#
# Indice : casier["clé"] pour lire ; casier["clé"] = valeur pour écrire


# À toi :
stock_a1 = casier["A1"]

casier["B2"] = 8
# --- Vérification (ne pas modifier) ---
assert stock_a1 == 12, f"stock_a1 : obtenu {stock_a1}, attendu 12"
assert casier["B2"] == 8, f"casier['B2'] : obtenu {casier['B2']}, attendu 8"
print("✅ Correct !")
