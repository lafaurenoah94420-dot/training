# ============================================================
# GTA — amende de Franklin
# ============================================================
# La police calcule une amende : prix de base + bonus si vitesse
# excessive. Écris une fonction qui retourne le total.
#
# Lance : python3 03_fonction.py
# ============================================================

#   amende(base, bonus_vitesse)
#
# amende(200, 0)    =>  200   (200 + 0)
# amende(200, 150)  =>  350   (200 + 150)
# amende(50, 30)    =>  80    (50 + 30)
#
# Résultat attendu : les trois appels ci-dessus
#
# Indice : def amende(base, bonus_vitesse):  puis  return base + bonus_vitesse

# À toi :
def amende(base, bonus_vitesse):
    return base + bonus_vitesse

# --- Vérification (ne pas modifier) ---
assert amende(200, 0) == 200, "amende(200, 0) doit retourner 200"
assert amende(200, 150) == 350, "amende(200, 150) doit retourner 350"
assert amende(50, 30) == 80, "amende(50, 30) doit retourner 80"
print("✅ Correct !")
