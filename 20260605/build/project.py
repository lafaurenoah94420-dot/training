# ============================================================
# Resident Evil — Inventaire d'herbes (build)
# ============================================================
# Implémente les 5 fonctions ci-dessous pour que main.py fonctionne.
# Lance : python3 main.py
# Implémente-les dans l'ordre — commence par TODO 1.
# ============================================================


# ------------------------------------------------------------
# TODO 1 — Libellé d'une herbe pour l'écran
# ------------------------------------------------------------
# L'inventaire affiche une ligne par type d'herbe avec la quantité.
# Construis le texte exact.
#
#   herb_name   : nom de l'herbe (str)
#   quantity    : quantité (int)
#
# format_herb_label("Herbe verte", 3)   =>   "Herbe verte : 3"
#
# format_herb_label("Spray", 1)   =>   "Spray : 1"
#
# Indice : f-string
# ------------------------------------------------------------
def format_herb_label(herb_name, quantity):
    return f"{herb_name} : {quantity}"


# ------------------------------------------------------------
# TODO 2 — Ajouter une herbe au sac
# ------------------------------------------------------------
# Leon ramasse une herbe. Ajoute herb_name à la fin de la liste
# inventory (la liste est modifiée sur place).
#
#   inventory   : liste des herbes (list)
#   herb_name   : nom à ajouter (str)
#
# sac = ["Herbe rouge"]  puis  add_herb(sac, "Spray")
#   =>  sac vaut ["Herbe rouge", "Spray"]
#
# Indice : .append()
# ------------------------------------------------------------
def add_herb(inventory, herb_name):
    return inventory.append(herb_name)


# ------------------------------------------------------------
# TODO 3 — Leon possède-t-il cette herbe ?
# ------------------------------------------------------------
# Vérifie si herb_name est présent dans inventory. Renvoie True ou False.
#
#   inventory   : liste des herbes (list)
#   herb_name   : nom cherché (str)
#
# has_herb(["Herbe verte", "Spray"], "Spray")   =>   True
#
# has_herb(["Herbe rouge"], "Herbe verte")   =>   False
#
# Indice : return herb_name in inventory
# ------------------------------------------------------------
def has_herb(inventory, herb_name):
    if herb_name in inventory:
        return True
    else:
        return False


# ------------------------------------------------------------
# TODO 4 — Compter un type d'herbe
# ------------------------------------------------------------
# Compte combien de fois herb_name apparaît dans inventory.
#
#   inventory   : liste des herbes (list)
#   herb_name   : nom à compter (str)
#
# count_herb_type(["Herbe verte", "Herbe rouge", "Herbe verte"], "Herbe verte")
#   =>   2
#
# count_herb_type(["Spray"], "Herbe verte")   =>   0
#
# Indice : for ... in inventory  +  if ... ==  +  compteur +=
# ------------------------------------------------------------
def count_herb_type(inventory, herb_name):
    count = 0
    for p in inventory:
        if p == herb_name:
            count += 1
    return count


# ------------------------------------------------------------
# TODO 5 — Message d'état selon les PV
# ------------------------------------------------------------
# L'écran affiche l'état de Leon selon ses points de vie.
#
#   hp   : points de vie actuels (int)
#
# hp <= 20        =>  "Critique"
# 21 <= hp <= 50  =>  "Blessé"
# hp > 50         =>  "Stable"
#
# health_status(35)   =>   "Blessé"
# health_status(80)   =>   "Stable"
# health_status(10)   =>   "Critique"
#
# Indice : if / elif / else
# ------------------------------------------------------------
def health_status(hp):
    etat = ""
    if hp <= 20:
        etat = "Critique"
    elif hp >= 21 and hp <= 50:
        etat = "Blessé"
    else:
        etat = "Stable"
    return etat