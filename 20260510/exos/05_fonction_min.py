# ============================================================
# Resident Evil — soin avec plafond de vie
# ============================================================
# Leon utilise un spray. La vie augmente mais ne peut jamais dépasser 100.
#
# Lance : python3 05_fonction_min.py
# ============================================================


def soigner(vie, soin):
    return(min(100, vie + soin))


# Implémente soigner pour renvoyer vie + soin, sans dépasser 100.
#
# soigner(60, 20)   =>   80
#
# soigner(90, 25)   =>   100   (90 + 25 = 115, plafonné à 100)
#
# Indice : return avec min(100, ...)

# À toi : remplace raise NotImplementedError


# --- Vérification (ne pas modifier) ---
assert soigner(60, 20) == 80, "soigner(60, 20) doit retourner 80."
assert soigner(90, 25) == 100, "soigner(90, 25) doit retourner 100, pas 115."
print("✅ Correct !")
