# ============================================================
# Resident Evil — Inventaire d'herbes
# ============================================================
# Leon gère ses herbes : libellés, ajout à l'inventaire, vérif
# d'une herbe, comptage, et message d'état selon ses PV.
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
    format_herb_label,
    add_herb,
    has_herb,
    count_herb_type,
    health_status,
)


def main():
    print("=== Resident Evil — Inventaire d'herbes ===\n")

    ligne = format_herb_label("Herbe verte", 3)
    print(f"Ligne inventaire : {ligne}")

    inventaire = ["Herbe rouge"]
    add_herb(inventaire, "Herbe verte")
    add_herb(inventaire, "Herbe verte")
    add_herb(inventaire, "Spray")
    print(f"Sac après ramassage : {inventaire}")

    possede = has_herb(inventaire, "Herbe verte")
    print(f"Leon a une Herbe verte ? {possede}")

    manque = has_herb(inventaire, "Herbe bleue")
    print(f"Leon a une Herbe bleue ? {manque}")

    nb_vertes = count_herb_type(inventaire, "Herbe verte")
    print(f"Nombre d'Herbes vertes : {nb_vertes}")

    etat = health_status(35)
    print(f"État à 35 PV : {etat}")

    etat_bas = health_status(15)
    print(f"État à 15 PV : {etat_bas}")

    print("\n✅ Leon sait ce qu'il a dans le sac — prêt pour le boss.")


if __name__ == "__main__":
    main()
