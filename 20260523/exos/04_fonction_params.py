# ============================================================
# Resident Evil — Dégâts après armure
# ============================================================
# Leon reçoit des dégâts. L'armure absorbe une partie des coups
# avant d'affecter ses points de vie. Le jeu calcule les PV restants.
#
# Lance : python3 04_fonction_params.py
# ============================================================

#   vie      : points de vie actuels
#   degats   : dégâts bruts de l'attaque
#   armure   : points absorbés par l'armure
#
# pv_restants(80, 30, 10)  →  80 - (30 - 10) = 80 - 20 = 60
# pv_restants(15, 25, 5)   →  15 - (25 - 5) = 15 - 20 = -5  →  0 (minimum)
#
# Résultat attendu : pv_restants(80, 30, 10) == 60
#                    pv_restants(15, 25, 5) == 0
#
# Indice : return + max(0, ...) avec 3 paramètres

def pv_restants(vie, degats, armure):
    return max(0, vie - (degats - armure))


# --- Vérification (ne pas modifier) ---
assert pv_restants(80, 30, 10) == 60, "80 - (30-10) = 60"
assert pv_restants(15, 25, 5) == 0, "15 - 20 = -5, plafonné à 0"
print("✅ Correct !")
