# ============================================================
# Resident Evil — pharmacie du commissariat
# ============================================================
# Leon consulte le stock d'antidotes dans l'armoire.
# S'il en reste au moins 2, il peut partir serein. Sinon,
# l'écran affiche une alerte.
#
# Lance : python3 04_dict_if.py
# ============================================================

stock = {"herb_green": 5, "spray": 1, "antidote": 1}
objet = "antidote"
quantite = 0
alerte = ""

# 1) Lis la quantité de antidote dans stock → quantite
# 2) Si quantite >= 2 → alerte = "Stock suffisant"
#    Sinon           → alerte = "Stock bas"
#
# stock["antidote"] = 1
#   1 >= 2 ?  non  →  alerte = "Stock bas"
#
# Résultat attendu : quantite == 1  et  alerte == "Stock bas"
#
# Indice : dict["cle"] puis if / else

# À toi :
quantite = stock["antidote"]

if quantite >= 2:
    alerte = "Stock suffisant"
else:
    alerte = "Stock bas"

# --- Vérification (ne pas modifier) ---
assert quantite == 1, f"quantite devrait valoir 1, obtenu : {quantite}"
assert alerte == "Stock bas", f"Obtenu : '{alerte}', attendu : 'Stock bas'"
print("✅ Correct !")
