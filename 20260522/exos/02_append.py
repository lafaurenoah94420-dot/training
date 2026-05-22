# ============================================================
# Project Zomboid — sac à dos de loot
# ============================================================
# Tu fouilles une maison. Chaque objet trouvé est ajouté à la liste
# du sac. Trois objets sont déjà notés — ajoute les deux nouveaux.
#
# Lance : python3 02_append.py
# ============================================================

sac = ["batte", "eau en bouteille"]

# Ajoute "cle de voiture" puis "bandage" à la fin de sac avec .append()
#
# départ : ["batte", "eau en bouteille"]
# après 1er append : ["batte", "eau en bouteille", "cle de voiture"]
# après 2e append  : ["batte", "eau en bouteille", "cle de voiture", "bandage"]
#
# Résultat attendu : len(sac) == 4  et  sac[-1] == "bandage"
#
# Indice : .append() deux fois

# À toi :
sac.append("cle de voiture")
sac.append("bandage")

# --- Vérification (ne pas modifier) ---
assert len(sac) == 4, f"Le sac doit avoir 4 objets, obtenu : {len(sac)}"
assert sac[-1] == "bandage", f"Dernier objet attendu : bandage, obtenu : {sac[-1]}"
print("✅ Correct !")
