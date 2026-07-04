# ============================================================
# The Last of Us — nom de l'arme
# ============================================================
# L'interface affiche la longueur du nom de l'arme équipée.
# Combien de caractères dans "fusil-pompe" ?
#
# Lance : python3 02_len.py
# ============================================================

arme = "fusil-pompe"
longueur = 0

# Stocke dans longueur le nombre de caractères de arme.
#
# "fusil-pompe"  →  11 caractères (f-u-s-i-l---p-o-m-p-e)
#
# Résultat attendu : longueur == 11
#
# Indice : len()

# À toi :
longueur = len(arme)

# --- Vérification (ne pas modifier) ---
assert longueur == 11, f"Obtenu : {longueur}, attendu : 11"
print("✅ Correct !")
