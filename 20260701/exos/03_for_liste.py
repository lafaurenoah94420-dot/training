# ============================================================
# GTA — bilan de missions
# ============================================================
# Franklin vient de finir sa session. À chaque mission il a infligé
# des dégâts. Le jeu doit calculer le total pour son classement.
#
# Lance : python3 03_for_liste.py
# ============================================================

degats = [5, 12, 3, 8, 20]
total_degats = 0

# Parcours la liste degats et additionne chaque valeur dans total_degats.
#
# tour 1 : x = 5   →  total_degats = 0 + 5  = 5
# tour 2 : x = 12  →  total_degats = 5 + 12 = 17
# tour 3 : x = 3   →  total_degats = 17 + 3 = 20
# tour 4 : x = 8   →  total_degats = 20 + 8 = 28
# tour 5 : x = 20  →  total_degats = 28 + 20 = 48
#
# Résultat attendu : total_degats == 48
#
# Indice : boucle for + +=

# À toi :
for i in degats:
    total_degats += i

# --- Vérification (ne pas modifier) ---
assert total_degats == 48, f"Obtenu : {total_degats}, attendu : 48"
print("✅ Correct !")
