# ============================================================
# GTA — Franklin et le braquage
# ============================================================
# Franklin braque une supérette. Il faut au moins 500$ de butin
# ET qu'il n'y ait pas de flics devant (flics = False) pour qu'il
# puisse partir tranquille.
#
# Lance : python3 01_and_or.py
# ============================================================

butin = 650
flics = False
peut_partir = False

# Met peut_partir à True seulement si :
#   butin >= 500  ET  flics est False
#
# Ici : 650 >= 500 → oui,  flics = False → oui  →  peut_partir = True
#
# Résultat attendu : peut_partir == True
#
# Indice : if ... and ...

# À toi :
if butin >= 500 and flics == False:
    peut_partir = True

# --- Vérification (ne pas modifier) ---
assert peut_partir is True, f"Obtenu : {peut_partir}, attendu : True"
print("✅ Correct !")
