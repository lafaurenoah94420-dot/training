# ============================================================
# Hearts of Iron IV — cadence d’usine sur cinq jours
# ============================================================
# Une usine sort le même nombre de fusils chaque jour ouvré. On simule cinq jours
# et on additionne la production dans une variable qui part de zéro.
#
# Lance : python3 03_range.py
# ============================================================

fusils_par_jour = 14

production_totale = 0

# Ajoute fusils_par_jour à production_totale pour chaque jour sur une plage de 5 jours.
#
# jour 0 : +14  →  total 14
# jour 1 : +14  →  total 28
# jour 2 : +14  →  total 42
# jour 3 : +14  →  total 56
# jour 4 : +14  →  total 70
#
# Résultat attendu : production_totale == 70
#
# Indice : for ... in range(5) puis +=

# À toi :
for fusil in range(5):
    production_totale += fusils_par_jour


# --- Vérification (ne pas modifier) ---
assert production_totale == 70, (
    f"Obtenu : {production_totale} — attendu : 70 (5 × 14)."
)
print("✅ Correct !")
