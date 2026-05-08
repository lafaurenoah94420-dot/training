# ============================================================
# Project Zomboid — sac de loot sans merci
# ============================================================
# Programme texte : longueur de code produit, consommation dans un inventaire
# dict, tirage de bruit radio, indicatif en majuscules, stamina bornée à 0.
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
    sku_length,
    consume_cans,
    noise_roll,
    shout_callsign,
    safe_stamina,
)


def main():
    print("=== Project Zomboid — sac de loot sans merci ===\n")

    code = "Z-9C12"
    print(f"Longueur du code boîte '{code}' : {sku_length(code)}")

    placard = {"conserves": 12, "eau": 4}
    consume_cans(placard, 5)
    print(f"Après 5 conserves bouffées : reste {placard['conserves']} boîtes.")

    bruit = noise_roll()
    print(f"Grésillement radio (niveau 1-10) : {bruit}")

    cri = shout_callsign("grenier")
    print(f"Indicatif hurlé : {cri}")

    stamina = safe_stamina(25, 10)
    stamina_bas = safe_stamina(8, 10)
    print(f"Stamina après effort modéré : {stamina}")
    print(f"Stamina après effort brutal (plancher 0) : {stamina_bas}")

    print("\n✅ Sac vidé — tout roule.")


if __name__ == "__main__":
    main()
