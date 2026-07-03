# ============================================================
# Tester — Distance sur la carte
# ============================================================
import sys

try:
    from main import distance_entre
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Vérifie que tu as bien défini la fonction distance_entre dans main.py")
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
_tester("distance_entre(0, 0, 3, 4) → 5", distance_entre(0, 0, 3, 4), 5)
_tester("distance_entre(0, 0, 0, 0) → 0", distance_entre(0, 0, 0, 0), 0)
_tester("distance_entre(1, 1, 4, 5) → 5", distance_entre(1, 1, 4, 5), 5)
_tester("distance_entre(0, 0, 10, 0) → 10", distance_entre(0, 0, 10, 0), 10)

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
