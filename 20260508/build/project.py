# ============================================================
# The Last of Us — Couloir sans issue (build)
# ============================================================
# Implémente les 5 fonctions ci-dessous pour que main.py fonctionne.
# Lance : python3 main.py
# Implémente-les dans l'ordre — commence par TODO 1.
# ============================================================

import random


# ------------------------------------------------------------
# TODO 1 — Munitions après rafale et petit ramassage
# ------------------------------------------------------------
# Joel vide son chargeur sur une vague puis récupère quelques balles au sol avant
# de reculer. Tu calcules ce qui reste à chamber : tu tires d'abord, puis tu ajoutes
# les balles ramassées. Si le total descend sous zéro après la rafale, tu restes à
# zéro — pas de munitions négatives.
#
#   current      : balles déjà au chargeur avant la scène (int)
#   fired        : balles dépensées pendant la rafale (int)
#   loot_rounds  : balles ramassées au sol après le tir (int)
#
# ammo_after_exchange(30, 12, 5)   =>   23   (30 - 12 + 5)
#
# ammo_after_exchange(8, 15, 0)   =>   0   (plancher : pas assez pour la rafale)
#
# Indice : une expression avec + et -, puis max(0, ...) pour borner le résultat
# ------------------------------------------------------------
def ammo_after_exchange(current, fired, loot_rounds):
    calcul = current - fired + loot_rounds
    return max(0, calcul)

    


# ------------------------------------------------------------
# TODO 2 — État du survivant selon la jauge de vie
# ------------------------------------------------------------
# La vie va de 0 à 100. Tu renvoies une courte étiquette pour savoir si Joel peut
# encore sprinter ou s'il doit se coller au mur. Utilise des seuils stricts :
# au-dessus de 70 c'est encore tenable, au-dessus de 25 mais pas au-delà de 70 c'est
# sérieux, sinon c'est critique.
#
#   hp   : points de vie actuels (0 à 100)
#
# survivor_condition(85)   =>   "OK"
#
# survivor_condition(44)   =>   "Blessé"
#
# survivor_condition(12)   =>   "Critique"
#
# Indice : if / elif / else avec des comparaisons sur hp
# ------------------------------------------------------------
def survivor_condition(hp):
    if hp > 70:
        return "OK"       
    elif hp <= 70 and hp >= 25:
        return "Blessé"
    elif hp < 25:
        return "Critique"




# ------------------------------------------------------------
# TODO 3 — Additionner les dégâts infligés à la meute
# ------------------------------------------------------------
# Chaque infecté encaisse un nombre entier de dégâts ; tu veux le total pour savoir
# si la salve a suffi. Parcourt la liste avec une boucle et cumule dans une variable
# qui part de zéro.
#
#   hits   : liste de dégâts entiers (peut être vide)
#
# total_shots_land([6, 14, 5, 11])   =>   36
#
# total_shots_land([])   =>   0
#
# Indice : for x in hits puis +=
# ------------------------------------------------------------
def total_shots_land(hits):
    total_shots_land = 0
    for shot in hits:
        total_shots_land += shot
    return total_shots_land


# ------------------------------------------------------------
# TODO 4 — Fusionner deux chargeurs partiels
# ------------------------------------------------------------
# Ellie combine mentalement deux chargeurs pour savoir combien de balles elle peut
# encore faire partir avant de devoir fouiller un cadavre. Addition simple.
#
#   mag_a   : balles dans le premier chargeur (int)
#   mag_b   : balles dans le second chargeur (int)
#
# combine_magazines(9, 6)   =>   15
#
# combine_magazines(0, 4)   =>   4
#
# Indice : return avec +
# ------------------------------------------------------------
def combine_magazines(mag_a, mag_b):
    mag = mag_a + mag_b
    return mag
    


# ------------------------------------------------------------
# TODO 5 — Qui ouvre la porte en premier
# ------------------------------------------------------------
# Le couloir est étroit : un seul nom passe devant. Tu tires au sort entre les deux
# prénoms passés en arguments. random est déjà importé en haut du fichier ; main.py
# fixe la graine juste avant l'appel pour que le résultat soit toujours le même chez
# toi quand tu lances le programme.
#
#   person_a   : premier prénom (str)
#   person_b   : second prénom (str)
#
# who_opens_door("Joel", "Ellie")   =>   "Ellie"   (avec random.seed(7) déjà fait dans main)
#
# Indice : random.choice avec une liste des deux prénoms
# ------------------------------------------------------------
def who_opens_door(person_a, person_b):
    person = [person_a, person_b]
    return random.choice(person)