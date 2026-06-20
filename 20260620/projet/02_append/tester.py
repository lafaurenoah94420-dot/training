# ============================================================
# Tester — Construire une liste
# ============================================================
import sys

try:
    from main import infectes_vus
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Définis infectes_vus dans main.py")
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


_tester("liste complète", infectes_vus, ["coureur", "coureur", "Tank", "coureur"])
_tester("longueur 4", len(infectes_vus), 4)

_passes = sum(_resultats)
_total = len(_resultats)
print(f"\n{'─' * 40}")
print(f"  {_passes}/{_total} tests passés")
if _passes == _total:
    print("  🎉 Parfait !")
else:
    print(f"  {_total - _passes} test(s) à corriger.")
print('─' * 40)
