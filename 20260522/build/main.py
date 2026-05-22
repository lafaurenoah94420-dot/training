# ============================================================
# GTA — Bilan d'amendes de Franklin
# ============================================================
# Programme texte : libellés d'amendes, ajout au dossier, total dû,
# comptage des grosses contraventions, dette après pot-de-vin.
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
    format_fine_label,
    add_fine,
    total_fines,
    count_over_amount,
    debt_after_payment,
)


def main():
    print("=== GTA — Bilan d'amendes de Franklin ===\n")

    ligne = format_fine_label("Excès de vitesse", 150)
    print(f"Ligne ticket : {ligne}")

    dossier = [200, 75]
    add_fine(dossier, 500)
    add_fine(dossier, 120)
    print(f"Montants dans le dossier : {dossier}")

    somme = total_fines([150, 500, 75, 1200, 300])
    print(f"Total des amendes (liste test) : {somme} €")

    grosses = count_over_amount([150, 500, 75, 1200, 300], 500)
    print(f"Amendes strictement au-dessus de 500 € : {grosses}")

    reste = debt_after_payment(800, 250)
    print(f"Dette après pot-de-vin (800 - 250) : {reste} €")

    reste_zero = debt_after_payment(100, 200)
    print(f"Dette après gros paiement (100 - 200) : {reste_zero} €")

    print("\n✅ Franklin connaît sa dette — décide s'il paye ou s'il fuit.")


if __name__ == "__main__":
    main()
