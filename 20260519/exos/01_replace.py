# ============================================================
# The Last of Us — fréquence radio
# ============================================================
# Joel doit envoyer un message sur la fréquence « QZ-7 ».
# Le terminal affiche mal le tiret : il est écrit avec un underscore.
# Corrige la chaîne pour l'affichage.
#
# Lance : python3 01_replace.py
# ============================================================

frequence_brute = "QZ_7"
frequence_affichee = frequence_brute.replace("QZ_7", "QZ-7")

# Remplace chaque "_" par "-" et stocke le résultat dans frequence_affichee.
#
# "QZ_7"  →  remplacer "_" par "-"  →  "QZ-7"
#
# Résultat attendu : frequence_affichee == "QZ-7"
#
# Indice : .replace()

# À toi :


# --- Vérification (ne pas modifier) ---
assert frequence_affichee == "QZ-7", f"Obtenu : '{frequence_affichee}'"
print("✅ Correct !")
