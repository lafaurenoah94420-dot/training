# ============================================================
# Exercice 3/6 — While avec condition d'arrêt
# ============================================================
# 📁 Dossier      : cd /Users/noah/Desktop/Python/20260702/projet/03_while_condition
# 📄 Instructions : open /Users/noah/Desktop/Python/20260702/projet/03_while_condition/instructions.html
# 🧪 Tester       : python3 tester.py
# ============================================================
def tirs_necessaires(vie_zombie, degats_par_tir):
    tirs = 0
    while vie_zombie > 0:
        vie_zombie -= degats_par_tir
        tirs += 1
    return tirs