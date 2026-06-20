# ============================================================
# Tester — Outils sur une liste
# ============================================================
import sys

try:
    from main import nombre_armes, degat_max, premier_arme
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Définis nombre_armes, degat_max et premier_arme dans main.py")
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


_tester("nombre_armes vaut 5", nombre_armes, 5)
_tester("degat_max vaut 95", degat_max, 95)
_tester("premier_arme vaut 'batte'", premier_arme, "batte")

_passes = sum(_resultats)
_total = len(_resultats)
print(f"\n{'─' * 40}")
print(f"  {_passes}/{_total} tests passés")
if _passes == _total:
    print("  🎉 Parfait !")
else:
    print(f"  {_total - _passes} test(s) à corriger.")
print('─' * 40)
