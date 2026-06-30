# ============================================================
# Exercice 6/6 — Résumé d'inventaire
# ============================================================
# 📁 Dossier      : cd /Users/noah/Desktop/Python/20260621/projet/06_inventaire_complet
# 📄 Instructions : open /Users/noah/Desktop/Python/20260621/projet/06_inventaire_complet/instructions.html
# 🧪 Tester       : python3 tester.py
# ============================================================
def resume_inventaire(inventaire):
    len_inv = len(inventaire)
    total = 0
    for i in inventaire:
        total += inventaire[i]
    return f"Inventaire : {len_inv} types, {total} objets"

