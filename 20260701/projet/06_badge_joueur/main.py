# ============================================================
# Exercice 6/6 — Badge joueur
# ============================================================
# 📁 Dossier      : cd /Users/noah/Desktop/Python/20260701/projet/06_badge_joueur
# 📄 Instructions : open /Users/noah/Desktop/Python/20260701/projet/06_badge_joueur/instructions.html
# 🧪 Tester       : python3 tester.py
# ============================================================
def creer_badge(pseudo, niveau, clan):
    clan_maj = clan.upper()
    pseudo_maj = pseudo.upper()
    return f"[{clan_maj}] {pseudo_maj} — Niv. {niveau}"