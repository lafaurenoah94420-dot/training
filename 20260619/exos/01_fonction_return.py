# ============================================================
# GTA — multiplicateur de wanted
# ============================================================
# Chaque crime ajoute des étoiles. La fonction double_etoiles()
# calcule le nouveau niveau quand Franklin se fait repérer.
#
# Lance : python3 01_fonction_return.py
# ============================================================

# double_etoiles(2)  →  2 × 2 = 4  →  retourne 4
# double_etoiles(0)  →  0 × 2 = 0  →  retourne 0
#
# Résultat attendu : double_etoiles(2) == 4  et  double_etoiles(0) == 0
#
# Indice : def + return + ×

def double_etoiles(etoiles):
    etoiles = etoiles * etoiles
    return etoiles


# --- Vérification (ne pas modifier) ---
assert double_etoiles(2) == 4, "double_etoiles(2) doit retourner 4"
assert double_etoiles(0) == 0, "double_etoiles(0) doit retourner 0"
print("✅ Correct !")
