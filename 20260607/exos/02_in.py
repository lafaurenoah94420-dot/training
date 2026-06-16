# ============================================================
# Resident Evil — Code porte du labo
# ============================================================
# Leon a une liste de codes valides. Vérifie si son code ouvre la porte.
#
# Lance : python3 02_in.py
# ============================================================

codes_valides = ["A12", "B45", "OMEGA"]
code_saisi = "B45"
acces = False

# Si code_saisi est dans codes_valides, acces vaut True, sinon False.
#
# code_saisi = "B45"  →  "B45" est dans la liste  →  acces = True
# code_saisi = "ZZZ"  →  pas dans la liste  →  acces = False
#
# Résultat attendu : acces == True  (car code_saisi vaut "B45" ici)
#
# Indice : if ... in ...

# À toi :
if code_saisi in codes_valides:
    acces = True

# --- Vérification (ne pas modifier) ---
assert acces is True, f"acces vaut {acces}, attendu : True"
print("✅ Correct !")
