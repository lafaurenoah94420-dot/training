# ============================================================
# The Last of Us — ciblage prioritaire
# ============================================================
# Joel scanne la zone : chaque nombre dans la liste est le niveau
# de PV d'un infecté repéré. Ceux qui ont strictement plus de 25 PV
# sont dangereux et doivent être éliminés en priorité.
# Combien y en a-t-il ?
#
# Lance : python 04_for_si.py
# ============================================================

pv_infectes = [30, 12, 40, 25, 50, 10]
risque_eleve = 0

# Parcours la liste pv_infectes. Pour chaque infecté,
# si ses PV sont strictement supérieurs à 25, ajoute 1 à risque_eleve.
# Attention : un infecté à exactement 25 PV ne compte pas.
#
# pv_infectes = [30, 12, 40, 25, 50, 10]
# 30 > 25 ? oui  →  risque_eleve = 1
# 12 > 25 ? non  →  risque_eleve = 1
# 40 > 25 ? oui  →  risque_eleve = 2
# 25 > 25 ? non  →  risque_eleve = 2  (25 ne compte pas)
# 50 > 25 ? oui  →  risque_eleve = 3
# 10 > 25 ? non  →  risque_eleve = 3
#
# Résultat attendu : risque_eleve == 3
#
# Indice : boucle for, puis if à l'intérieur de la boucle

for pv in pv_infectes:
    if pv > 25:
        risque_eleve += 1


# --- Vérification (ne pas modifier) ---
assert risque_eleve == 3, (
    f"Obtenu : {risque_eleve} — attendu : 3 "
    "(strictement plus de 25 : 30, 40 et 50 ; 25 ne compte pas)."
)
print("✅ Correct !")
