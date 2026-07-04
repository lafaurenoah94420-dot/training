# ============================================================
# Tester — Lire un dictionnaire
# ============================================================
import sys

try:
    from main import soins, spray, herbes, nb_types
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Crée soins, spray, herbes et nb_types dans main.py")
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


_tester("soins contient la clé spray", "spray" in soins, True)
_tester("spray vaut 2", spray, 2)
_tester("herbes vaut 4", herbes, 4)
_tester("nb_types vaut 3", nb_types, 3)

_passes = sum(_resultats)
_total = len(_resultats)
print(f"\n{'─' * 40}")
print(f"  {_passes}/{_total} tests passés")
if _passes == _total:
    print("  🎉 Parfait !")
else:
    print(f"  {_total - _passes} test(s) à corriger.")
print('─' * 40)
