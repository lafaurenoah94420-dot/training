# ============================================================
# Exercice 1/6 — Boucle while, découverte
# ============================================================
# 📁 Dossier      : cd /Users/noah/Desktop/Python/20260702/projet/01_while_decouverte
# 📄 Instructions : open /Users/noah/Desktop/Python/20260702/projet/01_while_decouverte/instructions.html
# 🧪 Tester       : python3 tester.py
# ============================================================
munitions = 6

coups_tires = 0

while munitions > 0:
    coups_tires += 1
    munitions -= 1

tour = 0

patrouilles = 0

while tour < 4:
    patrouilles += 1
    tour += 1