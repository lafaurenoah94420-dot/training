# ============================================================
# Hearts of Iron — usines construites
# ============================================================
# L'Allemagne lance 5 usines civiles d'affilée. Chaque usine coûte
# 2 usines militaires de stock (conversion du jeu). Au départ le stock
# militaire vaut 20. Après les 5 constructions, combien reste-t-il ?
#
# Lance : python3 03_range.py
# ============================================================

stock_militaire = 20
cout_par_usine = 2
nombre_usines = 5

# Répète nombre_usines fois : enlève cout_par_usine du stock.
#
# départ : stock_militaire = 20
# tour 1 : 20 - 2 = 18
# tour 2 : 18 - 2 = 16
# tour 3 : 16 - 2 = 14
# tour 4 : 14 - 2 = 12
# tour 5 : 12 - 2 = 10
#
# Résultat attendu : stock_militaire == 10
#
# Indice : for range(nombre_usines) et -=

# À toi :

for i in range(nombre_usines):
    stock_militaire -= cout_par_usine
# --- Vérification (ne pas modifier) ---
assert stock_militaire == 10, f"Obtenu : {stock_militaire}, attendu : 10"
print("✅ Correct !")
