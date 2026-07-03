# ============================================================
# Tester — While avec condition d'arrêt
# ============================================================
import sys

try:
    from main import tirs_necessaires
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Vérifie que tu as bien défini la fonction tirs_necessaires dans main.py")
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


# ---- Tests ----
_tester("tirs_necessaires(30, 10) → 3 tirs", tirs_necessaires(30, 10), 3)
_tester("tirs_necessaires(25, 10) → 3 tirs", tirs_necessaires(25, 10), 3)
_tester("tirs_necessaires(10, 15) → 1 tir", tirs_necessaires(10, 15), 1)
_tester("zombie déjà mort — 0 tir", tirs_necessaires(0, 5), 0)

# ---- Résultat ----
_passes = sum(_resultats)
_total = len(_resultats)
print(f"\n{'─' * 40}")
print(f"  {_passes}/{_total} tests passés")
if _passes == _total:
    print("  🎉 Parfait !")
else:
    print(f"  {_total - _passes} test(s) à corriger.")
print('─' * 40)
