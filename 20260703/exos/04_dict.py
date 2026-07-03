# ============================================================
# Hearts of Iron IV — ressources du pays
# ============================================================
# L'Allemagne a un stock de ressources. Le jeu lit la quantité
# d'acier dans le dictionnaire des stocks.
#
# Lance : python3 04_dict.py
# ============================================================

stocks = {
    "acier": 240,
    "caoutchouc": 85,
    "petrole": 120,
}

acier_dispo = 0

# Lis la valeur associée à la clé "acier" et stocke-la dans acier_dispo.
#
# stocks["acier"]  →  240
#
# Résultat attendu : acier_dispo == 240
#
# Indice : dict["cle"]

# À toi :
acier_dispo = stocks["acier"]

# --- Vérification (ne pas modifier) ---
assert acier_dispo == 240, f"Obtenu : {acier_dispo}, attendu : 240"
print("✅ Correct !")
