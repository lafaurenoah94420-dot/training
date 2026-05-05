# ============================================================
# GTA — niveaux d'étoiles cumulés
# ============================================================
# La liste `niveaux` enregistre le nombre d'étoiles obtenues à chaque mission.
# Additionne toutes les valeurs et stocke le résultat dans `etoiles_total`.
#
# Résultat attendu quand tu lances ce fichier :
#   ✅ Correct !
# ============================================================

niveaux = [2, 1, 4, 1, 3]

etoiles_total = 0

# À toi — utilise une boucle for :

for x in niveaux:
    etoiles_total += x


# --- Vérification (ne pas modifier) ---
assert etoiles_total == 11, (
    f"Obtenu : {etoiles_total}, attendu : 11 (somme de 2+1+4+1+3)."
)
print("✅ Correct !")
