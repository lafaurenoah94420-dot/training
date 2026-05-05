# ============================================================
# The Last of Us — cibles prioritaires
# ============================================================
# Chaque nombre dans la liste est la vie d'un infecté repéré.
# Compte combien ont strictement plus de 25 PV (cibles à traiter en priorité).
# Stocke ce nombre dans `risque_eleve`.
#
# Résultat attendu quand tu lances ce fichier :
#   ✅ Correct !
# ============================================================

pv_infectes = [30, 12, 40, 25, 50, 10]

risque_eleve = 0

# À toi — boucle for et condition if :

for pv in pv_infectes:
    if pv > 25:
        risque_eleve += 1

# --- Vérification (ne pas modifier) ---
assert risque_eleve == 3, (
    f"Obtenu : {risque_eleve} — attendu : 3 "
    "(strictement plus de 25 : 30, 40 et 50 ; 25 ne compte pas)."
)
print("✅ Correct !")