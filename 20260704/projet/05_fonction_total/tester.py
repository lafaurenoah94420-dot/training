# ============================================================
# Tester — Total des unités
# ============================================================
import sys

try:
    from main import total_unites
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Définis la fonction total_unites dans main.py")
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


_tester(
    "total infanterie + tanks + aviations",
    total_unites({"infanterie": 100, "tanks": 20, "aviations": 5}),
    125,
)
_tester("total d'un seul type", total_unites({"infanterie": 50}), 50)
_tester("total d'un dictionnaire vide", total_unites({}), 0)
_tester(
    "total avec des zéros",
    total_unites({"infanterie": 0, "tanks": 10, "aviations": 0}),
    10,
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
