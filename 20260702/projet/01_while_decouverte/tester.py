# ============================================================
# Tester — Boucle while, découverte
# ============================================================
import sys

try:
    from main import coups_tires, patrouilles
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Définis coups_tires et patrouilles dans main.py")
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
_tester("coups_tires vaut 6 après avoir vidé le chargeur", coups_tires, 6)
_tester("patrouilles vaut 4 après quatre tours de garde", patrouilles, 4)

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
