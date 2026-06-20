# ============================================================
# Exercice 3/6 — Compter dans une liste
# ============================================================
# 📄 Instructions : open /Users/noah/Desktop/Python/20260620/projet/03_compter/instructions.html
# 🧪 Tester       : python3 /Users/noah/Desktop/Python/20260620/projet/03_compter/tester.py
# ============================================================
def compter_type(liste, nom):
    compteur = 0
    for i in liste:
        if i == nom:
            compteur += 1
        else:
            compteur += 0
    return compteur