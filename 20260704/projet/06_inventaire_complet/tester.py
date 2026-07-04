# ============================================================
# Tester — Inventaire complet
# ============================================================
import sys

try:
    from main import initialiser, ramasser, afficher_total
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Définis initialiser, ramasser et afficher_total dans main.py")
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


inv_init = initialiser()
_tester(
    "initialiser retourne 3 objets",
    inv_init,
    {"conserve": 2, "marteau": 1, "bandage": 3},
)

inv_ramasser = {"conserve": 2, "marteau": 1, "bandage": 3}
ramasser(inv_ramasser, "conserve", 4)
_tester("ramasser ajoute 4 conserves → 6", inv_ramasser["conserve"], 6)

_tester(
    "afficher_total sur inventaire de départ",
    afficher_total({"conserve": 2, "marteau": 1, "bandage": 3}),
    6,
)
_tester("afficher_total sur inventaire vide", afficher_total({}), 0)

inv_complet = initialiser()
ramasser(inv_complet, "bandage", 2)
_tester(
    "scénario complet : init + ramasser + total",
    afficher_total(inv_complet),
    8,
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
