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

# Additionne tous les éléments de niveaux dans etoiles_total
#
# for x in [2, 1, 4, 1, 3]  =>  etoiles_total == 11
#
# Indice : boucle for + +=

for x in niveaux:
    etoiles_total += x


# --- Vérification (ne pas modifier) ---
assert etoiles_total == 11, (
    f"Obtenu : {etoiles_total}, attendu : 11 (somme de 2+1+4+1+3)."
)
print("✅ Correct !")
