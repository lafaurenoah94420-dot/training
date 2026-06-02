# ============================================================
# Resident Evil — Munitions dans le chargeur
# ============================================================
# Leon tire dans un infecté jusqu'à ce que son chargeur soit vide.
# Chaque tir enlève 1 balle. Compte combien de tirs il a fait.
#
# Lance : python3 04_while.py
# ============================================================

balles = 4
tirs = 0

# Tant que balles est supérieur à 0 :
#   enlève 1 à balles
#   ajoute 1 à tirs
#
# départ : balles = 4, tirs = 0
# tour 1 : balles = 3, tirs = 1
# tour 2 : balles = 2, tirs = 2
# tour 3 : balles = 1, tirs = 3
# tour 4 : balles = 0, tirs = 4  →  boucle s'arrête
#
# Résultat attendu : tirs == 4
#
# Indice : while balles > 0:

# À toi :
while balles > 0:
    balles -= 1
    tirs += 1
    

# --- Vérification (ne pas modifier) ---
assert tirs == 4, f"Obtenu : {tirs}, attendu : 4"
assert balles == 0, f"Il devrait rester 0 balle, obtenu : {balles}"
print("✅ Correct !")
