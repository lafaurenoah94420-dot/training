# ============================================================
# Resident Evil — inventaire de Leon
# ============================================================
# Leon fouille son sac. Le programme doit vérifier si "spray"
# est dans la liste d'objets qu'il transporte.
#
# Lance : python3 02_in.py
# ============================================================

sac = ["herbe", "spray", "munitions"]
a_spray = False

# Vérifie si "spray" est dans la liste sac.
# Stocke le résultat (vrai ou faux) dans a_spray.
#
# "spray" in sac  →  True  (car "spray" est dans la liste)
#
# Résultat attendu : a_spray == True
#
# Indice : mot-clé in

# À toi :
if "spray" in sac:
    a_spray = True

# --- Vérification (ne pas modifier) ---
assert a_spray == True, f"Obtenu : {a_spray}, attendu : True"
print("✅ Correct !")
