# ============================================================
# GTA — cartouches dans les chargeurs
# ============================================================
# Tu empiles des munitions par paquets de 7 pour remplir des chargeurs identiques.
# Il reste toujours quelques balles qui ne remplissent pas un chargeur complet :
# c’est le reste de la division entière.
#
# Lance : python3 01_modulo.py
# ============================================================

balles_total = 23
taille_chargeur = 7

reste = balles_total % taille_chargeur

# Calcule combien de balles restent « en vrac » après avoir formé des paquets de 7.
#
# 23 divisé par 7 : 7 × 3 = 21  →  il reste 2 balles qui ne complètent pas un 7.
#
# Résultat attendu : reste == 2
#
# Indice : opérateur % (modulo)

# À toi :


# --- Vérification (ne pas modifier) ---
assert reste == 2, "23 % 7 doit laisser un reste de 2 balles."
print("✅ Correct !")
