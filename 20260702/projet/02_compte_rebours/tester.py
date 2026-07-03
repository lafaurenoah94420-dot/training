# ============================================================
# Tester — Compte à rebours
# ============================================================
import sys

try:
    from main import compte_rebours
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Vérifie que tu as bien défini la fonction compte_rebours dans main.py")
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
_tester("compte_rebours(5) retourne 0", compte_rebours(5), 0)
_tester("compte_rebours(1) retourne 0", compte_rebours(1), 0)
_tester("compte_rebours(0) retourne 0 sans boucle", compte_rebours(0), 0)
_tester("compte_rebours(10) retourne 0", compte_rebours(10), 0)

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
