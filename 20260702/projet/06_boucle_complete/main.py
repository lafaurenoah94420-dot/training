# ============================================================
# Exercice 6/6 — Boucle complète
# ============================================================
# 📁 Dossier      : cd /Users/noah/Desktop/Python/20260702/projet/06_boucle_complete
# 📄 Instructions : open /Users/noah/Desktop/Python/20260702/projet/06_boucle_complete/instructions.html
# 🧪 Tester       : python3 tester.py
# ============================================================
def raid_final(vie, vagues):
    i = 0
    reussis = 0
    while i < len(vagues):
        if vagues[i] <= 0:
             i += 1
             continue
        vie = vie - vagues[i]
        if vie <= 0:
            vie =0
            break
        reussis += 1
        i += 1
    return (vie, reussis)