# ============================================================
# Hearts of Iron IV — tirage d'offensive
# ============================================================
# Le haut-commandement tire au sort un nom de plan parmi une liste courte.
# Pour ce fichier, la graine est fixée pour que le résultat soit toujours le même.
#
# Lance : python3 05_choice.py
# ============================================================

import random

random.seed(5)

plans = ["Alpha", "Bravo"]

plan_retenu = random.choice(plans)

# Mets dans plan_retenu un tirage aléatoire dans plans avec random.choice.
#
# Déroulé avec random.seed(5) déjà appelé :
#   le tirage doit être "Bravo"
#
# Résultat attendu : plan_retenu == "Bravo"
#
# Indice : random.choice(plans)

# À toi :


# --- Vérification (ne pas modifier) ---
assert plan_retenu == "Bravo", (
    f"Obtenu : {repr(plan_retenu)} — avec seed(5), choice doit retourner 'Bravo'."
)
print("✅ Correct !")
