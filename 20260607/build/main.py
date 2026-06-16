# ============================================================
# Project Zomboid — Nuit de survie
# ============================================================
# Tu gères la soif, le stock de nourriture et les alertes de la nuit.
# Statuts en majuscules, vérif du sac, consommation heure par heure,
# total des dégâts subis, et événement aléatoire de la nuit.
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
    format_status,
    has_food,
    eat_while_hungry,
    total_damage,
    random_night_event,
)

import random


def main():
    random.seed(7)

    print("=== Project Zomboid — Nuit de survie ===\n")

    statut = format_status("faim critique")
    print(f"Alerte écran : {statut}")

    sac = ["conserve", "eau", "bandage"]
    trouve = has_food(sac, "eau")
    print(f"Sac contient de l'eau ? {trouve}")

    manque = has_food(sac, "fusil")
    print(f"Sac contient un fusil ? {manque}")

    reste = eat_while_hungry(food=14, hunger=10)
    print(f"Nourriture restante après grignotage : {reste}")

    degats = total_damage([5, 12, 3, 8])
    print(f"Dégâts totaux de la nuit : {degats}")

    evenements = ["horde", "pluie", "cauchemar", "silence"]
    nuit = random_night_event(evenements)
    print(f"Événement de la nuit : {nuit}")

    print("\n✅ Tu as survécu à la nuit — enfin presque.")


if __name__ == "__main__":
    main()
