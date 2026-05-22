# ============================================================
# Hearts of Iron 4 — rapport de front
# ============================================================
# Le jeu affiche une ligne de statut avec le nom du pays et
# le nombre de divisions engagées. Construis cette ligne.
#
# Lance : python3 01_fstrings.py
# ============================================================

pays = "Allemagne"
divisions = 24
rapport = ""

# Construis rapport avec une f-string pour obtenir exactement :
# "Allemagne : 24 divisions en ligne"
#
# pays = "Allemagne", divisions = 24
#   →  "Allemagne : 24 divisions en ligne"
#
# Résultat attendu : rapport == "Allemagne : 24 divisions en ligne"
#
# Indice : f"... {variable} ..."

# À toi :
rapport = f"{pays} : {divisions} divisions en ligne"

# --- Vérification (ne pas modifier) ---
assert rapport == "Allemagne : 24 divisions en ligne", f"Obtenu : '{rapport}'"
print("✅ Correct !")
