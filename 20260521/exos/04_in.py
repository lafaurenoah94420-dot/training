# ============================================================
# The Last of Us — équipement de Joel
# ============================================================
# Joel fouille son sac. Le jeu doit savoir s'il a déjà une arbalète
# dans l'inventaire pour afficher le bon tutoriel.
#
# Lance : python3 04_in.py
# ============================================================

inventaire = ["lampe", "kit", "bouteille", "arbalète", "couteau"]
objet_cherche = "arbalète"
a_l_objet = False

# Vérifie si objet_cherche est présent dans inventaire.
# Stocke True ou False dans a_l_objet.
#
# "arbalète" est dans la liste  →  a_l_objet = True
# si objet_cherche valait "fusil"  →  a_l_objet = False
#
# Résultat attendu : a_l_objet == True
#
# Indice : mot-clé in

# À toi :
if objet_cherche in inventaire:
    a_l_objet = True

# --- Vérification (ne pas modifier) ---
assert a_l_objet is True, f"Obtenu : {a_l_objet}, attendu : True"
print("✅ Correct !")
