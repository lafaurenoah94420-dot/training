# ============================================================
# Resident Evil — nom de virus
# ============================================================
# Le rapport du labo mentionne le virus "T-Virus".
# Pour l'affichage secret, remplace "T-" par "Projet ".
#
# Lance : python3 02_replace.py
# ============================================================

nom_virus = "T-Virus"
nom_secret = ""

# Remplace "T-" par "Projet " dans nom_virus et stocke dans nom_secret.
#
# "T-Virus"  →  remplace "T-" par "Projet "  →  "Projet Virus"
#
# Résultat attendu : nom_secret == "Projet Virus"
#
# Indice : .replace()

# À toi :
nom_secret = nom_virus.replace("T-", "Projet ")

# --- Vérification (ne pas modifier) ---
assert nom_secret == "Projet Virus", f"Obtenu : '{nom_secret}'"
print("✅ Correct !")
