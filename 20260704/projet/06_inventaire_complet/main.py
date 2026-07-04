# ============================================================
# Exercice 6/6 — Inventaire complet
# ============================================================
# 📁 Dossier      : cd /Users/noah/Desktop/Python/20260704/projet/06_inventaire_complet
# 📄 Instructions : open /Users/noah/Desktop/Python/20260704/projet/06_inventaire_complet/instructions.html
# 🧪 Tester       : python3 tester.py
# ============================================================
def initialiser():
    dictionnaire = {"bandage": 3, "conserve": 2, "marteau": 1}
    return dictionnaire

def ramasser(inventaire, objets, qty):
        inventaire[objets] += qty

def afficher_total(inventaire):
    total = 0
    for i in inventaire:
        total += inventaire[i]
    return total