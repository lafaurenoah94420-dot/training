# ============================================================
# Hearts of Iron IV — divisions en réserve
# ============================================================
# Une liste donne le statut de chaque division. Compte combien
# sont exactement "réserve" (compteur qui monte à chaque match).
#
# Lance : python3 04_for_if.py
# ============================================================

statuts = ["front", "réserve", "réserve", "entraînement", "réserve", "front"]

nombre_reserve = 0

# Parcours statuts. À chaque fois que l'élément vaut "réserve", ajoute 1.
#
# Tour par tour : front (non) · réserve (+1) · réserve (+1) · …
#
# Résultat attendu : nombre_reserve == 3
#
# Indice : for s in statuts:  puis  if s == "réserve":

# À toi :
for s in statuts:
    if s == "réserve":
        nombre_reserve += 1

# --- Vérification (ne pas modifier) ---
assert nombre_reserve == 3, f"Obtenu : {nombre_reserve}, attendu : 3"
print("✅ Correct !")
