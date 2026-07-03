# ============================================================
# Nahla — Carte d'identité officielle
# ============================================================
# Nom complet : nahla la duchesse
# → CARTE : [NAHLA LA DUCHESSE] — Statut : REINE DU CANAPÉ
# Surnom secret : grosse pouffe → censuré en ***
# ============================================================
guichet_ouvert = "oui"

while guichet_ouvert == "oui":
    nouveau_titre = input("Que sera le nouveau nom ? ")
    titre_maj = nouveau_titre.upper()
    statut_maj = nouveau_statut = input("Que sera le nouveau statut de Nahla ? ")
    nouveau_statut.upper()
    print(f"Carte : {titre_maj} — Statut : {statut_maj}")
    guichet_ouvert = input("Doit on faire une carte ? ")
