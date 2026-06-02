# ============================================================
# The Last of Us — Filtration à l'eau
# ============================================================
# Joel prépare de l'eau potable au camp : premier flacon en main,
# vérifie le charbon dans le sac, compte les flacons propres, simule
# des cycles de filtration et calcule l'eau récupérée.
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
    first_flask_name,
    has_charcoal,
    count_clean_flasks,
    filter_cycles_needed,
    liters_from_cycles,
)


def main():
    print("=== The Last of Us — Filtration à l'eau ===\n")

    flasks = ["flacon_A", "flacon_B", "gourde"]
    print(f"Premier flacon à traiter : {first_flask_name(flasks)}")

    backpack = ["corde", "charbon", "tissu"]
    print(f"Charbon dans le sac : {has_charcoal(backpack)}")

    backpack_sans = ["corde", "tissu"]
    print(f"Charbon (sans charbon) : {has_charcoal(backpack_sans)}")

    statuses = ["propre", "sale", "propre", "sale", "propre"]
    clean = count_clean_flasks(statuses)
    print(f"Flacons propres : {clean}")

    cycles = filter_cycles_needed(47)
    print(f"Cycles pour purifier (saleté 47) : {cycles}")

    liters = liters_from_cycles(4)
    print(f"Litres récupérés après 4 cycles : {liters}")

    print("\n✅ L'eau est potable — Joel peut boire.")


if __name__ == "__main__":
    main()
