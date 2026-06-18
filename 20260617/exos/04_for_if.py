# ============================================================
# Resident Evil — munitions lourdes
# ============================================================
# Leon compte combien de chargeurs ont plus de 10 balles.
# Parcours la liste et incrémente le compteur seulement si > 10.
#
# Lance : python3 04_for_if.py
# ============================================================

chargeurs = [8, 15, 6, 12, 20, 3]
gros_chargeurs = 0

# Pour chaque chargeur, si balles > 10, ajoute 1 à gros_chargeurs.
#
# 8  > 10 ? non  →  gros_chargeurs = 0
# 15 > 10 ? oui  →  gros_chargeurs = 1
# 6  > 10 ? non  →  gros_chargeurs = 1
# 12 > 10 ? oui  →  gros_chargeurs = 2
# 20 > 10 ? oui  →  gros_chargeurs = 3
# 3  > 10 ? non  →  gros_chargeurs = 3
#
# Résultat attendu : gros_chargeurs == 3
#
# Indice : for + if + +=

# À toi :
balles = 0
for balles in chargeurs:
    if balles > 10:
        gros_chargeurs += 1

# --- Vérification (ne pas modifier) ---
assert gros_chargeurs == 3, f"Obtenu : {gros_chargeurs}, attendu : 3"
print("✅ Correct !")
