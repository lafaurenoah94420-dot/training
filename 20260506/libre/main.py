# ============================================================
# Nahla — Audit croquettes / paresse
# ============================================================
# Exemple d'exécution attendu (à reproduire avec ton code) :
#
# Sacs ouverts cette semaine ? 3
# Flemme (0-10) ? 9
# Bilan : investissement humain inutile. Nahla n'a pas bougé mais exige des excuses écrites pour le bruit du sac.
# ============================================================

sacs = int(input("Combien de sac a été ouvert ? "))

qualite_croquette = (input("De quelle qualité sont les croquettes ? : ")) # bon ou mauvais

flemme = int(input("Niveau de flemme ? "))

bilan_sacs = f"nombre de sacs ouverts : {sacs}"

bilan_flemme = f"Niveau de flemme : {flemme}"

print(bilan_sacs)

if qualite_croquette == "bon":
    print("Les croquettes sont bonnes.")
elif qualite_croquette == "mauvais":
    print("Les croquettes sont dégeux.")
else:
    print("Réponds par bon ou mauvais")

print(bilan_flemme)