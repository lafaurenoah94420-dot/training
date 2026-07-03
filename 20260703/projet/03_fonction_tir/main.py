# ============================================================
# Exercice 3/6 — Tir aléatoire
# ============================================================
# 📁 Dossier      : cd /Users/noah/Desktop/Python/20260703/projet/03_fonction_tir
# 📄 Instructions : open /Users/noah/Desktop/Python/20260703/projet/03_fonction_tir/instructions.html
# 🧪 Tester       : python3 tester.py
# ============================================================
import random

def tirer_degats(min_dmg, max_dmg):
    return random.randint(min_dmg, max_dmg)