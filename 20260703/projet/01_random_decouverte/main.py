# ============================================================
# Exercice 1/6 — Butin aléatoire
# ============================================================
# 📁 Dossier      : cd /Users/noah/Desktop/Python/20260703/projet/01_random_decouverte
# 📄 Instructions : open /Users/noah/Desktop/Python/20260703/projet/01_random_decouverte/instructions.html
# 🧪 Tester       : python3 tester.py
# ============================================================
import random

armes = ["hache", "batte", "couteau"]

arme_trouvee = random.choice(armes)

nb_zombies = random.randint(2, 8)