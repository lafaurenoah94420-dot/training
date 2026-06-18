# ============================================================
# GTA — total des dégâts
# ============================================================
# Franklin a fini 4 missions. Chaque mission a un score de dégâts.
# Additionne tout avec une boucle for.
#
# Lance : python3 02_for_liste.py
# ============================================================

degats = [15, 8, 22, 5]
total = 0

# Parcours degats et additionne chaque valeur dans total.
#
# tour 1 : d = 15  →  total = 0 + 15 = 15
# tour 2 : d = 8   →  total = 15 + 8 = 23
# tour 3 : d = 22  →  total = 23 + 22 = 45
# tour 4 : d = 5   →  total = 45 + 5 = 50
#
# Résultat attendu : total == 50
#
# Indice : for d in degats + +=

# À toi :
for n in degats:
    total += n

# --- Vérification (ne pas modifier) ---
assert total == 50, f"Obtenu : {total}, attendu : 50"
print("✅ Correct !")
