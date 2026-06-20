# ============================================================
# Resident Evil — Armoire du RPD
# ============================================================
# Implémente les 5 fonctions ci-dessous pour que main.py fonctionne.
# Lance : python3 main.py
# Implémente-les dans l'ordre — commence par TODO 1.
# ============================================================


# ------------------------------------------------------------
# TODO 1 — Compter les objets dans l'armoire
# ------------------------------------------------------------
# Leon ouvre l'armoire du RPD et veut savoir combien de compartiments
# sont déjà occupés avant d'y ranger quoi que ce soit.
#
#   locker   : liste des objets déjà présents (list de str)
#
# locker_slots(["spray", "herbe_verte", "munitions"])   =>   3
#
# locker_slots(["munitions"])   =>   1
#
# Indice : len()
# ------------------------------------------------------------
def locker_slots(locker):
    return len(locker)


# ------------------------------------------------------------
# TODO 2 — Ranger un objet trouvé
# ------------------------------------------------------------
# Leon ramasse un objet dans le commissariat et le glisse dans
# l'armoire. La liste est modifiée sur place ; tu la renvoies à la fin.
#
#   locker   : liste actuelle des objets (list de str)
#   item     : nom de l'objet à ajouter (str)
#
# stash_item(["spray", "munitions"], "herbe_bleue")
#   =>   ["spray", "munitions", "herbe_bleue"]
#
# stash_item([], "spray")   =>   ["spray"]
#
# Indice : append()
# ------------------------------------------------------------
def stash_item(locker, item):
    locker.append(item)
    return locker


# ------------------------------------------------------------
# TODO 3 — Dénombrer une herbe précise
# ------------------------------------------------------------
# Pour savoir s'il peut combiner des herbes, Leon doit compter
# combien de fois un type précis apparaît dans l'armoire.
#
#   locker     : liste des objets (list de str)
#   herb_name  : nom de l'herbe à chercher (str)
#
# count_herbs(["herbe_verte", "spray", "herbe_verte"], "herbe_verte")
#   =>   2
#
# count_herbs(["spray", "munitions"], "herbe_verte")   =>   0
#
# Indice : for + if + compteur avec +=
# ------------------------------------------------------------
def count_herbs(locker, herb_name):
    compteur = 0
    for i in locker:
        if i == herb_name:
            compteur += 1
    return compteur


# ------------------------------------------------------------
# TODO 4 — Additionner les points de soin
# ------------------------------------------------------------
# Sur la table de craft, chaque herbe trouvée a une valeur de soin.
# Leon additionne toutes les valeurs pour savoir combien de PV il
# peut récupérer au total.
#
#   healing_values   : liste de points de soin (list d'int)
#
# total_heal_power([25, 50, 25])   =>   100
#
# total_heal_power([80])   =>   80
#
# Indice : for + total += valeur
# ------------------------------------------------------------
def total_heal_power(healing_values):
    total = 0
    for i in healing_values:
        total += i
    return total 



# ------------------------------------------------------------
# TODO 5 — Résumé de l'armoire
# ------------------------------------------------------------
# Avant de quitter la salle des étoiles, Leon affiche une ligne
# récapitulative avec le nombre total d'objets rangés.
#
#   locker   : liste des objets (list de str)
#
# locker_status(["spray", "herbe_verte", "munitions", "herbe_bleue"])
#   =>   "Armoire RPD : 4 objets"
#
# locker_status([])   =>   "Armoire RPD : 0 objets"
#
# Indice : f-string + len()
# ------------------------------------------------------------
def locker_status(locker):
    nombre = len(locker)
    return f"Armoire RPD : {nombre} objets"