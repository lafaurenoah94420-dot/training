# ============================================================
# Tester — Combat aléatoire
# ============================================================
import sys

try:
    from main import compter_tirs
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Vérifie que tu as bien défini la fonction compter_tirs dans main.py")
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


def _tester_vrai(description, condition):
    if condition:
        print(f"✅ {description}")
        _resultats.append(True)
    else:
        print(f"❌ {description}")
        _resultats.append(False)


# ---- Tests ----
_tester_vrai(
    "compter_tirs(100, 10, 20) retourne entre 5 et 10 tirs",
    5 <= compter_tirs(100, 10, 20) <= 10,
)
_tester("compter_tirs(15, 5, 5) → 3 tirs", compter_tirs(15, 5, 5), 3)
_tester("compter_tirs(0, 5, 5) → 0 tirs", compter_tirs(0, 5, 5), 0)
_tester("compter_tirs(5, 5, 5) → 1 tir", compter_tirs(5, 5, 5), 1)

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
