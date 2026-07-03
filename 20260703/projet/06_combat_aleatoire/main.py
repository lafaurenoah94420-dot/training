# ============================================================
# Exercice 6/6 — Combat aléatoire
# ============================================================
# 📁 Dossier      : cd /Users/noah/Desktop/Python/20260703/projet/06_combat_aleatoire
# 📄 Instructions : open /Users/noah/Desktop/Python/20260703/projet/06_combat_aleatoire/instructions.html
# 🧪 Tester       : python3 tester.py
# ============================================================
import random

def compter_tirs(vie, min_dmg, max_dmg):
    tours = 0
    if vie <= 0:
        return tours
    else:
        while vie > 0:
            tours += 1
            degats = random.randint(min_dmg, max_dmg)
            vie -= degats
    return tours



