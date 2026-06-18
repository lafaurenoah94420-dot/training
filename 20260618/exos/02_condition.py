# ============================================================
# Project Zomboid — niveau de faim
# ============================================================
# L'HUD affiche un mot selon la faim du survivant :
#   plus de 80  →  "Rassasié"
#   plus de 30  →  "Correct"
#   sinon       →  "Affamé"
#
# Ton personnage a faim = 65. Quel mot s'affiche ?
#
# Lance : python3 02_condition.py
# ============================================================

faim = 65
statut = ""

# Détermine statut avec if / elif / else.
#
# faim = 65
#   65 > 80 ?  non
#   65 > 30 ?  oui  →  statut = "Correct"
#
# (si faim valait 90  →  "Rassasié" ; si 10  →  "Affamé")
#
# Résultat attendu : statut == "Correct"
#
# Indice : if / elif / else

# À toi :
if faim > 80:
    statut = "Rassasié"
elif faim <= 80 and faim > 30:
    statut = "Correct"
else:
    statut ="Affamé"

# --- Vérification (ne pas modifier) ---
assert statut == "Correct", f"Obtenu : '{statut}', attendu : 'Correct'"
print("✅ Correct !")
