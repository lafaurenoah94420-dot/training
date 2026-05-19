# ============================================================
# GTA — Comptoir de liasses (build)
# ============================================================
# Implémente les 5 fonctions ci-dessous pour que main.py fonctionne.
# Lance : python3 main.py
# Implémente-les dans l'ordre — commence par TODO 1.
# ============================================================


# ------------------------------------------------------------
# TODO 1 — Liasses entières dans le butin
# ------------------------------------------------------------
# Franklin range le cash par liasses de même valeur. Tu renvoies combien de liasses
# complètes tiennent dans le total, sans compter les billets « en vrac ».
#
#   cash        : montant total en dollars (int)
#   bundle_size : valeur d'une liasse complète (int)
#
# full_stacks(1000, 50)   =>   20
#
# full_stacks(75, 50)   =>   1
#
# Indice : //
# ------------------------------------------------------------
def full_stacks(cash, bundle_size):
    return cash // bundle_size


# ------------------------------------------------------------
# TODO 2 — Palier de recherche sur la radio
# ------------------------------------------------------------
# Selon le nombre d'étoiles, la police diffuse un niveau d'alerte différent.
# Utilise des seuils stricts dans cet ordre :
#   stars <= 2  →  "Discret"
#   stars <= 4  (mais pas déjà Discret)  →  "Recherché"
#   sinon  →  "Priorité max"
#
#   stars   : niveau de wanted (int)
#
# wanted_tier(1)   =>   "Discret"
#
# wanted_tier(3)   =>   "Recherché"
#
# wanted_tier(5)   =>   "Priorité max"
#
# Indice : if / elif / else avec <=
# ------------------------------------------------------------
def wanted_tier(stars):
    if stars <= 2:
        return"Discret"
    elif stars <= 4:
        return"Recherché"
    else:
        return"Priorité max"




# ------------------------------------------------------------
# TODO 3 — Phrase radio formatée
# ------------------------------------------------------------
# Le dispatcher veut une ligne unique avec l'indicatif et le quartier, pour l'écran
# du téléphone. La ponctuation doit être exacte.
#
#   callsign   : indicatif du crew (str)
#   district   : nom du quartier (str)
#
# radio_line("Fox", "Vinewood")   =>   "Radio : Fox — Vinewood"
#
# radio_line("V-12", "Davis")   =>   "Radio : V-12 — Davis"
#
# Indice : return avec une f-string (tiret long — entre indicatif et quartier)
# ------------------------------------------------------------
def radio_line(callsign, district):
    return f"Radio : {callsign} — {district}"


# ------------------------------------------------------------
# TODO 4 — Pseudos du crew sur le comptoir
# ------------------------------------------------------------
# Tu pars d'une liste vide, tu y ajoutes trois pseudos dans l'ordre, puis tu renvoies
# la liste complète pour l'affichage du planning.
#
# crew_roster()   =>   ["V-12", "Cash", "Hook"]
#
# Indice : liste vide, trois fois .append(...), puis return
# ------------------------------------------------------------
def crew_roster():
    liste = []
    liste.append("V-12")
    liste.append("Cash")
    liste.append("Hook")
    return liste


# ------------------------------------------------------------
# TODO 5 — Réputation après un coup (plafond 100)
# ------------------------------------------------------------
# Chaque braquage rapporte des points de réputation street, mais le compteur ne peut
# jamais dépasser 100 sur l'interface.
#
#   rep   : réputation actuelle (int)
#   gain  : points gagnés sur le coup (int)
#
# cap_rep(85, 30)   =>   100
#
# cap_rep(40, 20)   =>   60
#
# Indice : return min(100, ...)
# ------------------------------------------------------------
def cap_rep(rep, gain):
    return(min(100, rep + gain))
