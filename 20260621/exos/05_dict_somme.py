# ============================================================
# Hearts of Iron IV — Stock de ressources
# ============================================================
# Le quartier général compte le total de toutes les ressources
# dans le dépôt. Chaque type est une clé du dictionnaire.
#
# Lance : python3 05_dict_somme.py
# ============================================================

depot = {
    "acier": 10,
    "caoutchouc": 5,
    "petrole": 3,
}

total = 0

# Parcours chaque clé de depot avec une boucle for.
# À chaque tour, ajoute depot[cle] au total.
#
# tour 1 : cle = "acier"    →  total = 0 + 10 = 10
# tour 2 : cle = "caoutchouc" →  total = 10 + 5 = 15
# tour 3 : cle = "petrole"  →  total = 15 + 3 = 18
#
# Résultat attendu : total == 18
#
# Indice : for cle in dict:  puis  total += dict[cle]

# À toi :
for i in depot:
    total += depot[i]

# --- Vérification (ne pas modifier) ---
assert total == 18, f"Obtenu : {total}, attendu : 18"
print("✅ Correct !")
