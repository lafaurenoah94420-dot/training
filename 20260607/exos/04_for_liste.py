# ============================================================
# Hearts of Iron 4 — Total des pertes
# ============================================================
# Une division subit des pertes chaque jour. Additionne toutes les
# valeurs de la liste pour obtenir le total.
#
# Lance : python3 04_for_liste.py
# ============================================================

pertes = [12, 5, 30, 8, 15]
total_pertes = sum(pertes)

# Parcours pertes et additionne chaque valeur dans total_pertes.
#
# tour 1 : p = 12  →  total_pertes = 12
# tour 2 : p = 5   →  total_pertes = 17
# tour 3 : p = 30  →  total_pertes = 47
# tour 4 : p = 8   →  total_pertes = 55
# tour 5 : p = 15  →  total_pertes = 70
#
# Résultat attendu : total_pertes == 70
#
# Indice : for + +=

# À toi :


# --- Vérification (ne pas modifier) ---
assert total_pertes == 70, f"Obtenu : {total_pertes}, attendu : 70"
print("✅ Correct !")
