# ============================================================
# GTA — Stats de la voiture de Franklin
# ============================================================
# Franklin vient d'installer un turbo sur sa voiture. Le jeu
# met à jour la stat "vitesse_max" dans le dictionnaire du véhicule.
#
# Lance : python3 03_dict.py
# ============================================================

voiture = {
    "modele": "Buffalo",
    "vitesse_max": 180,
    "acceleration": 7,
}

# 1) Lis la vitesse actuelle et stocke-la dans vitesse_actuelle
# 2) Ajoute 25 km/h au turbo : voiture["vitesse_max"] = nouvelle valeur
# 3) Stocke la nouvelle vitesse dans vitesse_apres_turbo
#
# vitesse_actuelle  →  voiture["vitesse_max"]  →  180
# après turbo       →  180 + 25                 →  205
#
# Résultat attendu : vitesse_actuelle == 180  et  vitesse_apres_turbo == 205
#
# Indice : dict["cle"] pour lire et écrire

vitesse_actuelle = 0
vitesse_apres_turbo = 0

# À toi :

vitesse_actuelle = voiture["vitesse_max"]
vitesse_apres_turbo = vitesse_actuelle + 25

voiture["vitesse_max"] = vitesse_apres_turbo

# --- Vérification (ne pas modifier) ---
assert vitesse_actuelle == 180, f"vitesse_actuelle : {vitesse_actuelle}"
assert voiture["vitesse_max"] == 205, f"vitesse_max dans le dict : {voiture['vitesse_max']}"
assert vitesse_apres_turbo == 205, f"vitesse_apres_turbo : {vitesse_apres_turbo}"
print("✅ Correct !")
