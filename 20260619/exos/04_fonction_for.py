# ============================================================
# Hearts of Iron 4 — pertes par division
# ============================================================
# Écris une fonction somme_divisions() qui reçoit une liste de nombres
# (hommes perdus par division) et retourne la somme totale.
#
# Lance : python3 04_fonction_for.py
# ============================================================

# somme_divisions([100, 50, 25])  →  100 + 50 + 25 = 175  →  retourne 175
# somme_divisions([1, 2, 3])      →  retourne 6
# somme_divisions([])             →  retourne 0
#
# Résultat attendu : somme_divisions([100, 50, 25]) == 175
#
# Indice : def + for + accumulateur += + return

def somme_divisions(pertes):
    total = 0
    for i in pertes:
        total += i
    return total
# --- Vérification (ne pas modifier) ---
assert somme_divisions([100, 50, 25]) == 175, "somme_divisions([100, 50, 25]) doit retourner 175"
assert somme_divisions([1, 2, 3]) == 6, "somme_divisions([1, 2, 3]) doit retourner 6"
assert somme_divisions([]) == 0, "somme_divisions([]) doit retourner 0"
print("✅ Correct !")
