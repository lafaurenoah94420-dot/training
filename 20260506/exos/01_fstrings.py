# ============================================================
# The Last of Us — rapport de route
# ============================================================
# Ellie doit envoyer une ligne radio synthétique avec son nom de code et le
# nombre d'infectés repérés dans les deux dernières heures. Tu dois construire
# cette ligne dans une seule chaîne.
#
# Lance : python3 01_fstrings.py
# ============================================================

code_name = "Éclair"
spotted = 12

ligne_radio = ""

# Construis ligne_radio pour que le texte soit EXACTEMENT au format :
#
#   Code Éclair — contacts : 12.
#
# (avec les valeurs de code_name et spotted dedans, sans casser la ponctuation.)
#
# Déroulé avec les valeurs actuelles :   
#   code_name vaut "Éclair"
#   spotted vaut 12
#   la phrase doit contenir le mot "Éclair", deux-points + espace, puis "12"
#
# Résultat attendu : ligne_radio == "Code Éclair — contacts : 12."
#
# Indice : f-string avec accolades pour insérer code_name et spotted

# À toi :
ligne_radio = f"Code {code_name} — contacts : {spotted}."

# --- Vérification (ne pas modifier) ---
assert ligne_radio == "Code Éclair — contacts : 12.", (
    f"Obtenu : {repr(ligne_radio)} — vérifie tirets, ponctuation et valeurs."
)
print("✅ Correct !")
