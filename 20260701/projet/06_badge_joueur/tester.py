# ============================================================
# Tester — Badge joueur
# ============================================================
import sys

try:
    from main import creer_badge
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Vérifie que tu as bien défini la fonction creer_badge dans main.py")
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
_tester(
    "badge Franklin des Ballas",
    creer_badge("franklin", 42, "ballas"),
    "[BALLAS] FRANKLIN — Niv. 42",
)
_tester(
    "badge Ellie niveau 1",
    creer_badge("ellie", 1, "fireflies"),
    "[FIREFLIES] ELLIE — Niv. 1",
)
_tester(
    "badge niveau 100",
    creer_badge("leon", 100, "stars"),
    "[STARS] LEON — Niv. 100",
)
_tester(
    "pseudo déjà en majuscules",
    creer_badge("CJ", 50, "grove"),
    "[GROVE] CJ — Niv. 50",
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
