# ============================================================
# Resident Evil — dégâts du coup de couteau
# ============================================================
# Leon attaque un zombie. La fonction calcule les PV restants
# après les dégâts. Les PV ne peuvent pas descendre sous 0.
#
# Lance : python3 04_fonction.py
# ============================================================

#   pv_actuels : points de vie du zombie avant l'attaque
#   degats     : dégâts infligés par le couteau
#
# frapper(40, 15)  →  40 - 15 = 25  →  retourne 25
# frapper(10, 25)  →  10 - 25 = -15 →  plafonné à 0, retourne 0
#
# Résultat attendu : frapper(40, 15) == 25  et  frapper(10, 25) == 0
#
# Indice : return + max(0, ...)


def frapper(pv_actuels, degats):
    soustraction = pv_actuels - degats
    return max(0, soustraction)


# --- Vérification (ne pas modifier) ---
assert frapper(40, 15) == 25, "frapper(40, 15) doit retourner 25"
assert frapper(10, 25) == 0, "frapper(10, 25) doit retourner 0, pas un nombre négatif"
print("✅ Correct !")
