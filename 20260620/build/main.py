# ============================================================
# Resident Evil — Armoire du RPD
# ============================================================
# Leon fouille l'armoire de la police : il compte ce qu'il y a
# dedans, range les objets trouvés, dénombre les herbes et résume
# l'inventaire avant de repartir dans les couloirs.
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
    locker_slots,
    stash_item,
    count_herbs,
    total_heal_power,
    locker_status,
)


def main():
    print("=== Resident Evil — Armoire du RPD ===\n")

    armoire = ["spray", "herbe_verte", "munitions"]
    slots = locker_slots(armoire)
    print(f"Compartiments occupés : {slots}")

    armoire = stash_item(armoire, "herbe_bleue")
    print(f"Après fouille : {armoire}")

    verts = count_herbs(armoire, "herbe_verte")
    print(f"Herbes vertes : {verts}")

    soins = [25, 50, 25, 80]
    puissance = total_heal_power(soins)
    print(f"PV récupérables sur la table : {puissance}")

    rapport = locker_status(armoire)
    print(rapport)

    print("\n✅ L'armoire est cataloguée — les zombies peuvent attendre.")


if __name__ == "__main__":
    main()
