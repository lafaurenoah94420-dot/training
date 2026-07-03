# ============================================================
# Exercice 2/6 — Remplacer dans un texte
# ============================================================
# 📁 Dossier      : cd /Users/noah/Desktop/Python/20260701/projet/02_replace
# 📄 Instructions : open /Users/noah/Desktop/Python/20260701/projet/02_replace/instructions.html
# 🧪 Tester       : python3 tester.py
# ============================================================
rapport = "Umbrella a perdu le contrôle du T-Virus à Raccoon City"

code = "STARS-007"

rapport_censure = rapport.replace("Umbrella", "[CENSURÉ]")

code_masque = code.replace("007", "███")