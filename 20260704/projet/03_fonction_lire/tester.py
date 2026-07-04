# ============================================================
# Tester — Lire avec une fonction
# ============================================================
import sys

try:
    from main import lire_stock
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Définis la fonction lire_stock dans main.py")
    sys.exit(1)

_resultats = []

STOCKS = {
    "munitions": 12,
    "medkit": 2,
    "bouteille": 1,
}


def _tester(description, obtenu, attendu):
    if obtenu == attendu:
        print(f"✅ {description}")
        _resultats.append(True)
    else:
        print(f"❌ {description}")
        print(f"   Attendu : {attendu!r}")
        print(f"   Obtenu  : {obtenu!r}")
        _resultats.append(False)


_tester("lire_stock munitions → 12", lire_stock(STOCKS, "munitions"), 12)
_tester("lire_stock medkit → 2", lire_stock(STOCKS, "medkit"), 2)
_tester("lire_stock bouteille → 1", lire_stock(STOCKS, "bouteille"), 1)
_tester(
    "lire_stock sur un autre stock",
    lire_stock({"clous": 30, "planches": 8}, "clous"),
    30,
)

_passes = sum(_resultats)
_total = len(_resultats)
print(f"\n{'─' * 40}")
print(f"  {_passes}/{_total} tests passés")
if _passes == _total:
    print("  🎉 Parfait !")
else:
    print(f"  {_total - _passes} test(s) à corriger.")
print('─' * 40)
