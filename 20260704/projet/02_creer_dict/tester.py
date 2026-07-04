# ============================================================
# Tester — Créer un dictionnaire
# ============================================================
import sys

try:
    from main import equipage
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Crée le dictionnaire equipage dans main.py")
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


_tester("equipage a 3 membres", len(equipage), 3)
_tester("pilote vaut Franklin", equipage["pilote"], "Franklin")
_tester("braqueur vaut Michael", equipage["braqueur"], "Michael")
_tester("hacker vaut Lester", equipage["hacker"], "Lester")

_passes = sum(_resultats)
_total = len(_resultats)
print(f"\n{'─' * 40}")
print(f"  {_passes}/{_total} tests passés")
if _passes == _total:
    print("  🎉 Parfait !")
else:
    print(f"  {_total - _passes} test(s) à corriger.")
print('─' * 40)
