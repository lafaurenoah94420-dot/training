# ============================================================
# Exercice 4/6 — Distance sur la carte
# ============================================================
# 📁 Dossier      : cd /Users/noah/Desktop/Python/20260703/projet/04_fonction_distance
# 📄 Instructions : open /Users/noah/Desktop/Python/20260703/projet/04_fonction_distance/instructions.html
# 🧪 Tester       : python3 tester.py
# ============================================================
import math

def distance_entre(x1, y1 , x2, y2):
    return math.floor(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))