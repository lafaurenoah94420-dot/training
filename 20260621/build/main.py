# ============================================================
# Project Zomboid — Garde-manger de la safehouse
# ============================================================
# Avant la nuit, tu fais l'inventaire du garde-manger : tu lis
# les quantités par type, tu mets à jour ce que tu as ramené de
# Knoxville, tu vérifies s'il reste de quoi manger, tu comptes
# le total de rations et tu affiches un résumé pour la bande.
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
    ration_count,
    restock_food,
    has_food,
    total_rations,
    pantry_status,
)


def main():
    print("=== Project Zomboid — Garde-manger de la safehouse ===\n")

    pantry = {
        "conserves": 4,
        "pates": 2,
        "eau": 6,
    }

    conserves = ration_count(pantry, "conserves")
    print(f"Conserves en stock : {conserves}")

    restock_food(pantry, "pates", 5)
    print(f"Pâtes après razzia : {pantry['pates']}")

    eau_ok = has_food(pantry, "eau")
    print(f"Il reste de l'eau : {eau_ok}")

    chips_ok = has_food(pantry, "chips")
    print(f"Il reste des chips : {chips_ok}")

    total = total_rations(pantry)
    print(f"Total de rations : {total}")

    rapport = pantry_status(pantry)
    print(rapport)

    print("\n✅ Le garde-manger est à jour — la nuit peut commencer.")


if __name__ == "__main__":
    main()
