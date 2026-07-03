# ============================================================
# Tester — Tir aléatoire
# ============================================================
import sys

try:
    from main import tirer_degats
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Vérifie que tu as bien défini la fonction tirer_degats dans main.py")
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


def _tester_plage(description, min_val, max_val, nb_appels=20):
    echecs = []
    for _ in range(nb_appels):
        obtenu = tirer_degats(min_val, max_val)
        if not (min_val <= obtenu <= max_val):
            echecs.append(obtenu)
    if not echecs:
        print(f"✅ {description}")
        _resultats.append(True)
    else:
        print(f"❌ {description}")
        print(f"   Valeurs hors plage : {echecs[:3]}")
        _resultats.append(False)


# ---- Tests ----
_tester_plage("tirer_degats(10, 20) reste entre 10 et 20", 10, 20)
_tester_plage("tirer_degats(1, 5) reste entre 1 et 5", 1, 5)
_tester_plage("tirer_degats(30, 30) retourne toujours 30", 30, 30)
_tester("tirer_degats(0, 0) → 0", tirer_degats(0, 0), 0)

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
