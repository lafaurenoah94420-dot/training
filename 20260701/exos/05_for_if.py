# ============================================================
# Hearts of Iron IV — divisions blindées
# ============================================================
# Le général compte combien de divisions ont un niveau d'armure
# supérieur ou égal à 5. Seules celles-là peuvent mener l'assaut.
#
# Lance : python3 05_for_if.py
# ============================================================

armures = [3, 7, 5, 2, 8, 4]
nb_elites = 0

# Parcours la liste armures. À chaque tour, si la valeur est >= 5,
# ajoute 1 à nb_elites.
#
# tour 1 : a = 3  →  3 >= 5 ? non  →  nb_elites reste 0
# tour 2 : a = 7  →  7 >= 5 ? oui  →  nb_elites = 1
# tour 3 : a = 5  →  5 >= 5 ? oui  →  nb_elites = 2
# tour 4 : a = 2  →  2 >= 5 ? non  →  nb_elites reste 2
# tour 5 : a = 8  →  8 >= 5 ? oui  →  nb_elites = 3
# tour 6 : a = 4  →  4 >= 5 ? non  →  nb_elites reste 3
#
# Résultat attendu : nb_elites == 3
#
# Indice : for + if + +=

# À toi :
for i in armures:
    if i >= 5:
        nb_elites += 1

# --- Vérification (ne pas modifier) ---
assert nb_elites == 3, f"Obtenu : {nb_elites}, attendu : 3"
print("✅ Correct !")
