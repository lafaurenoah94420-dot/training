# ============================================================
# Resident Evil — niveau de danger
# ============================================================
# L'écran tactique affiche un niveau de danger selon les PV de Leon.
# Plus de 50 PV → "Faible". Entre 20 et 50 → "Modéré". Moins de 20 → "Critique".
#
# Lance : python3 02_elif.py
# ============================================================

vie = 35
niveau = ""

# Détermine le niveau de danger selon la valeur de vie.
#
# vie = 35  →  35 > 50 ? non  →  35 >= 20 ? oui  →  niveau = "Modéré"
# vie = 60  →  60 > 50 ? oui  →  niveau = "Faible"
# vie = 10  →  10 > 50 ? non  →  10 >= 20 ? non  →  niveau = "Critique"
#
# Résultat attendu : niveau == "Modéré"  (car vie vaut 35 ici)
#
# Indice : if / elif / else

# À toi :
if vie > 50:
    niveau = "Faible"
elif vie <= 50 and vie > 20:
    niveau = "Modéré"
else:
    niveau = "Critique"

# --- Vérification (ne pas modifier) ---
assert niveau == "Modéré", f"Obtenu : '{niveau}', attendu : 'Modéré'"
print("✅ Correct !")
