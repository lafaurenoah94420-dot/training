# ============================================================
# Tester — return
# ============================================================
import sys

try:
    from main import munitions_restantes
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Vérifie que tu as bien défini la fonction munitions_restantes dans main.py")
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
_tester("munitions_restantes(30, 10) → 20", munitions_restantes(30, 10), 20)
_tester("munitions_restantes(5, 5) → 0", munitions_restantes(5, 5), 0)
_tester("munitions_restantes(3, 10) → 0 (pas négatif)", munitions_restantes(3, 10), 0)
_tester("munitions_restantes(0, 0) → 0", munitions_restantes(0, 0), 0)

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
