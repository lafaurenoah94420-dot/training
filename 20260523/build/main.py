# ============================================================
# Resident Evil — Armoire du commissariat
# ============================================================
# Leon fouille l'armoire de la salle de stars : tirage au sort d'un
# compartiment, lecture des soins dans la table des objets, calcul des PV
# après une attaque, et inventaire total de l'armoire.
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
    pick_locker_item,
    supply_code_length,
    heal_amount,
    hp_after_attack,
    total_supplies,
)


def main():
    print("=== Resident Evil — Armoire du commissariat ===\n")

    locker = ["herbe_verte", "herbe_bleue", "spray", "munitions"]
    found = pick_locker_item(locker)
    print(f"Compartiment ouvert : {found}")

    length = supply_code_length(found)
    print(f"Longueur du code objet : {length} caractères")

    heal_table = {
        "herbe_verte": 25,
        "herbe_bleue": 50,
        "spray": 80,
        "munitions": 0,
    }
    heal = heal_amount("herbe_bleue", heal_table)
    print(f"Soin herbe_bleue : {heal} PV")

    hp = hp_after_attack(80, 30, 10)
    print(f"PV après attaque (80, 30, 10) : {hp}")

    hp_low = hp_after_attack(15, 25, 5)
    print(f"PV après attaque (15, 25, 5) : {hp_low}")

    cabinet = {"herbe_verte": 3, "herbe_bleue": 1, "spray": 2, "munitions": 5}
    total = total_supplies(cabinet)
    print(f"Total objets dans l'armoire : {total}")

    print("\n✅ Leon sait ce qu'il peut soigner — les zombies peuvent venir.")


if __name__ == "__main__":
    main()
