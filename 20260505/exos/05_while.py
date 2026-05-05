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

# Tant que mobilisation est inférieure à 50, ajoute 8 et compte une semaine.
# La boucle s'arrête dès que mobilisation atteint ou dépasse 50.
#
# départ        : mobilisation = 10, semaines = 0
# après tour 1  : mobilisation = 18, semaines = 1
# après tour 2  : mobilisation = 26, semaines = 2
# après tour 3  : mobilisation = 34, semaines = 3
# après tour 4  : mobilisation = 42, semaines = 4
# après tour 5  : mobilisation = 50, semaines = 5  →  50 >= 50, la boucle s'arrête
#
# Résultat attendu : semaines == 5
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
