# ============================================================
# The Last of Us — dégâts de l'arme
# ============================================================
# Joel tire sur un infecté. La fonction calcule les dégâts finaux.
# Sans bonus, l'arme fait 25 dégâts. Avec un headshot, le bonus
# s'ajoute (valeur par défaut : bonus = 0).
#
# Lance : python3 05_fonction_defaut.py
# ============================================================

#   base   : dégâts de base de l'arme (toujours 25 ici)
#   bonus  : dégâts supplémentaires (0 par défaut si non précisé)
#
# degats(25)       →  25 + 0  = 25
# degats(25, 15)   →  25 + 15 = 40
#
# Résultat attendu : degats(25) == 25  et  degats(25, 15) == 40
#
# Indice : def avec bonus=0 et return base + bonus

def degats(base, bonus=0):
    return base + bonus


# --- Vérification (ne pas modifier) ---
assert degats(25) == 25, "degats(25) doit retourner 25"
assert degats(25, 15) == 40, "degats(25, 15) doit retourner 40"
print("✅ Correct !")
