# ============================================================
# Resident Evil — Inventaire du commissariat
# ============================================================
# Tu gères l'armurerie de Leon : ajouter des armes, vérifier
# si un objet est présent, compter les munitions, repérer les
# armes puissantes et totaliser le poids du sac.
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
    add_weapon,
    has_weapon,
    total_ammo,
    count_powerful,
    total_weight,
)


def main():
    print("=== Resident Evil — Inventaire du commissariat ===\n")

    armory = ["couteau"]
    count = add_weapon(armory, "pistolet")
    print(f"Armes : {armory} ({count} au total)")

    add_weapon(armory, "fusil à pompe")
    print(f"Armes après 2e ajout : {armory}")

    trouve = has_weapon(armory, "pistolet")
    print(f"Pistolet dans l'armurerie ? {trouve}")

    absent = has_weapon(armory, "lance-roquettes")
    print(f"Lance-roquettes présent ? {absent}")

    munitions = total_ammo([12, 8, 30, 5])
    print(f"Munitions totales : {munitions}")

    puissantes = count_powerful([5, 15, 8, 20, 12], 10)
    print(f"Armes au-dessus de 10 dégâts : {puissantes}")

    poids = total_weight([6, 4, 2, 8])
    print(f"Poids total du sac (kg) : {poids}")

    print("\n✅ Armurerie prête — bonne chance contre les zombies.")


if __name__ == "__main__":
    main()
