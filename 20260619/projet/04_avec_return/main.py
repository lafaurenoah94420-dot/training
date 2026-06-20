# ============================================================
# Exercice 4/6 — return
# ============================================================
# 📄 Instructions : open /Users/noah/Desktop/Python/20260619/projet/04_avec_return/instructions.html
# 🧪 Tester       : python3 /Users/noah/Desktop/Python/20260619/projet/04_avec_return/tester.py
# ============================================================
def munitions_restantes(chargeur, tirees):
    for i in range(tirees):
        if chargeur <= 0:
            return 0
        elif chargeur > 0:
            chargeur -= 1
    return chargeur