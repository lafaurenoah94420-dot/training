# ============================================================
# Tester — Deux fonctions ensemble
# ============================================================
import sys

try:
    from main import est_critique, statut_vie
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Vérifie que tu as bien défini est_critique et statut_vie dans main.py")
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


# ---- Tests ----
_tester("est_critique(15) → True", est_critique(15), True)
_tester("est_critique(50) → False", est_critique(50), False)
_tester("est_critique(20) → True (seuil inclus)", est_critique(20), True)
_tester("statut_vie(15) → CRITIQUE", statut_vie(15), "CRITIQUE")
_tester("statut_vie(80) → OK", statut_vie(80), "OK")

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
