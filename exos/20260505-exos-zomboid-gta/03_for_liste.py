# ============================================================
# GTA — bilan de missions
# ============================================================
# Franklin vient de finir sa session. À chaque mission il a obtenu
# un nombre d'étoiles. Le jeu doit calculer son total pour afficher
# son classement en fin de journée.
#
# Lance : python 03_for_liste.py
# ============================================================

niveaux = [2, 1, 4, 1, 3]
etoiles_total = 0

# Parcours la liste niveaux et additionne chaque valeur dans etoiles_total.
#
# tour 1 : x = 2  →  etoiles_total = 0 + 2 = 2
# tour 2 : x = 1  →  etoiles_total = 2 + 1 = 3
# tour 3 : x = 4  →  etoiles_total = 3 + 4 = 7
# tour 4 : x = 1  →  etoiles_total = 7 + 1 = 8
# tour 5 : x = 3  →  etoiles_total = 8 + 3 = 11
#
# Résultat attendu : etoiles_total == 11
#
# Indice : boucle for + +=

for x in niveaux:
    etoiles_total += x


# --- Vérification (ne pas modifier) ---
assert etoiles_total == 11, (
    f"Obtenu : {etoiles_total}, attendu : 11 (somme de 2+1+4+1+3)."
)
print("✅ Correct !")
