# ============================================================
# The Last of Us — Sac à dos de Joel
# ============================================================
# Joel fouille son sac avant d'entrer dans un bâtiment infesté.
# Il doit savoir s'il a encore un kit de soin avant de partir.
#
# Lance : python3 02_in_liste.py
# ============================================================

sac = ["torche", "corde", "kit de soin", "briquet"]
a_un_kit = False

# Vérifie si "kit de soin" est dans la liste sac.
# Si oui, a_un_kit doit valoir True, sinon False.
#
# "kit de soin" in sac  →  True  →  a_un_kit = True
#
# Résultat attendu : a_un_kit == True
#
# Indice : mot-clé in  +  if

# À toi :
if "kit de soin" in sac:
    a_un_kit = True

# --- Vérification (ne pas modifier) ---
assert a_un_kit is True, f"Obtenu : {a_un_kit}, attendu : True"
print("✅ Correct !")
