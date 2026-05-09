# ============================================================
# Hearts of Iron IV — Quartier sous tension
# ============================================================
# Programme texte : litres « en vrac » après remplissage de jerricans, ordre présent
# dans une pile de télégrammes, production cumulée sur plusieurs jours, dénombrement
# de rapports au-dessus d'un seuil, manivelle jusqu'à tension minimale.
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
    spare_litres,
    order_tag_present,
    gear_over_days,
    fronts_above_threshold,
    crank_until_live,
)


def main():
    print("=== Hearts of Iron IV — Quartier sous tension ===\n")

    vrac = spare_litres(47, 15)
    print(f"Litres impossibles à caser dans les jerricans de 15 L : {vrac}")

    pile = ["ATTACK", "HOLD", "PUSH"]
    ok = order_tag_present("HOLD", pile)
    print(f"L'ordre HOLD est bien dans la pile : {ok}")

    cumul = gear_over_days(14, 5)
    print(f"Production cumulée sur 5 jours (14 unités / jour) : {cumul}")

    niveaux = [22, 65, 38, 71, 40]
    alertes = fronts_above_threshold(niveaux, 40)
    print(f"Rapports strictement au-dessus du seuil 40 : {alertes}")

    volts = crank_until_live(9, 18, 60)
    print(f"Tension après cranking jusqu'au plancher : {volts}")

    print("\n✅ Quartier stabilisé — réserve et radios alignées.")


if __name__ == "__main__":
    main()
