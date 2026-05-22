# ============================================================
# The Last of Us — infectés dans le bâtiment
# ============================================================
# Joel scanne chaque étage. Certains signaux indiquent un infecté
# présent (True). Compte combien d'étages sont infestés.
#
# Lance : python3 05_for_if.py
# ============================================================

etages_infestes = [True, False, True, True, False, False, True]
nombre_infestes = 0

# Parcours la liste. À chaque True, ajoute 1 à nombre_infestes.
#
# tour 1 : True  →  nombre_infestes = 1
# tour 2 : False →  nombre_infestes = 1
# tour 3 : True  →  nombre_infestes = 2
# tour 4 : True  →  nombre_infestes = 3
# tour 5 : False →  nombre_infestes = 3
# tour 6 : False →  nombre_infestes = 3
# tour 7 : True  →  nombre_infestes = 4
#
# Résultat attendu : nombre_infestes == 4
#
# Indice : for + if + +=

# À toi :
for i in etages_infestes:
    if i == True:
        nombre_infestes += 1

# --- Vérification (ne pas modifier) ---
assert nombre_infestes == 4, f"Obtenu : {nombre_infestes}, attendu : 4"
print("✅ Correct !")
