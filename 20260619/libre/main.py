# ============================================================
# Nahla — Avocat de la défense
# ============================================================
# Accusation : Nahla a dormi sur le canapé interdit.
# Plaidoirie : Votre Honneur, le canapé était froid. Nahla l'a réchauffé. C'est un service rendu à la famille.
# Verdict : Coupable. Amende : 3 sachets de friandises.
# ============================================================
def tribunal_de_Nahla():
    verdict_non_coupable = "Nahla est aquité des ses crimes"
    verdict_coupable = "Nahla aura une peine d'un an sans paté"
    verdict_EXTREMEMENT_coupable = "Pour ses crimes odieux et inhumain (meme si c'est un chat), Nahla n'aura plus le droit à du paté pour le restant des ses jours !"

    continuer_le_tribual = "oui"
    while continuer_le_tribual == "oui":
        accusation_un = input("Nahla a t'elle mangé des croquettes sans autorisation ? ")
        accusation_deux = input("Nahla a t'elle oser m'ignorer comme une racaille ? ")

        if accusation_un == "oui" and accusation_deux == "oui":
            print(verdict_EXTREMEMENT_coupable)
        elif accusation_un == "oui" and accusation_deux == "non" or accusation_un == "non" and accusation_deux == "oui":
            print(verdict_coupable)
        elif accusation_un == "non" and accusation_deux == "non":
            print(verdict_non_coupable)
        continuer_le_tribual = input("Devons nous continuer le tribunal ? ")
        
tribunal_de_Nahla()
