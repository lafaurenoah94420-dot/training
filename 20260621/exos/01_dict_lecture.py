# ============================================================
# GTA — Amende au commissariat
# ============================================================
# Franklin consulte son casier au commissariat. Les infos sont
# stockées dans un dictionnaire : type d'infraction → montant.
# Il veut afficher le montant de sa dernière contravention.
#
# Lance : python3 01_dict_lecture.py
# ============================================================

casier = {
    "stationnement": 80,
    "exces_vitesse": 250,
    "feu_rouge": 135,
}

amende = 0

# Lis la valeur associée à la clé "exces_vitesse" et stocke-la dans amende.
#
# casier["exces_vitesse"]  →  la valeur liée à cette clé  →  250
#
# Résultat attendu : amende == 250
#
# Indice : dict["cle"]

# À toi :
amende = casier["exces_vitesse"]

# --- Vérification (ne pas modifier) ---
assert amende == 250, f"Obtenu : {amende}, attendu : 250"
print("✅ Correct !")
