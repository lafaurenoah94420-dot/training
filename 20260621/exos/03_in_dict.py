# ============================================================
# Project Zomboid — Vérifier le stock
# ============================================================
# Tu fouilles le placard de survie. Avant de cuisiner, tu veux
# savoir si tu as encore des conserves de haricots.
#
# Lance : python3 03_in_dict.py
# ============================================================

placard = {
    "haricots": 4,
    "eau": 2,
    "bandage": 1,
}

a_des_haricots = False

# Vérifie si la clé "haricots" est dans le dictionnaire placard.
# Stocke True ou False dans a_des_haricots.
#
# "haricots" est une clé de placard  →  a_des_haricots = True
# "pizza" ne serait pas dans placard  →  False
#
# Résultat attendu : a_des_haricots == True
#
# Indice : "cle" in dict

# À toi :
if "haricots" in placard:
    a_des_haricots = True

# --- Vérification (ne pas modifier) ---
assert a_des_haricots is True, f"Obtenu : {a_des_haricots}, attendu : True"
print("✅ Correct !")
