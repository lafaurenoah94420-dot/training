# ============================================================
# Project Zomboid — coup de stress après sprint
# ============================================================
# Tu tires un jet pour représenter un sprint nerveux, puis tu soustrais une pénalité
# de fatigue. Le stress restant ne peut pas descendre sous 0.
#
# Lance : python3 04_randint_max.py
# ============================================================

import random

random.seed(10)

jet_sprint = random.randint(1, 10)
penalite = 3
stress_net = 0

stress_net = max(0, jet_sprint - penalite)
# Étape 1 : place dans jet_sprint un entier aléatoire entre 1 et 10 inclus.
#
# Étape 2 : calcule stress_net = max(0, jet_sprint - penalite)
#
# Déroulé avec la graine fixée à 10 :
#   jet_sprint doit valoir 10
#   penalite vaut 3
#   10 - 3 = 7  →  stress_net doit être 7 (pas besoin du plancher ici)
#
# Résultat attendu : stress_net == 7
#
# Indice : random.randint(1, 10) puis max(0, ...)

# À toi :


# --- Vérification (ne pas modifier) ---
assert stress_net == 7, (
    f"Obtenu : stress_net={stress_net} — avec seed(10), jet=10 et penalite=3 → 7."
)
print("✅ Correct !")
