# ============================================================
# Exercice 5/6 — Deux fonctions ensemble
# ============================================================
# 📄 Instructions : open /Users/noah/Desktop/Python/20260619/projet/05_combinaison/instructions.html
# 🧪 Tester       : python3 /Users/noah/Desktop/Python/20260619/projet/05_combinaison/tester.py
# ============================================================
def est_critique(vie):
    if vie <= 20:
        return True
    else:
        return False

def statut_vie(vie):
    resultat = est_critique(vie)
    if resultat == True:
        return "CRITIQUE"
    else:
        return "OK"