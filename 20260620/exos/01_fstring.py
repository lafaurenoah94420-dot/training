# ============================================================
# The Last of Us — HUD de survie
# ============================================================
# L'interface affiche le nom du personnage et ses points de vie
# sur une seule ligne. Ellie a 73 PV après un combat.
#
# Lance : python3 01_fstring.py
# ============================================================

nom = "ellie"
pv = 73
ligne_hud = f"{nom} — {pv} PV"

# Construis la ligne avec une f-string :
# nom = "ellie", pv = 73  →  ligne_hud = "ellie — 73 PV"
#
# Résultat attendu : ligne_hud == "ellie — 73 PV"
#
# Indice : f"... {nom} ... {pv} ..."

# À toi :


# --- Vérification (ne pas modifier) ---
assert ligne_hud == "ellie — 73 PV", f"Obtenu : '{ligne_hud}'"
print("✅ Correct !")
