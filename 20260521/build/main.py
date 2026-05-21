# ============================================================
# Project Zomboid — Barricader les fenêtres
# ============================================================
# Programme texte : planches après une barricade, alerte de stock, barricade
# de toute la maison, vérif d'outil dans le sac, nuits d'assiège jusqu'au calme.
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
    planks_after_window,
    stock_message,
    barricade_all_windows,
    has_tool,
    nights_until_quiet,
)


def main():
    print("=== Project Zomboid — Barricader les fenêtres ===\n")

    restant = planks_after_window(12, 3)
    print(f"Planches après 1 fenêtre (12 - 3) : {restant}")

    msg = stock_message(3)
    print(f"Alerte stock (3 planches) : {msg}")

    final = barricade_all_windows(20, 4, 3)
    print(f"Planches après 4 fenêtres à 3 chacune (départ 20) : {final}")

    sac = ["marteau", "clous", "scie"]
    ok = has_tool(sac, "marteau")
    print(f"Marteau dans le sac ? {ok}")

    nuits = nights_until_quiet(10, 3)
    print(f"Nuits avant le calme (bruit 10, -3/nuit) : {nuits}")

    print("\n✅ Maison barricadée — la nuit peut commencer.")


if __name__ == "__main__":
    main()
