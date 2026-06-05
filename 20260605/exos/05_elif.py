# ============================================================
# Project Zomboid — niveau de faim
# ============================================================
# Selon la faim (0 à 100), affiche un message dans niveau.
# Utilise if / elif / else.
#
# Lance : python3 05_elif.py
# ============================================================

faim = 35
niveau = ""

# faim = 35 ici.
#
# faim <= 20        →  niveau = "critique"
# 21 <= faim <= 50  →  niveau = "faible"
# faim > 50         →  niveau = "ok"
#
# Résultat attendu : niveau == "faible"
#
# Indice : if / elif / else avec <= et >

# À toi :
if faim <= 20:
    niveau = "critique"
elif faim >= 21 and faim <= 50:
    niveau = "faible"
else:
    niveau = "ok"

# --- Vérification (ne pas modifier) ---
assert niveau == "faible", f"Obtenu : '{niveau}', attendu : 'faible'"
print("✅ Correct !")
