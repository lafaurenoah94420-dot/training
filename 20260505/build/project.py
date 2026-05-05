# ============================================================
# Project Zomboid — jauge de faim (build)
# ============================================================
# Implémente les 3 fonctions ci-dessous pour que main.py fonctionne.
# Lance : python main.py
# Implémente-les dans l'ordre — commence par TODO 1.
# ============================================================


# ------------------------------------------------------------
# TODO 1 — Manger fait baisser la faim
# ------------------------------------------------------------
# Après un repas, la jauge de faim de Chris baisse.
# Si la nourriture est plus calorique que ce qu'il lui reste de faim,
# la jauge tombe à 0 — elle ne peut jamais être négative.
#
#   current_hunger  : la faim actuelle (un nombre entre 0 et 100)
#   food_value      : les points de faim que la nourriture enlève
#
# eat_reduce_hunger(60, 25)  =>  35
# eat_reduce_hunger(10, 40)  =>  0   (pas -30)
#
# Indice : max(0, ...)
# ------------------------------------------------------------
def eat_reduce_hunger(current_hunger, food_value):
    current_hunger -= food_value
    return max(0, current_hunger)


# ------------------------------------------------------------
# TODO 2 — Le temps qui passe fait monter la faim
# ------------------------------------------------------------
# Plus Chris attend, plus il a faim. Chaque heure, la jauge monte
# d'un certain nombre de points. Elle ne peut pas dépasser 100 —
# au-delà, il s'effondre de faim de toute façon.
#
#   current_hunger  : la faim actuelle (un nombre entre 0 et 100)
#   rise_per_hour   : de combien la faim monte par heure
#   hours           : combien d'heures se sont écoulées
#
# hunger_from_time_passing(10, 5, 4)   =>  30   (10 + 5 * 4)
# hunger_from_time_passing(90, 5, 4)   =>  100  (pas 110)
#
# Indice : min(100, ...)
# ------------------------------------------------------------
def hunger_from_time_passing(current_hunger, rise_per_hour, hours):
    current_hunger += rise_per_hour * hours
    return min(100, current_hunger)


# ------------------------------------------------------------
# TODO 3 — Message selon le niveau de faim
# ------------------------------------------------------------
# L'interface du jeu affiche un message d'alerte selon la jauge.
# Trois niveaux : critique, modéré, ou tranquille.
# Le texte doit être identique caractère pour caractère — main.py compare
# exactement ce que tu retournes.
#
#   hunger  : la faim actuelle (un nombre entre 0 et 100)
#
# hunger_status_message(90)  =>  "Critique : trouve à manger maintenant."
# hunger_status_message(55)  =>  "Faim modérée : pense à grignoter."
# hunger_status_message(20)  =>  "Tranquille pour l'instant."
#
# Indice : if / elif / else + return
# ------------------------------------------------------------
def hunger_status_message(hunger):
    if hunger >= 80:
        return "Critique : trouve à manger maintenant."
    elif hunger >= 40:
        return "Faim modérée : pense à grignoter."
    else:
        return "Tranquille pour l'instant."
