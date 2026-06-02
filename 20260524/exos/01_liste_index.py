# ============================================================
# GTA — Arme équipée
# ============================================================
# Franklin a plusieurs armes dans son inventaire rapide.
# La case 0 est celle équipée en premier. Le jeu doit afficher
# le nom de l'arme en slot 0 pour le HUD.
#
# Lance : python3 01_liste_index.py
# ============================================================

inventaire = ["Pistolet", "Fusil à pompe", "Couteau", "SMG"]
arme_equipee = ""

# Récupère l'élément à l'index 0 de inventaire
# et stocke-le dans arme_equipee.
#
# inventaire[0]  →  "Pistolet"
#
# Résultat attendu : arme_equipee == "Pistolet"
#
# Indice : inventaire[0]

# À toi :
arme_equipee = inventaire[0]

# --- Vérification (ne pas modifier) ---
assert arme_equipee == "Pistolet", f"Obtenu : '{arme_equipee}'"
print("✅ Correct !")
