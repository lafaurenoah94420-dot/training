# ============================================================
# The Last of Us — dégâts totaux de Joel
# ============================================================
# Joel a infligé des dégâts à chaque infecté d'une liste.
# Calcule la somme de tous les dégâts avec une boucle for.
#
# Lance : python3 04_somme_liste.py
# ============================================================

degats_par_cible = [12, 8, 25, 5, 30]

total = 0

# Parcours degats_par_cible et ajoute chaque valeur à total.
#
# Tour 1 : total = 0 + 12 = 12
# Tour 2 : total = 12 + 8 = 20
# Tour 3 : total = 20 + 25 = 45
# Tour 4 : total = 45 + 5 = 50
# Tour 5 : total = 50 + 30 = 80
#
# Résultat attendu : total == 80
#
# Indice : for d in degats_par_cible:  puis  total += d

# À toi :
for d in degats_par_cible:
    total += d

# --- Vérification (ne pas modifier) ---
assert total == 80, f"Obtenu : {total}, attendu : 80 (12+8+25+5+30)"
print("✅ Correct !")
