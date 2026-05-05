# ============================================================
# Hearts of Iron IV — ligne de rapport
# ============================================================
# Le jeu affiche une ligne du type « France : 42 divisions » pour le
# résumé stratégique. Tu dois construire exactement cette phrase avec les
# deux variables déjà définies ci-dessous.
#
# Lance : python 01_fstring.py
# ============================================================

pays = "France"
divisions = 42
ligne_rapport = ""

# Construis ligne_rapport pour qu'elle soit exactement :
# France : 42 divisions
# (respecte espaces, deux-points et le mot « divisions ».)
#
# Contenu attendu : France : 42 divisions
#
# Indice : f"..."

# À toi :


# --- Vérification (ne pas modifier) ---
assert ligne_rapport == "France : 42 divisions", f"Obtenu : '{ligne_rapport}'"
print("✅ Correct !")
