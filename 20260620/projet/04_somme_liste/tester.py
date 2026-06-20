# ============================================================
# Tester — Total d'une liste
# ============================================================
import sys

try:
    from main import total_degats
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
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


_tester("total [10,20,5]", total_degats([10, 20, 5]), 35)
_tester("liste vide → 0", total_degats([]), 0)
_tester("un seul [40]", total_degats([40]), 40)

_passes = sum(_resultats)
_total = len(_resultats)
print(f"\n{'─' * 40}")
print(f"  {_passes}/{_total} tests passés")
if _passes == _total:
    print("  🎉 Parfait !")
else:
    print(f"  {_total - _passes} test(s) à corriger.")
print('─' * 40)
