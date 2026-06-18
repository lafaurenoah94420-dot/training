# ============================================================
# Hearts of Iron 4 — pertes totales
# ============================================================
# Écris une fonction total_pertes() qui reçoit une liste de nombres
# et retourne la somme de tous les éléments (avec une boucle for).
#
# Lance : python3 05_fonction_liste.py
# ============================================================

# total_pertes([10, 5, 3])  →  10 + 5 + 3 = 18  →  retourne 18
# total_pertes([1, 1, 1, 1])  →  retourne 4
# total_pertes([])  →  rien à additionner  →  retourne 0
#
# Résultat attendu : total_pertes([10, 5, 3]) == 18
#
# Indice : def + for + += + return

def total_pertes(pertes):
    total = 0
    for p in pertes:
        total += p
    return total


# --- Vérification (ne pas modifier) ---
assert total_pertes([10, 5, 3]) == 18, "total_pertes([10, 5, 3]) doit retourner 18"
assert total_pertes([1, 1, 1, 1]) == 4, "total_pertes([1, 1, 1, 1]) doit retourner 4"
assert total_pertes([]) == 0, "total_pertes([]) doit retourner 0"
print("✅ Correct !")
