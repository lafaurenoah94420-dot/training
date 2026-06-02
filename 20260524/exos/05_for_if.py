# ============================================================
# HOI4 — Provinces capturées
# ============================================================
# Tu repasses en revue une liste de provinces après une offensive.
# Certaines sont déjà sous ton contrôle (statut "captured").
# Compte combien tu en as prises.
#
# Lance : python3 05_for_if.py
# ============================================================

provinces = [
    {"nom": "Lille", "statut": "captured"},
    {"nom": "Arras", "statut": "enemy"},
    {"nom": "Amiens", "statut": "captured"},
    {"nom": "Rouen", "statut": "captured"},
    {"nom": "Reims", "statut": "enemy"},
]

nb_capturees = 0

# Parcours provinces avec for.
# Si le statut de la province vaut "captured", ajoute 1 à nb_capturees.
#
# Lille   → captured  →  nb_capturees = 1
# Arras   → enemy     →  nb_capturees = 1
# Amiens  → captured  →  nb_capturees = 2
# Rouen   → captured  →  nb_capturees = 3
# Reims   → enemy     →  nb_capturees = 3
#
# Résultat attendu : nb_capturees == 3
#
# Indice : for p in provinces:  puis  if p["statut"] == "captured":

# À toi :
for p in provinces:
    if p["statut"] == "captured":
        nb_capturees += 1

# --- Vérification (ne pas modifier) ---
assert nb_capturees == 3, f"Obtenu : {nb_capturees}, attendu : 3"
print("✅ Correct !")
