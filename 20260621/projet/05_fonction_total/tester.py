# ============================================================
# Tester — Totaliser les valeurs
# ============================================================
import sys

try:
    from main import total_ressources
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Définis la fonction total_ressources dans main.py")
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


_tester("total HOI4 → 18", total_ressources({"acier": 10, "caoutchouc": 5, "petrole": 3}), 18)
_tester("total vide → 0", total_ressources({}), 0)
_tester("total un type → 7", total_ressources({"munitions": 7}), 7)

_passes = sum(_resultats)
_total = len(_resultats)
print(f"\n{'─' * 40}")
print(f"  {_passes}/{_total} tests passés")
if _passes == _total:
    print("  🎉 Parfait !")
else:
    print(f"  {_total - _passes} test(s) à corriger.")
print('─' * 40)
