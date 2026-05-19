# ============================================================
# GTA — Comptoir de liasses
# ============================================================
# Programme texte : liasses entières dans un butin, palier de recherche en trois
# niveaux, phrase radio formatée, liste de pseudos du crew, réputation plafonnée.
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
    full_stacks,
    wanted_tier,
    radio_line,
    crew_roster,
    cap_rep,
)


def main():
    print("=== GTA — Comptoir de liasses ===\n")

    stacks = full_stacks(1000, 50)
    print(f"Liasses complètes de 50$ dans 1000$ : {stacks}")

    niveau = wanted_tier(3)
    print(f"Niveau radio (3 étoiles) : {niveau}")

    msg = radio_line("Fox", "Vinewood")
    print(msg)

    equipe = crew_roster()
    print(f"Pseudos enregistrés : {equipe}")

    rep = cap_rep(85, 30)
    print(f"Réputation après coup (plafond 100) : {rep}")

    print("\n✅ Comptoir fermé — tout est carré.")


if __name__ == "__main__":
    main()
