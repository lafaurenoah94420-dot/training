# ============================================================
# GTA — braquages de la semaine
# ============================================================
# Franklin a enregistré le butin de chaque braquage (en milliers $).
# Le jeu doit afficher le total pour le classement hebdo.
#
# Lance : python3 03_for_liste.py
# ============================================================

butins = [15, 8, 22, 5, 30]
total_butin = 0

for i in butins: 
    total_butin += i

# Parcours butins et additionne chaque valeur dans total_butin.
#
# tour 1 : x = 15  →  total_butin = 0 + 15  = 15
# tour 2 : x = 8   →  total_butin = 15 + 8  = 23
# tour 3 : x = 22  →  total_butin = 23 + 22 = 45
# tour 4 : x = 5   →  total_butin = 45 + 5  = 50
# tour 5 : x = 30  →  total_butin = 50 + 30 = 80
#
# Résultat attendu : total_butin == 80
#
# Indice : boucle for + +=

# À toi :


# --- Vérification (ne pas modifier) ---
assert total_butin == 80, f"Obtenu : {total_butin}, attendu : 80"
print("✅ Correct !")
