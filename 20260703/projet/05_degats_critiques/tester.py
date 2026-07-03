# ============================================================
# Tester — Dégâts critiques
# ============================================================
import math
import sys

try:
    from main import degats_finaux
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Vérifie que tu as bien défini la fonction degats_finaux dans main.py")
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


def _tester_plage(description, base, bonus_min, bonus_max, nb_appels=30):
    minimum = math.floor(base) + bonus_min
    maximum = math.floor(base) + bonus_max
    echecs = []
    for _ in range(nb_appels):
        obtenu = degats_finaux(base, bonus_min, bonus_max)
        if not (minimum <= obtenu <= maximum):
            echecs.append(obtenu)
    if not echecs:
        print(f"✅ {description}")
        _resultats.append(True)
    else:
        print(f"❌ {description}")
        print(f"   Plage attendue : {minimum} à {maximum}")
        print(f"   Valeurs hors plage : {echecs[:3]}")
        _resultats.append(False)


# ---- Tests ----
_tester_plage(
    "degats_finaux(47.8, 5, 15) reste dans la bonne plage",
    47.8, 5, 15,
)
_tester_plage(
    "degats_finaux(10.2, 0, 3) reste dans la bonne plage",
    10.2, 0, 3,
)
_tester(
    "bonus fixe — degats_finaux(20.9, 4, 4) → 24",
    degats_finaux(20.9, 4, 4),
    24,
)

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
