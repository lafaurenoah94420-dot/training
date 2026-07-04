# ============================================================
# Le procès de Nahla
# ============================================================
# Accusation du jour : Nahla a dormi 19h et refusé de bouger.
# Verdict : coupable.
# ============================================================
accusation = int(input("Combien de temps Nahla a dormis ? "))

autre_accusation = "oui"

while autre_accusation == "oui":
    if accusation <= 0:
        print("Nahla n'a pas dormis, elle est libre")
    elif accusation > 0 and accusation <= 6:
        print("Nahla n'a pas beaucoup dormis, elle est libre")
    elif accusation > 6 and accusation <= 12:
        print("Nahla a trop dormis, sentence : Nahla dormiras sur le sol la prochaine fois")
    elif accusation > 12 and accusation <= 16:
        print("Nahla a beaucoup trop dormis, sentence : Nahla n'auras pas le droit de dormir avant 6 heures")
    else:
        print("Nahla a VRAIMENT BEAUCOUP TROP DORMIS, sentece : Nahla est expulsé de la maison pendant un jour")
    autre_accusation = input("Une autre accusation ? ")
    if autre_accusation == "oui":
        accusation = int(input("Combien de temps Nahla a dormis ? "))