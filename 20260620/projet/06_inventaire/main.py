# ============================================================
# Exercice 6/6 — Mini inventaire
# ============================================================
# 📄 Instructions : open /Users/noah/Desktop/Python/20260620/projet/06_inventaire/instructions.html
# 🧪 Tester       : python3 /Users/noah/Desktop/Python/20260620/projet/06_inventaire/tester.py
# ============================================================
def ajouter(inventaire, objet):
    inventaire.append(objet)
    return inventaire

def resume_inventaire(inventaire):
    return (f"Inventaire : {len(inventaire)} objets")
