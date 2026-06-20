# ============================================================
# Exercice 5/6 — Présence et position
# ============================================================
# 📄 Instructions : open /Users/noah/Desktop/Python/20260620/projet/05_presence/instructions.html
# 🧪 Tester       : python3 /Users/noah/Desktop/Python/20260620/projet/05_presence/tester.py
# ============================================================
def contient(liste, objet):
    if objet in liste:
        return True
    else:
        return False

def index_de(liste, objet):
    position = 0
    if contient(liste, objet) == False:
        return -1
    for i in liste:
        if liste[position] == objet:
            return position
        else:
            position = position + 1

liste = ["pomme", "banane", "carotte", "poire"]
resultat = index_de(liste, "poire")