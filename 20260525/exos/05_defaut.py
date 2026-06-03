# ============================================================
# HOI4 — Pénalité de moral par défaut
# ============================================================
# Quand un général attaque sans bonus, la moral baisse d'une valeur
# par défaut. Tu peux passer un malus supplémentaire en paramètre.
#
# Lance : python3 05_defaut.py
# ============================================================

#   malus_extra  : pénalité en plus (par défaut 0 si on n'en passe pas)
#
# moral_apres_attaque(10)        =>  8   (10 - 2, malus par défaut 2)
# moral_apres_attaque(10, 5)     =>  3   (10 - 2 - 5)
# moral_apres_attaque(1)         =>  0   (ne descend pas sous 0)
#
# Résultat attendu : les trois appels ci-dessus
#
# Indice : def moral_apres_attaque(moral, malus_extra=0):  puis  return max(0, ...)

def moral_apres_attaque(moral, malus_extra=0):
    return max(0, moral - 2 - malus_extra)


# --- Vérification (ne pas modifier) ---
assert moral_apres_attaque(10) == 8, "moral_apres_attaque(10) doit retourner 8"
assert moral_apres_attaque(10, 5) == 3, "moral_apres_attaque(10, 5) doit retourner 3"
assert moral_apres_attaque(1) == 0, "moral_apres_attaque(1) doit retourner 0"
print("✅ Correct !")
