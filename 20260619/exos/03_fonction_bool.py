# ============================================================
# Project Zomboid — est-ce la fin ?
# ============================================================
# Le jeu doit savoir si le survivant est mort. La fonction est_mort()
# retourne True si les PV sont à 0 ou moins, False sinon.
#
# Lance : python3 03_fonction_bool.py
# ============================================================

#   vie   : points de vie actuels (int)
#
# est_mort(0)    =>  True
# est_mort(15)   =>  False
# est_mort(-3)   =>  True
#
# Résultat attendu :
#   est_mort(0) == True
#   est_mort(15) == False
#
# Indice : if / else + return True ou return False

def est_mort(vie):
    if vie <= 0:
        return True
    else:
        return False


# --- Vérification (ne pas modifier) ---
assert est_mort(0) is True, "est_mort(0) doit retourner True"
assert est_mort(15) is False, "est_mort(15) doit retourner False"
assert est_mort(-3) is True, "est_mort(-3) doit retourner True"
print("✅ Correct !")
