# ============================================================
# Tester — Vérifier une clé
# ============================================================
import sys

try:
    from main import a_objet
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Définis la fonction a_objet dans main.py")
    sys.exit(1)

_resultats = []

SACOCHE = {
    "bandages": 0,
    "munitions": 12,
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


_tester("bandages présent → True", a_objet(SACOCHE, "bandages"), True)
_tester("antidote absent → False", a_objet(SACOCHE, "antidote"), False)
_tester("munitions présent → True", a_objet(SACOCHE, "munitions"), True)

_passes = sum(_resultats)
_total = len(_resultats)
print(f"\n{'─' * 40}")
print(f"  {_passes}/{_total} tests passés")
if _passes == _total:
    print("  🎉 Parfait !")
else:
    print(f"  {_total - _passes} test(s) à corriger.")
print('─' * 40)
