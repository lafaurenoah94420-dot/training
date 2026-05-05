# ============================================================
# Hearts of Iron IV — mobilisation nationale
# ============================================================
# La jauge de mobilisation démarre à 10. Chaque semaine, elle
# monte de 8 points. Dès qu'elle atteint ou dépasse 50, la montée
# s'arrête — l'armée est prête. Combien de semaines faut-il ?
#
# Lance : python 05_while.py
# ============================================================

mobilisation = 10
semaines = 0

# Fais monter mobilisation de 8 par semaine jusqu'à ce qu'elle atteigne 50.
# Incrémente semaines à chaque tour de boucle.
#
# départ : mobilisation = 10, semaines = 0
# après 5 tours : mobilisation = 50, semaines = 5
#
# Indice : while + deux += dans le corps de la boucle

while mobilisation < 50:
    mobilisation += 8
    semaines += 1


# --- Vérification (ne pas modifier) ---
assert semaines == 5, (
    f"Obtenu : {semaines} semaines — reprends depuis 10 et ajoute 8 jusqu'à ≥ 50."
)
assert mobilisation >= 50, (
    f"mobilisation vaut {mobilisation} — la boucle doit s'arrêter une fois le seuil atteint."
)
print("✅ Correct !")
