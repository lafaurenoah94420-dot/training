# ============================================================
# The Last of Us — soin d'urgence
# ============================================================
# Joel utilise un kit. La fonction soigner() ajoute des PV
# mais la vie ne peut jamais dépasser 100.
#
# Lance : python3 03_fonction.py
# ============================================================

# soigner(40, 25)  →  40 + 25 = 65   →  retourne 65
# soigner(85, 30)  →  85 + 30 = 115  →  plafonné à 100, retourne 100
#
# Résultat attendu : soigner(40, 25) == 65  et  soigner(85, 30) == 100
#
# Indice : return + min(100, vie + soin)

def soigner(vie, soin):
    return min(100, vie + soin)


# --- Vérification (ne pas modifier) ---
assert soigner(40, 25) == 65, "soigner(40, 25) doit retourner 65"
assert soigner(85, 30) == 100, "soigner(85, 30) doit retourner 100, pas 115"
print("✅ Correct !")
