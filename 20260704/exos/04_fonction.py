# ============================================================
# GTA — gain de mission
# ============================================================
# Franklin reçoit une récompense de base plus un bonus.
# La fonction calcule le total gagné.
#
# Lance : python3 04_fonction.py
# ============================================================

#   base   : l'argent fixe de la mission
#   bonus  : l'argent bonus (tip, objets volés...)
#
# gain(500, 150)  →  650
# gain(1000, 0)   →  1000
#
# Résultat attendu : gain(500, 150) == 650  et  gain(1000, 0) == 1000
#
# Indice : def + return + addition

def gain(base, bonus):
    return base + bonus


# --- Vérification (ne pas modifier) ---
assert gain(500, 150) == 650, "gain(500, 150) doit retourner 650"
assert gain(1000, 0) == 1000, "gain(1000, 0) doit retourner 1000"
print("✅ Correct !")
