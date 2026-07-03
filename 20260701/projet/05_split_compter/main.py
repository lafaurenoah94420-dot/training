# ============================================================
# Exercice 5/6 — Split et compter
# ============================================================
# 📁 Dossier      : cd /Users/noah/Desktop/Python/20260701/projet/05_split_compter
# 📄 Instructions : open /Users/noah/Desktop/Python/20260701/projet/05_split_compter/instructions.html
# 🧪 Tester       : python3 tester.py
# ============================================================
def compter_unites(texte_liste):
    if texte_liste == "" :
        return 0
    return len(texte_liste.split(","))