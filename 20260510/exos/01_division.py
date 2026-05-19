# ============================================================
# GTA — partage du butin en liasses
# ============================================================
# Franklin récupère 1000$ en cash. Chaque liasse « propre » vaut 50$.
# Combien de liasses complètes peut-il ranger sans couper une liasse ?
#
# Lance : python3 01_division.py
# ============================================================

cash = 1000
liasse = 50

liasses_pleines = cash // liasse


# Calcule combien de liasses entières tiennent dans cash (division entière).
#
# 1000 // 50 = 20   (vingt liasses complètes)
#
# Résultat attendu : liasses_pleines == 20
#
# Indice : opérateur // (division entière)

# À toi :


# --- Vérification (ne pas modifier) ---
assert liasses_pleines == 20, "1000 // 50 doit donner 20 liasses pleines."
print("✅ Correct !")
