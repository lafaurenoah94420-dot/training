# ============================================================
# Project Zomboid — dégâts au corps à corps
# ============================================================
# Quand tu frappes un zombie, les dégâts dépendent de ta force
# et du type d'arme. La fonction calcule le total.
#
# Lance : python3 04_fonction_params.py
# ============================================================

#   force  : ta force de base (un nombre)
#   arme   : les dégâts bonus de l'arme (un nombre)
#
# degats(10, 5)  →  10 + 5 = 15  →  retourne 15
# degats(8, 12)  →  8 + 12 = 20  →  retourne 20
#
# Résultat attendu : degats(10, 5) == 15  et  degats(8, 12) == 20
#
# Indice : return + addition des deux paramètres

def degats(force, arme):
    return force + arme


# --- Vérification (ne pas modifier) ---
assert degats(10, 5) == 15, "degats(10, 5) doit retourner 15"
assert degats(8, 12) == 20, "degats(8, 12) doit retourner 20"
print("✅ Correct !")
