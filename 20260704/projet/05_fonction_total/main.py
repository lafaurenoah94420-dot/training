# ============================================================
# Exercice 5/6 — Total des unités
# ============================================================
# 📁 Dossier      : cd /Users/noah/Desktop/Python/20260704/projet/05_fonction_total
# 📄 Instructions : open /Users/noah/Desktop/Python/20260704/projet/05_fonction_total/instructions.html
# 🧪 Tester       : python3 tester.py
# ============================================================
def total_unites(stocks):
    total = 0
    for i in stocks:
        total += stocks[i]
    return total