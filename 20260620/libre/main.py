# ============================================================
# Nahla — Inventaire des croquettes
# ============================================================
# Objet à ajouter : friandise
# Après vol : ['croquettes', 'patee', 'friandise']
# Croquettes dans le placard : 1
# Placard Nahla : 3 objets
# ============================================================
placard = ["croquettes", "patée"]

objet_volé = input()
ajout_objet_volé = placard.append(objet_volé)

message = f"Nahla a volée des {objet_volé} donc après le vol, il y a {placard} dans le placard"

print(message)

