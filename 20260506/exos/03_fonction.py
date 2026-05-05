# ============================================================
# GTA — réparation express
# ============================================================
# Los Santos Customs facture un coup fixe par réparation, quel que soit
# le véhicule. La fonction doit renvoyer le coût total (pas l'afficher).
#
# Lance : python 03_fonction.py
# ============================================================

#   prix_fixe  : coût d'une intervention (en dollars)
#   nombre     : combien d'interventions
#
# cout_total(500, 2)  =>  500 * 2  =>  1000
# cout_total(200, 4)  =>  200 * 4  =>  800
#
# Résultat attendu : cout_total(500, 2) == 1000  et  cout_total(200, 4) == 800
#
# Indice : return et *

def cout_total(prix_fixe, nombre):
    pass  # remplace pass par ton code


# --- Vérification (ne pas modifier) ---
assert cout_total(500, 2) == 1000, "cout_total(500, 2) doit valoir 1000"
assert cout_total(200, 4) == 800, "cout_total(200, 4) doit valoir 800"
print("✅ Correct !")
