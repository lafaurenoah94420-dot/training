# ============================================================
# Hearts of Iron — puissance de division
# ============================================================
# Une division a des régiments. La puissance totale est le nombre
# de régiments multiplié par 10.
#
# Lance : python3 04_fonction.py
# ============================================================

#   regiments : nombre de régiments dans la division
#
# puissance(3)  =>  3 * 10 = 30
# puissance(7)  =>  7 * 10 = 70
#
# Résultat attendu : puissance(3) == 30  et  puissance(7) == 70
#
# Indice : def + return + *

def puissance(regiments):
    return regiments * 10


# --- Vérification (ne pas modifier) ---
assert puissance(3) == 30, "puissance(3) doit retourner 30"
assert puissance(7) == 70, "puissance(7) doit retourner 70"
print("✅ Correct !")
