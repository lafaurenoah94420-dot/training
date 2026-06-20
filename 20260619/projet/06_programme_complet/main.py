# ============================================================
# Exercice 6/6 — Mini programme complet
# ============================================================
# 📄 Instructions : open /Users/noah/Desktop/Python/20260619/projet/06_programme_complet/instructions.html
# 🧪 Tester       : python3 /Users/noah/Desktop/Python/20260619/projet/06_programme_complet/tester.py
# ============================================================
def rapport_nuit(zone, nombre):
    return f"Zone {zone} — {nombre} infectés repérés"

def evaluer_nuit(infectes):
    if infectes <= 5:
        return "Calme"
    elif infectes > 5 and infectes <= 16:
        return "Tendu"
    elif infectes > 16:
        return "Critique"