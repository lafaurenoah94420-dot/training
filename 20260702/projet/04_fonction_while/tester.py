# ============================================================
# Tester — Fonction avec while
# ============================================================
import sys

try:
    from main import missions_necessaires
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Vérifie que tu as bien défini la fonction missions_necessaires dans main.py")
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
_tester("missions_necessaires(100, 30) → 4 missions", missions_necessaires(100, 30), 4)
_tester("missions_necessaires(100, 50) → 2 missions", missions_necessaires(100, 50), 2)
_tester("objectif déjà atteint — 0 mission", missions_necessaires(0, 10), 0)
_tester("missions_necessaires(15, 10) → 2 missions", missions_necessaires(15, 10), 2)

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
