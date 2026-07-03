# ============================================================
# Exercice 4/6 — Fonction avec while
# ============================================================
# 📁 Dossier      : cd /Users/noah/Desktop/Python/20260702/projet/04_fonction_while
# 📄 Instructions : open /Users/noah/Desktop/Python/20260702/projet/04_fonction_while/instructions.html
# 🧪 Tester       : python3 tester.py
# ============================================================
def missions_necessaires(xp_objectif, xp_par_mission):
    total = 0
    mission = 0
    while total < xp_objectif:
        total += xp_par_mission
        mission += 1
    return mission