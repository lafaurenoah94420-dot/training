# ============================================================
# Nahla — Cachettes secrètes
# ============================================================
# Nahla a planqué des croquettes dans la maison. Tu enregistres
# chaque pièce et la quantité, tu calcules le total, puis Nahla
# juge si l'humain mérite un mot ou du mépris.
#
# Exemple d'exécution :
#   Nom de la pièce : salon
#   Nombre de croquettes : 40
#   Encore une pièce ? (o/n) : o
#   Nom de la pièce : cuisine
#   Nombre de croquettes : 25
#   Encore une pièce ? (o/n) : n
#   Total caché : 65 croquettes
#   Nahla dit : "J'ai 65 croquettes. Toi t'as rien. Parle pas."
# ============================================================

lieu = input("Où ca se passe ?")

arrogance_de_nahla = "J'ai encore des croquettes, c'est moi la boss"

stock = int(input("Combien de croquettes ? "))

def nahla_est_grosse(lieu, stock):
    print(f"Nahla mange ses croquettes dans {lieu}")
    while stock > 0:
        print(arrogance_de_nahla)
        stock -= 15
    else:
        print("Ah je suis foutue")

nahla_est_grosse(lieu, stock)
