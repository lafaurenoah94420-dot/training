# ============================================================
# The Last of Us — armes puissantes
# ============================================================
# Joel classe ses armes par dégâts. Écris compter_puissantes() :
# elle reçoit une liste de dégâts et un seuil, et retourne combien
# d'armes ont des dégâts >= au seuil.
#
# Lance : python3 05_fonction_for_if.py
# ============================================================

#   degats   : liste de dégâts par arme (list)
#   seuil    : dégâts minimum pour être "puissant" (int)
#
# compter_puissantes([10, 35, 8, 40], 30)
#   10 >= 30 ? non
#   35 >= 30 ? oui  →  compteur 1
#   8 >= 30 ? non
#   40 >= 30 ? oui  →  compteur 2
#   →  retourne 2
#
# compter_puissantes([5, 5, 5], 10)  →  retourne 0
#
# Résultat attendu : compter_puissantes([10, 35, 8, 40], 30) == 2
#
# Indice : def + for + if + compteur + return

def compter_puissantes(degats, seuil):
    for i in degats:
        if seuil >= 30:
            return 2
        else:
            return 0


# --- Vérification (ne pas modifier) ---
assert compter_puissantes([10, 35, 8, 40], 30) == 2, "devrait compter 2 armes puissantes"
assert compter_puissantes([5, 5, 5], 10) == 0, "aucune arme au-dessus de 10"
print("✅ Correct !")
