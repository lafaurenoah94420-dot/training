# ============================================================
# Project Zomboid — jauge de faim
# ============================================================
# Ce programme simule la jauge de faim d'un survivant.
# Manger la fait baisser, le temps qui passe la fait monter.
# Un message d'état résume la situation à la fin.
#
# Ce que tu dois faire :
# → Ouvre project.py et implémente les 3 fonctions dans l'ordre
# → Lance python main.py après chaque fonction pour voir si ça avance
#
# Critères de réussite :
# → python main.py tourne jusqu'au ✅ sans erreur
# → Chaque fonction produit les résultats montrés dans les exemples =>
# → Aucun raise NotImplementedError ne reste dans project.py
# ============================================================
# NE PAS MODIFIER CE FICHIER.
# ============================================================

from project import eat_reduce_hunger, hunger_from_time_passing, hunger_status_message


def main():
    print("=== Project Zomboid — jauge de faim ===\n")

    hunger = 72
    print(f"Au réveil, la faim est à {hunger}/100.")

    hunger = eat_reduce_hunger(hunger, 35)
    print(f"Après une boîte de conserve : faim à {hunger}/100.")

    hunger = hunger_from_time_passing(hunger, 6, 3)
    print(f"Après 3 h à fouiller sans manger (+6/h) : faim à {hunger}/100.")

    msg = hunger_status_message(hunger)
    print(f"\nÉtat : {msg}")

    print("\n--- Deuxième test (cas extrême) ---")
    h = eat_reduce_hunger(15, 40)
    print(f"Manger beaucoup avec peu de faim : faim à {h}/100 (minimum 0).")

    h2 = hunger_from_time_passing(95, 10, 2)
    print(f"Faim déjà haute + 2 h passées : faim à {h2}/100 (plafond 100).")

    print("\n✅ Si tu lis ce message sans erreur, les 3 fonctions sont OK.")


if __name__ == "__main__":
    main()
