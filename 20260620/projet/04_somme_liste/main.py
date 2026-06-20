# ============================================================
# Exercice 4/6 — Total d'une liste
# ============================================================
# 📄 Instructions : open /Users/noah/Desktop/Python/20260620/projet/04_somme_liste/instructions.html
# 🧪 Tester       : python3 /Users/noah/Desktop/Python/20260620/projet/04_somme_liste/tester.py
# ============================================================
def total_degats(degats):
    accumulateur = 0
    for i in degats:
        accumulateur += i
    return accumulateur


