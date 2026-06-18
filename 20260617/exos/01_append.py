# ============================================================
# Project Zomboid — inventaire de survie
# ============================================================
# Tu fouilles une maison. Chaque objet trouvé s'ajoute à la liste
# inventaire avec append().
#
# Lance : python3 01_append.py
# ============================================================

inventaire = ["batte"]

# Ajoute ces 3 objets un par un avec append() :
#   "eau"
#   "conserve"
#   "bandage"
#
# inventaire commence : ["batte"]
# après "eau"       : ["batte", "eau"]
# après "conserve"  : ["batte", "eau", "conserve"]
# après "bandage"   : ["batte", "eau", "conserve", "bandage"]
#
# Résultat attendu : len(inventaire) == 4
#
# Indice : inventaire.append("...")

# À toi :
inventaire.append("eau")
inventaire.append("conserve")
inventaire.append("bandage")

# --- Vérification (ne pas modifier) ---
assert len(inventaire) == 4, f"Obtenu : {len(inventaire)} objets, attendu : 4"
assert inventaire[-1] == "bandage", f"Dernier objet : '{inventaire[-1]}', attendu : 'bandage'"
print("✅ Correct !")
