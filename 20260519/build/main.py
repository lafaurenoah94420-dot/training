# ============================================================
# The Last of Us — Relais de ravitaillement
# ============================================================
# Programme texte : fréquences radio corrigées, lecture et réappro du cache,
# poids total des sacs, jours de rations restantes avec consommation par jour.
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
    format_channel,
    read_supply,
    restock,
    total_weight,
    rations_days,
)


def main():
    print("=== The Last of Us — Relais de ravitaillement ===\n")

    freq = format_channel("QZ_7")
    print(f"Fréquence affichée : {freq}")

    cache = {"bandages": 4, "bullets": 120, "food": 6}
    stock_food = read_supply(cache, "food")
    print(f"Rations en cache : {stock_food}")

    restock(cache, "food", 3)
    print(f"Rations après caisse (+3) : {cache['food']}")

    poids = total_weight([2, 5, 3, 1])
    print(f"Poids total des sacs (kg) : {poids}")

    jours = rations_days(24)
    print(f"Jours de rations (2/jour par défaut) : {jours}")

    jours_urgent = rations_days(25, 5)
    print(f"Jours de rations (5/jour) : {jours_urgent}")

    print("\n✅ Relais opérationnel — Joel peut passer la nuit.")


if __name__ == "__main__":
    main()
