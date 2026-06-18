# ============================================================
# Malik — Soirée à la maison
# ============================================================
# A couru nu dans le salon ? oui
# A crié à 3h du mat ? oui
# A cassé quelque chose ? non
# A dit une phrase incompréhensible ? oui
#
# Score : 3/4
# Niveau : Appelle les secours
# ============================================================
a_couru_nu_dans_le_salon = input("Est ce que le fou a couru nu (???) dans le salon ? ")
a_crié_à_3h_du_mat = input("Est ce que le cinglé a crié à 3h du matin ? ")
a_cassé_quelque_chose = input("Est ce que le malade a cassé quelque chose ? ")
a_dit_une_phrase_incompréhensible = input("Est ce que le psychopate a dit une phrase incompréhensible ? ")

score = 0

if a_couru_nu_dans_le_salon == "oui":
    score += 1

if a_crié_à_3h_du_mat == "oui":
    score += 1

if a_cassé_quelque_chose == "oui":
    score += 1

if a_dit_une_phrase_incompréhensible == "oui":
    score += 1



if score == 0:
    print("Malik est appaisé")
elif score == 1:
    print("Malik est un peu énergique")
elif score == 2:
    print("Malik est devenu fou (ce qui est normal)")
elif score == 3:
    print("Attention ! Malik est devenu complètement malade")
elif score == 4:
    print("MALIK A PÉTÉ UN CABLE ! APPELÉ LES SECOURS")