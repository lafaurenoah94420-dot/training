# ============================================================
# Hearts of Iron IV — bureau de mobilisation
# ============================================================
# Ce programme calcule la production hebdomadaire d'équipements, simule
# un tirage de bonus de recrues avec une graine fixe, puis estime combien
# de jours il faut pour atteindre un stock militaire cible.
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

from project import equipment_produced, event_conscripts_bonus, days_to_reach_stock


def main():
    print("=== Hearts of Iron IV — bureau de mobilisation ===\n")

    weekly = equipment_produced(4, 25)
    print(f"Production cette semaine : {weekly} équipements (4 usines × 25).")

    bonus = event_conscripts_bonus(99)
    print(f"Événement national — bonus recrues : +{bonus} (tirage avec graine 99).")

    jours = days_to_reach_stock(200, 75, 500)
    print(f"Pour passer de 200 à au moins 500 avec +75/j : {jours} jour(s).")

    print("\n--- Cas limites ---")
    print(f"Sans usine : {equipment_produced(0, 100)} équipement(s).")
    print(f"Déjà au stock visé : {days_to_reach_stock(500, 10, 500)} jour(s).")

    print("\n✅ Si tu lis ce message sans erreur, les 3 fonctions sont OK.")


if __name__ == "__main__":
    main()
