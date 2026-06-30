# ============================================================
# Tester — Lire un dictionnaire
# ============================================================
import sys

try:
    from main import verts, bleues, total_types, soins
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Crée soins, verts, bleues et total_types dans main.py")
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


_tester("verts vaut 3", verts, 3)
_tester("bleues vaut 1", bleues, 1)
_tester("total_types vaut 3", total_types, 3)

_passes = sum(_resultats)
_total = len(_resultats)
print(f"\n{'─' * 40}")
print(f"  {_passes}/{_total} tests passés")
if _passes == _total:
    print("  🎉 Parfait !")
else:
    print(f"  {_total - _passes} test(s) à corriger.")
print('─' * 40)
