# ============================================================
# GTA — amendes empilées
# ============================================================
# Michael doit additionner les montants des amendes numérotées de 1 à 9 : la 1ère
# vaut 20$, la 2ème aussi, … jusqu'à la 9ème (toujours 20$ par amendes).
# Calcule le total dans total_amendes avec une boucle for et range.
#
# Lance : python3 03_range.py
# ============================================================

montant_par_amende = 20
nombre_amendes = 9

total_amendes = 0

# Additionne montant_par_amende pour chaque numéro de 1 jusqu'à nombre_amendes.
#
# Déroulé (valeurs actuelles) :
#   tour 1 → ajouter 20 → total 20
#   tour 2 → ajouter 20 → total 40
#   …
#   tour 9 → ajouter 20 → total 180
#
# Résultat attendu : total_amendes == 180
#
# Indice : for i in range(1, nombre_amendes + 1) puis total_amendes += ...

# À toi :

for i in range(1, nombre_amendes + 1):
    total_amendes += montant_par_amende



# --- Vérification (ne pas modifier) ---
assert total_amendes == 180, (
    f"Obtenu : {total_amendes} — attendu : 180 (9 × 20)."
)
print("✅ Correct !")
