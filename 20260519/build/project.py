# ============================================================
# The Last of Us — Relais de ravitaillement (build)
# ============================================================
# Implémente les 5 fonctions ci-dessous pour que main.py fonctionne.
# Lance : python3 main.py
# Implémente-les dans l'ordre — commence par TODO 1.
# ============================================================


# ------------------------------------------------------------
# TODO 1 — Corriger l'affichage de la fréquence
# ------------------------------------------------------------
# Le terminal du relais affiche mal les fréquences : les tirets sont des
# underscores. Tu renvoies la chaîne corrigée pour l'écran radio.
#
#   raw_label   : fréquence telle qu'affichée (str)
#
# format_channel("QZ_7")   =>   "QZ-7"
#
# format_channel("RELAY_A3")   =>   "RELAY-A3"
#
# Indice : .replace()
# ------------------------------------------------------------
def format_channel(raw_label):
    return raw_label.replace("_", "-")


# ------------------------------------------------------------
# TODO 2 — Lire le stock d'un article
# ------------------------------------------------------------
# Joel consulte le cache du relais : un dictionnaire article → quantité.
# Tu renvoies combien il reste pour la clé demandée.
#
#   cache   : inventaire du relais (dict, ex. {"food": 6, "bullets": 120})
#   item    : nom de l'article (str)
#
# read_supply({"food": 6, "bullets": 120}, "food")   =>   6
#
# read_supply(©"food": 6, "bullets": 120}, "bullets")   =>   120
#
# Indice : cache[item]
# ------------------------------------------------------------
def read_supply(cache, item):
    return cache[item]


# ------------------------------------------------------------
# TODO 3 — Réapprovisionner un article
# ------------------------------------------------------------
# Une caisse arrive au relais : tu ajoutes la quantité à l'article dans le cache.
# La fonction modifie le dict sur place (pas besoin de return).
#
#   cache    : inventaire du relais (dict)
#   item     : nom de l'article (str)
#   amount   : quantité à ajouter (int)
#
# Avant : cache = {"food": 6}
# restock(cache, "food", 3)   =>   cache["food"] vaut 9
#
# Avant : cache = {"bandages": 0}
# restock(cache, "bandages", 5)   =>   cache["bandages"] vaut 5
#
# Indice : cache[item] = cache[item] + amount
# ------------------------------------------------------------
def restock(cache, item, amount):
    cache[item] += amount 
    


# ------------------------------------------------------------
# TODO 4 — Poids total des sacs
# ------------------------------------------------------------
# Chaque sac a un poids en kg. Joel doit connaître le total pour le portage.
# Parcours la liste et additionne toutes les valeurs.
#
#   weights   : liste des poids en kg (list d'int)
#
# total_weight([2, 5, 3, 1])   =>   11
#
# total_weight([10])   =>   10
#
# Indice : boucle for + +=
# ------------------------------------------------------------
def total_weight(weights):
    total = 0
    for i in weights:
        total += i
    return total


# ------------------------------------------------------------
# TODO 5 — Jours de rations restantes
# ------------------------------------------------------------
# Avec le stock total de rations, combien de jours complets tiennent les
# survivants ? Par défaut chaque jour consomme 2 rations (paramètre daily).
#
#   total   : nombre de rations en stock (int)
#   daily   : rations consommées par jour (int, défaut 2)
#
# rations_days(24)   =>   12
#
# rations_days(25, 5)   =>   5
#
# Indice : def rations_days(total, daily=2): puis return avec //
# ------------------------------------------------------------
def rations_days(total, daily=2):
    return total // daily
