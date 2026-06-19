# ============================================================
# Resident Evil — munitions après les tirs
# ============================================================
# Leon tire sur des zombies. La fonction balles_restantes() calcule
# combien il reste de balles. Le résultat ne peut pas être négatif.
#
# Lance : python3 02_fonction_params.py
# ============================================================

#   stock   : balles au départ (int)
#   tirees  : balles tirées (int)
#
# balles_restantes(30, 7)   →  30 - 7 = 23   →  retourne 23
# balles_restantes(5, 12)   →  5 - 12 = -7   →  plafonné à 0, retourne 0
#
# Résultat attendu :
#   balles_restantes(30, 7) == 23
#   balles_restantes(5, 12) == 0
#
# Indice : return + max(0, stock - tirees)

def balles_restantes(stock, tirees):
    return max(0, stock - tirees)


# --- Vérification (ne pas modifier) ---
assert balles_restantes(30, 7) == 23, "balles_restantes(30, 7) doit retourner 23"
assert balles_restantes(5, 12) == 0, "balles_restantes(5, 12) doit retourner 0"
print("✅ Correct !")
