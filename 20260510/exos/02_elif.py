# ============================================================
# Project Zomboid — alerte faim
# ============================================================
# La jauge de faim est un nombre de 0 à 100. Selon le niveau, l'écran
# affiche un message différent (trois paliers, pas seulement deux).
#
# Lance : python3 02_elif.py
# ============================================================

faim = 55

message = ""
if faim > 70:
    message = "Rassasié"
elif faim > 30 and faim < 70:
    message = "Affamé"
else:
    message = "Critique"
# Assigne message selon faim :
#   faim > 70  →  "Rassasié"
#   faim > 30  (mais pas > 70)  →  "Affamé"
#   sinon  →  "Critique"
#
# Avec faim == 55 :
#   55 > 70 ? non
#   55 > 30 ? oui  →  message = "Affamé"
#
# Résultat attendu : message == "Affamé"
#
# Indice : if / elif / else (dans cet ordre, du plus haut au plus bas)

# À toi :


# --- Vérification (ne pas modifier) ---
assert message == "Affamé", (
    f"Obtenu : '{message}' — avec faim = 55, le message attendu est 'Affamé'."
)
print("✅ Correct !")
