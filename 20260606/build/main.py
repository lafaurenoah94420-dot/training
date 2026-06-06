# ============================================================
# The Last of Us — Décodage radio
# ============================================================
# Joel intercepte des messages codés, lit les munitions du plan
# de ravitaillement, note les jours de marche et décide si le
# groupe peut partir vers le prochain relais.
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
    decode_radio_code,
    ammo_remaining,
    log_march_days,
    read_stash_ammo,
    departure_ok,
)


def main():
    print("=== The Last of Us — Décodage radio ===\n")

    message_brut = "XP_RELAIS_NORD"
    message_clair = decode_radio_code(message_brut)
    print(f"Message décodé : {message_clair}")

    balles = ammo_remaining(30, 12)
    print(f"Munitions après 12 tirs (sur 30) : {balles}")

    balles_epuisees = ammo_remaining(5, 20)
    print(f"Munitions après 20 tirs (sur 5) : {balles_epuisees}")

    jours = log_march_days(1, 5)
    print(f"Jours notés dans le carnet : {jours}")

    plan = {"fusil": 24, "pistolet": 12, "arc": 8}
    stock_fusil = read_stash_ammo(plan, "fusil")
    print(f"Munitions fusil dans le plan : {stock_fusil}")

    peut_partir = departure_ok(stock_fusil, 15)
    print(f"Assez de munitions pour partir (15 min) ? {peut_partir}")

    trop_peu = departure_ok(8, 15)
    print(f"Avec 8 balles, seuil 15 — peut partir ? {trop_peu}")

    print("\n✅ Joel sait lire la radio et quand bouger — cap sur le relais.")


if __name__ == "__main__":
    main()
