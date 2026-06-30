# ============================================================
# Exercice 5/6 — Totaliser les valeurs
# ============================================================
# 📁 Dossier      : cd /Users/noah/Desktop/Python/20260621/projet/05_fonction_total
# 📄 Instructions : open /Users/noah/Desktop/Python/20260621/projet/05_fonction_total/instructions.html
# 🧪 Tester       : python3 tester.py
# ============================================================
def total_ressources(depot):
    total = 0
    for i in depot:
        total += depot[i]
    return total
