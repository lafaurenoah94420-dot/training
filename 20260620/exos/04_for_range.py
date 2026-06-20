# ============================================================
# Hearts of Iron 4 — production d'usines
# ============================================================
# Tu as 6 usines militaires. Chacune produit 12 équipements par jour.
# Calcule la production totale sur la semaine (7 jours).
#
# Lance : python3 04_for_range.py
# ============================================================

usines = 6
production_par_usine = 12
total_equipement = 0

# Boucle 7 fois (7 jours). À chaque tour, ajoute la production du jour
# à total_equipement. Production d'un jour = usines × production_par_usine
#
# un jour : 6 × 12 = 72 équipements
# 7 jours : 72 × 7 = 504 équipements
#
# tour 1 : total = 0 + 72 = 72
# tour 2 : total = 72 + 72 = 144
# ... (7 tours au total)
#
# Résultat attendu : total_equipement == 504
#
# Indice : for ... in range(7) + +=

# À toi :
for i in range(7):
    total_equipement += usines * production_par_usine


# --- Vérification (ne pas modifier) ---
assert total_equipement == 504, f"Obtenu : {total_equipement}, attendu : 504"
print("✅ Correct !")
