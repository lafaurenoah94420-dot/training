# ============================================================
# GTA — Casier de Franklin
# ============================================================
# Tu gères le casier judiciaire de Franklin : amendes, dettes,
# statut recherché, total des contraventions et infractions graves.
#
# Ce que tu dois faire :
# → Ouvre project.py et implémente les 5 fonctions dans l'ordre
# → Lance python3 ../run_build.py après chaque fonction (depuis exos/)
#   ou python3 main.py si tu es déjà dans build/
#
# Critères de réussite :
# → python3 main.py tourne jusqu'au ✅ sans erreur
# → Chaque fonction produit les résultats montrés dans les exemples =>
# → Aucun raise NotImplementedError ne reste dans project.py
# ============================================================
# NE PAS MODIFIER CE FICHIER.
# ============================================================

from project import (
    fine_amount,
    debt_remaining,
    is_wanted,
    total_fines,
    count_serious,
)


def main():
    print("=== GTA — Casier de Franklin ===\n")

    amende = fine_amount(3)
    print(f"Amende pour 3 crimes : {amende}$")

    reste = debt_remaining(5000, 3200)
    print(f"Dette restante après paiement : {reste}$")

    recherche = is_wanted(2)
    print(f"Franklin est recherché ? {recherche}")

    calme = is_wanted(0)
    print(f"Franklin est clean ? {calme}")

    contraventions = [200, 500, 150, 800, 300]
    total = total_fines(contraventions)
    print(f"Total des amendes sur la liste : {total}$")

    graves = count_serious(contraventions, 400)
    print(f"Infractions graves (>= 400$) : {graves}")

    print("\n✅ Casier à jour — pour l'instant.")


if __name__ == "__main__":
    main()
