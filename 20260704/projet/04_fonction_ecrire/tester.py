# ============================================================
# Tester — Écrire dans un dictionnaire
# ============================================================
import sys

try:
    from main import ajouter
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Définis la fonction ajouter dans main.py")
    sys.exit(1)

_resultats = []


def _tester(description, obtenu, attendu):
    if obtenu == attendu:
        print(f"✅ {description}")
        _resultats.append(True)
    else:
        print(f"❌ {description}")
        print(f"   Attendu : {attendu!r}")
        print(f"   Obtenu  : {obtenu!r}")
        _resultats.append(False)


stocks1 = {"nourriture": 5, "eau": 2}
ajouter(stocks1, "nourriture", 3)
_tester("ajouter nourriture +3 → 8", stocks1["nourriture"], 8)

stocks2 = {"eau": 10}
ajouter(stocks2, "eau", 5)
_tester("ajouter eau +5 → 15", stocks2["eau"], 15)

stocks3 = {"bandage": 1}
ajouter(stocks3, "bandage", 0)
_tester("ajouter zéro ne change rien", stocks3["bandage"], 1)

stocks4 = {"clous": 20, "planches": 8}
ajouter(stocks4, "planches", 4)
_tester("ajouter planches +4 → 12", stocks4["planches"], 12)

_passes = sum(_resultats)
_total = len(_resultats)
print(f"\n{'─' * 40}")
print(f"  {_passes}/{_total} tests passés")
if _passes == _total:
    print("  🎉 Parfait !")
else:
    print(f"  {_total - _passes} test(s) à corriger.")
print('─' * 40)
