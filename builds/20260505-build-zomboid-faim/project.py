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
# Ce que ça fait : après avoir mangé, la jauge de faim baisse. Elle ne peut
# pas descendre en dessous de 0.
#
# Exemple :
#   Entrée  : current_hunger = 60, food_value = 25
#   Sortie  : 35
#
# Indice : soustraire food_value à current_hunger ; si le résultat serait
#          négatif, utilise 0 à la place (if ou max(...)).
# ------------------------------------------------------------
def eat_reduce_hunger(current_hunger, food_value):
    current_hunger -= food_value
    return max(0, current_hunger)


# ------------------------------------------------------------
# TODO 2 — Le temps qui passe fait monter la faim
# ------------------------------------------------------------
# Ce que ça fait : chaque heure, la faim augmente d'un certain nombre de
# points. La jauge ne peut pas dépasser 100.
#
# Exemple :
#   Entrée  : current_hunger = 10, rise_per_hour = 5, hours = 4
#   Sortie  : 30   (10 + 5 * 4)
#
# Indice : calcule d'abord current_hunger + rise_per_hour * hours, puis
#          borne le résultat pour qu'il ne dépasse jamais 100 (if ou min(...)).
# ------------------------------------------------------------
def hunger_from_time_passing(current_hunger, rise_per_hour, hours):
    current_hunger += rise_per_hour * hours
    return min(100, current_hunger)


# ------------------------------------------------------------
# TODO 3 — Message selon le niveau de faim
# ------------------------------------------------------------
# Ce que ça fait : renvoie une phrase en français selon la valeur de hunger.
#   - si hunger >= 80  → "Critique : trouve à manger maintenant."
#   - sinon si hunger >= 40 → "Faim modérée : pense à grignoter."
#   - sinon → "Tranquille pour l'instant."
#
# Exemple :
#   Entrée  : hunger = 90
#   Sortie  : "Critique : trouve à manger maintenant." (respecte les guillemets
#             et la ponctuation EXACTEMENT comme ci-dessus)
#
# Indice : enchaîne if / elif / else et renvoie la chaîne avec return.
# ------------------------------------------------------------
def hunger_status_message(hunger):
    if hunger >= 80:
        return "Critique : trouve à manger maintenant."
    elif hunger >= 40:
        return "Faim modérée : pense à grignoter."
    else:
        return "Tranquille pour l'instant."