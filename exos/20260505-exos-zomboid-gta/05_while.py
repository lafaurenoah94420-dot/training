# ============================================================
# Hearts of Iron IV — montée de la mobilisation
# ============================================================
# La jauge `mobilisation` commence à 10. Chaque semaine elle augmente de 8.
# Dès que `mobilisation` atteint ou dépasse 50, la montée s'arrête.
# Compte le nombre de semaines écoulées dans `semaines` (une incrémentation par semaine).
#
# Résultat attendu quand tu lances ce fichier :
#   ✅ Correct !
# ============================================================

mobilisation = 10
semaines = 0

while mobilisation < 50:
    mobilisation += 8
    semaines += 1

# À toi — boucle while :


# --- Vérification (ne pas modifier) ---
assert semaines == 5, (
    f"Obtenu : {semaines} semaines — reprends depuis 10 et ajoute 8 jusqu'à ≥ 50."
)
assert mobilisation >= 50, (
    f"mobilisation vaut {mobilisation} — la boucle doit s'arrêter une fois le seuil atteint."
)
print("✅ Correct !")
