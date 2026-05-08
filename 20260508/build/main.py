# ============================================================
# The Last of Us — Couloir sans issue
# ============================================================
# Programme texte : munitions après tir et ramasse, état du survivant selon la vie,
# addition des dégâts sur plusieurs infectés, fusion de chargeurs, tirage de qui
# ouvre la porte en premier.
#
# Ce que tu dois faire :
# → Ouvre project.py et implémente les 5 fonctions dans l'ordre
# → Lance python3 main.py après chaque fonction pour voir si ça avance
#
# Critères de réussite :
# → python3 main.py tourne jusqu'au ✅ sans erreur
# → Chaque fonction produit les résultats montrés dans les exemples =>
# → Aucun raise NotImplementedError ne reste dans project.py
# ============================================================
# NE PAS MODIFIER CE FICHIER.
# ============================================================

import random

from project import (
    ammo_after_exchange,
    survivor_condition,
    total_shots_land,
    combine_magazines,
    who_opens_door,
)


def main():
    print("=== The Last of Us — Couloir sans issue ===\n")

    reste = ammo_after_exchange(30, 12, 5)
    print(f"Munitions après rafale + ramasse : {reste}")

    sec = ammo_after_exchange(8, 15, 0)
    print(f"Plus une balle utile (plancher 0) : {sec}")

    for vie in (85, 44, 12):
        print(f"Vie {vie} → état : {survivor_condition(vie)}")

    cumul = total_shots_land([6, 14, 5, 11])
    print(f"Dégâts cumulés sur la meute : {cumul}")

    combine = combine_magazines(9, 6)
    print(f"Ballettes prêtes à chamber : {combine}")

    random.seed(7)
    premier = who_opens_door("Joel", "Ellie")
    print(f"Qui ouvre la porte en premier : {premier}")

    print("\n✅ Couloir franchi — vous vous éclipsez.")


if __name__ == "__main__":
    main()
