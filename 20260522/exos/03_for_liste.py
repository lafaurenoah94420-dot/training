# ============================================================
# GTA — total des amendes
# ============================================================
# Franklin doit payer toutes ses amendes d'un coup. Additionne
# chaque montant de la liste pour obtenir la dette totale.
#
# Lance : python3 03_for_liste.py
# ============================================================

amendes = [150, 500, 75, 1200, 300]
dette_totale = 0

# Parcours amendes et additionne chaque montant dans dette_totale.
#
# tour 1 : m = 150   →  dette_totale = 0 + 150   = 150
# tour 2 : m = 500   →  dette_totale = 150 + 500  = 650
# tour 3 : m = 75    →  dette_totale = 650 + 75   = 725
# tour 4 : m = 1200  →  dette_totale = 725 + 1200 = 1925
# tour 5 : m = 300   →  dette_totale = 1925 + 300 = 2225
#
# Résultat attendu : dette_totale == 2225
#
# Indice : for ... in amendes  et  +=

# À toi :
for i in amendes:
    dette_totale += i

# --- Vérification (ne pas modifier) ---
assert dette_totale == 2225, f"Obtenu : {dette_totale}, attendu : 2225"
print("✅ Correct !")
