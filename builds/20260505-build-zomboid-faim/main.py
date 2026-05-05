# Programme principal — ne pas modifier.
# Lis ce fichier pour comprendre ce que project.py doit fournir.

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
