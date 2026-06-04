# ============================================================
# GTA — Partage du butin
# ============================================================
# Après un braquage : type de butin au hasard, parts dans un dict
# d'équipe, part de Franklin en %, total des liasses, compte à rebours
# police tant qu'il reste du temps pour finir le partage.
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
    pick_loot_type,
    add_crew_cut,
    franklin_percent,
    sum_payouts,
    countdown_police,
)


def main():
    print("=== GTA — Partage du butin ===\n")

    types = ["liasses", "bijoux", "or"]
    butin = pick_loot_type(types)
    print(f"Type de butin tiré : {butin}")

    parts = {"Franklin": 0, "Lamar": 0, "Trevor": 0}
    add_crew_cut(parts, "Lamar", 1200)
    add_crew_cut(parts, "Trevor", 800)
    add_crew_cut(parts, "Lamar", 300)
    print(f"Parts équipe : {parts}")

    part_franklin = franklin_percent(10000, 40)
    print(f"40 % de 10 000 $ pour Franklin : {part_franklin} $")

    total = sum_payouts([1500, 2200, 900, 400])
    print(f"Total des liasses comptées : {total} $")

    reste = countdown_police(120, 25)
    print(f"Secondes restantes avant les flics (120, pas de 25) : {reste} s")

    reste_court = countdown_police(30, 25)
    print(f"Secondes restantes (30, pas de 25) : {reste_court} s")

    print("\n✅ Le butin est partagé — Franklin peut disparaître.")


if __name__ == "__main__":
    main()
