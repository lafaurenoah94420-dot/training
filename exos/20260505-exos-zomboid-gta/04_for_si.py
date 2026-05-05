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

# Compte les infectés avec pv strictement > 25
#
# pour [30, 12, 40, 25, 50, 10]  =>  risque_eleve == 3
# (30, 40 et 50 comptent — 25 ne compte pas, il faut strictement plus)
#
# Indice : boucle for + if à l'intérieur

for pv in pv_infectes:
    if pv > 25:
        risque_eleve += 1


# --- Vérification (ne pas modifier) ---
assert risque_eleve == 3, (
    f"Obtenu : {risque_eleve} — attendu : 3 "
    "(strictement plus de 25 : 30, 40 et 50 ; 25 ne compte pas)."
)
print("✅ Correct !")
