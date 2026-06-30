# ============================================================
# Exercice 4/6 — Vérifier une clé
# ============================================================
# 📁 Dossier      : cd /Users/noah/Desktop/Python/20260621/projet/04_fonction_contient
# 📄 Instructions : open /Users/noah/Desktop/Python/20260621/projet/04_fonction_contient/instructions.html
# 🧪 Tester       : python3 tester.py
# ============================================================
def a_objet(inventaire, nom):
    if nom in inventaire:
        return True
    else:
        return False