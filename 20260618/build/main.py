# ============================================================
# Project Zomboid — Veille de nuit
# ============================================================
# Tu gères une nuit de siège : alertes par zone, niveau de menace,
# vagues d'infectés, état des provisions et dégâts à la barricade.
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
    format_zone_alert,
    threat_label,
    total_spawned,
    supply_status,
    barricade_damage,
)


def main():
    print("=== Project Zomboid — Veille de nuit ===\n")

    alerte = format_zone_alert("Garage", 3, 12)
    print(f"Radio : {alerte}")

    label = threat_label(8)
    print(f"Menace actuelle : {label}")

    label_critique = threat_label(22)
    print(f"Menace après horde : {label_critique}")

    spawned = total_spawned(5)
    print(f"Infectés apparus cette nuit : {spawned}")

    placard = {"eau": 4, "conserve": 1, "bandage": 0}
    eau = supply_status(placard, "eau")
    bandage = supply_status(placard, "bandage")
    print(f"Stock eau : {eau}")
    print(f"Stock bandages : {bandage}")

    degats = barricade_damage(10, 3, 5)
    print(f"Dégâts à la barricade : {degats}")

    print("\n✅ La nuit est passée — la barricade tient encore.")


if __name__ == "__main__":
    main()
