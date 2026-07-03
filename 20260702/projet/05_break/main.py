# ============================================================
# Exercice 5/6 — Break dans une boucle
# ============================================================
# 📁 Dossier      : cd /Users/noah/Desktop/Python/20260702/projet/05_break
# 📄 Instructions : open /Users/noah/Desktop/Python/20260702/projet/05_break/instructions.html
# 🧪 Tester       : python3 tester.py
# ============================================================
def fouiller_coffre(objets, cible):
    i = 0
    trouve = False
    while i < len(objets):
        if objets[i] == cible:
            trouve = True
            break
        i += 1
    
    if trouve == True:
        return i
    else:
        return -1 

