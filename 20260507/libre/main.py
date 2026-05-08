# ============================================================
# Nahla — Procès du rayon croquettes
# ============================================================
# Exemple d'exécution attendu (à reproduire avec ton code) :
#
# Crime ? il a respiré trop fort près du sac
# Peine : interdiction de bouger les sourcils pendant 24 h.
# Mépris : 11/10 (dépasse l'échelle, comme d'habitude).
# Verdict : Nahla accepte les excuses uniquement si elles sont écrites en croquettes.
# ============================================================

croquettes = int(input("Combien de croquettes elle a mangé ?"))

crime_impardonable = "Nahla a mangé trop de croquettes" #plus de 40
crime_pardonable = "Nahla n'a pas mangé beaucoup de croquettes"
peine_coupable = "Sentence : Ne doit pas grossir pendant 24h" #si plus de 40
peine_non_coupable = "Nahla est pardonné"

if croquettes > 40:
    print(crime_impardonable)
    print(peine_coupable)
elif croquettes <= 40:
    print(crime_pardonable)
    print(peine_non_coupable)
