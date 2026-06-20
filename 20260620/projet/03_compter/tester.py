# ============================================================
# Tester — Compter dans une liste
# ============================================================
import sys

try:
    from main import compter_type
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


types = ["coureur", "Tank", "coureur", "rapide", "coureur"]
_tester("3 coureurs", compter_type(types, "coureur"), 3)
_tester("1 Tank", compter_type(types, "Tank"), 1)
_tester("0 mega", compter_type(types, "mega"), 0)

_passes = sum(_resultats)
_total = len(_resultats)
print(f"\n{'─' * 40}")
print(f"  {_passes}/{_total} tests passés")
if _passes == _total:
    print("  🎉 Parfait !")
else:
    print(f"  {_total - _passes} test(s) à corriger.")
print('─' * 40)
