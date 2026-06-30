# ============================================================
# Tester — Résumé d'inventaire
# ============================================================
import sys

try:
    from main import resume_inventaire
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Définis la fonction resume_inventaire dans main.py")
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
    "résumé armoire RPD",
    resume_inventaire({"spray": 2, "herbe_verte": 3, "munitions": 5}),
    "Inventaire : 3 types, 10 objets",
)
_tester(
    "résumé un seul type",
    resume_inventaire({"spray": 1}),
    "Inventaire : 1 types, 1 objets",
)
_tester(
    "résumé vide",
    resume_inventaire({}),
    "Inventaire : 0 types, 0 objets",
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
