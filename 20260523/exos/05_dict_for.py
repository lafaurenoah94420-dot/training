# ============================================================
# HOI4 — Main-d'œuvre totale
# ============================================================
# Tu consultes le rapport de ton armée. Chaque branche a un
# effectif différent. Le jeu doit afficher le total de soldats.
#
# Lance : python3 05_dict_for.py
# ============================================================

effectifs = {
    "infanterie": 12000,
    "artillerie": 3500,
    "cavalerie": 2000,
    "reserve": 8000,
}

total = 0

# Parcours effectifs avec une boucle for et additionne
# chaque valeur dans total.
#
# tour "infanterie"  →  total = 0 + 12000 = 12000
# tour "artillerie"  →  total = 12000 + 3500 = 15500
# tour "cavalerie"   →  total = 15500 + 2000 = 17500
# tour "reserve"     →  total = 17500 + 8000 = 25500
#
# Résultat attendu : total == 25500
#
# Indice : for branche in effectifs:  puis  effectifs[branche]

# À toi :
for branche in effectifs:
    total += effectifs[branche]

# --- Vérification (ne pas modifier) ---
assert total == 25500, f"Obtenu : {total}, attendu : 25500"
print("✅ Correct !")
