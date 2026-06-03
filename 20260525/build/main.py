# ============================================================
# Hearts of Iron IV — Rapport de moral
# ============================================================
# Tu gères le moral des divisions : codes de secteur, statut,
# pertes après bataille, conditions pour attaquer, bilan des pertes.
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

from project import (
    sector_number,
    morale_status,
    morale_after_battle,
    front_can_attack,
    count_heavy_losses,
)


def main():
    print("=== Hearts of Iron IV — Rapport de moral ===\n")

    code = "ARM-7-F"
    print(f"Secteur extrait du rapport {code} : {sector_number(code)}")

    print(f"Moral 85 : {morale_status(85)}")
    print(f"Moral 42 : {morale_status(42)}")
    print(f"Moral 12 : {morale_status(12)}")

    after = morale_after_battle(60, 15)
    print(f"Moral après bataille (60, perte 15) : {after}")

    after_extra = morale_after_battle(60, 15, 5)
    print(f"Moral avec malus extra (60, 15, 5) : {after_extra}")

    peut = front_can_attack(45, True, True)
    print(f"Le front peut attaquer (45, ravitaillement OK, ordres OK) : {peut}")

    batailles = [
        {"branche": "infanterie", "pertes": 120},
        {"branche": "infanterie", "pertes": 40},
        {"branche": "artillerie", "pertes": 200},
        {"branche": "infanterie", "pertes": 95},
    ]
    lourdes = count_heavy_losses(batailles)
    print(f"Batailles d'infanterie avec pertes >= 100 : {lourdes}")

    print("\n✅ Le haut commandement a son rapport — la guerre continue.")


if __name__ == "__main__":
    main()
