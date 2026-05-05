# ============================================================
# Project Zomboid — heures de survie (sauvegarde)
# ============================================================
# La sauvegarde stocke le nombre d'heures survécues comme une chaîne
# de caractères (texte). Pour les calculs, le jeu doit convertir ça en
# nombre entier.
#
# Lance : python 02_int.py
# ============================================================

texte_heures = "24"
heures = 0

# Mets dans heures la valeur entière obtenue à partir de texte_heures.
#
# texte_heures est la chaîne "24"
# int("24") correspond au nombre entier 24
#
# Résultat attendu : heures == 24
#
# Indice : int(...)

# À toi :


# --- Vérification (ne pas modifier) ---
assert heures == 24, f"Obtenu : {heures}, attendu : 24"
assert isinstance(heures, int), "heures doit être un int, pas une chaîne"
print("✅ Correct !")
