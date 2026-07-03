# ============================================================
# Project Zomboid — kit de soin
# ============================================================
# Ton personnage utilise un bandage. La fonction calcule la nouvelle vie
# après soin. Elle ne peut jamais dépasser 100 — c'est le maximum.
#
# Lance : python3 04_fonction.py
# ============================================================

#   vie   : les points de vie actuels
#   soin  : les points récupérés grâce au bandage
#
# soigner(60, 20)  →  60 + 20 = 80   →  retourne 80
# soigner(90, 20)  →  90 + 20 = 110  →  plafonné à 100, retourne 100
#
# Résultat attendu : soigner(60, 20) == 80  et  soigner(90, 20) == 100
#
# Indice : return + min(100, ...)

def soigner(vie, soin):
    vie_soin = vie + soin
    return min(100, vie_soin)


# --- Vérification (ne pas modifier) ---
assert soigner(60, 20) == 80, "soigner(60, 20) doit retourner 80"
assert soigner(90, 20) == 100, "soigner(90, 20) doit retourner 100, pas 110"
print("✅ Correct !")
