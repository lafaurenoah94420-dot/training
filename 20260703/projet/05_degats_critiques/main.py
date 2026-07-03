# ============================================================
# Exercice 5/6 — Dégâts critiques
# ============================================================
# 📁 Dossier      : cd /Users/noah/Desktop/Python/20260703/projet/05_degats_critiques
# 📄 Instructions : open /Users/noah/Desktop/Python/20260703/projet/05_degats_critiques/instructions.html
# 🧪 Tester       : python3 tester.py
# ============================================================
import math
import random

def degats_finaux(base, bonus_min, bonus_max):
    degats_finaux = random.randint(bonus_min, bonus_max) + math.floor(base)
    return degats_finaux