# ============================================================
# Resident Evil — trousse et corridors
# ============================================================
# Programme texte : ligne radio d'inventaire, présence d'un objet, stress le long
# d'un couloir répétitif, assemblage de trousses en nombre entier, estimation des
# coups pour une porte coincée.
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
    briefing_line,
    inventory_has,
    corridor_stress,
    medkits_from_parts,
    hits_to_destroy,
)


def main():
    print("=== Resident Evil — trousse et corridors ===\n")

    ligne = briefing_line("Leon", 3)
    print(f"Ligne radio : {ligne}")

    trousse = ["spray", "herbe verte", "munitions 9mm"]
    print(f"Herbe verte dans la trousse ? {inventory_has('herbe verte', trousse)}")
    print(f"Cartouche shotgun dans la trousse ? {inventory_has('cartouche', trousse)}")

    stress = corridor_stress(6)
    print(f"\nStress cumulé sur le couloir (6 segments) : {stress}")

    kits = medkits_from_parts(25, 8)
    print(f"Trousses complètes avec 25 composants (8 par trousse) : {kits}")

    coups = hits_to_destroy(50, 12)
    print(f"Coup nécessaires pour une porte à 50 PV (12 par coup) : {coups}")

    print("\n✅ Briefing terminé — tout roule.")


if __name__ == "__main__":
    main()
