# ============================================================
# GTA — crimes de la soirée
# ============================================================
# Franklin note chaque crime dans une liste au fil de la nuit.
# Ajoute deux crimes à la liste crimes.
#
# Lance : python3 03_append.py
# ============================================================

crimes = ["vol de voiture"]

# crimes vaut ["vol de voiture"] au départ.
# Ajoute "braquage" puis "course-poursuite" avec .append()
#
# Résultat attendu : crimes == ["vol de voiture", "braquage", "course-poursuite"]
#
# Indice : crimes.append("...")

# À toi :
crimes.append("braquage")
crimes.append("course-poursuite")


# --- Vérification (ne pas modifier) ---
assert crimes == ["vol de voiture", "braquage", "course-poursuite"], f"Obtenu : {crimes}"
print("✅ Correct !")
