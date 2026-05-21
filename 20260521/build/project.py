# ============================================================
# Project Zomboid — Barricader les fenêtres (build)
# ============================================================
# Implémente les 5 fonctions ci-dessous pour que main.py fonctionne.
# Lance : python3 main.py
# Implémente-les dans l'ordre — commence par TODO 1.
# ============================================================


# ------------------------------------------------------------
# TODO 1 — Planches après une fenêtre
# ------------------------------------------------------------
# Tu poses des planches sur une fenêtre. Le stock diminue du coût de la
# barricade. Le stock ne peut pas devenir négatif.
#
#   planks   : planches disponibles avant (int)
#   cost     : planches consommées pour une fenêtre (int)
#
# planks_after_window(12, 3)   =>   9
#
# planks_after_window(2, 5)   =>   0
#
# Indice : max(0, planks - cost)
# ------------------------------------------------------------
def planks_after_window(planks, cost):
    restant = max(0, planks - cost)
    return restant


# ------------------------------------------------------------
# TODO 2 — Message selon le stock
# ------------------------------------------------------------
# L'écran de craft affiche un avertissement selon les planches restantes.
# Utilise ces seuils dans cet ordre :
#   planks <= 0   →  "Rupture"
#   planks < 5    →  "Stock faible"
#   sinon         →  "Stock OK"
#
#   planks   : planches restantes (int)
#
# stock_message(0)   =>   "Rupture"
#
# stock_message(3)   =>   "Stock faible"
#
# stock_message(10)   =>   "Stock OK"
#
# Indice : if / elif / else
# ------------------------------------------------------------
def stock_message(planks):
    if planks <= 0:
        return "Rupture"
    elif planks < 5:
        return "Stock faible"
    else:
        return "Stock OK"


# ------------------------------------------------------------
# TODO 3 — Barricader toutes les fenêtres
# ------------------------------------------------------------
# La maison a plusieurs fenêtres. Chaque fenêtre coûte le même nombre de
# planches. Répète l'opération num_windows fois et renvoie le stock final
# (jamais négatif à la fin).
#
#   planks        : stock de départ (int)
#   num_windows   : nombre de fenêtres à barricader (int)
#   cost_each     : planches par fenêtre (int)
#
# barricade_all_windows(20, 4, 3)   =>   8
#
# barricade_all_windows(5, 3, 2)   =>   0
#
# Indice : for range(num_windows) et -= sur une variable locale
# ------------------------------------------------------------
def barricade_all_windows(planks, num_windows, cost_each):
    for i in range(num_windows):
        planks -= cost_each
    return planks


# ------------------------------------------------------------
# TODO 4 — Outil dans le sac
# ------------------------------------------------------------
# Avant de barricader, le jeu vérifie si tu as le bon outil dans ton inventaire.
#
#   inventory   : liste de noms d'objets (list de str)
#   tool_name   : outil recherché (str)
#
# has_tool(["marteau", "clous", "scie"], "marteau")   =>   True
#
# has_tool(["clous", "bandages"], "scie")   =>   False
#
# Indice : mot-clé in
# ------------------------------------------------------------
def has_tool(inventory, tool_name):
    if tool_name in inventory:
        return True
    else:
        return False


# ------------------------------------------------------------
# TODO 5 — Nuits jusqu'au calme
# ------------------------------------------------------------
# Une horde gratte aux volets. Chaque nuit le bruit baisse d'un certain nombre.
# Compte combien de nuits sont nécessaires avant que le bruit tombe à 0 ou moins.
# Tant que noise > 0 : enlève drop_per_night et ajoute 1 au compteur.
#
#   noise            : niveau de bruit au début (int)
#   drop_per_night   : baisse par nuit (int)
#
# nights_until_quiet(10, 3)   =>   4
#
# nights_until_quiet(4, 2)   =>   2
#
# Indice : while + -= et compteur +=
# ------------------------------------------------------------
def nights_until_quiet(noise, drop_per_night):
    units = 0
    while noise > 0:
        units += 1
        noise -= drop_per_night
    return units
