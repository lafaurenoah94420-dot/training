# ============================================================
# Tester — Mini programme complet
# ============================================================
import sys

try:
    from main import rapport_nuit, evaluer_nuit
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Vérifie que tu as bien défini rapport_nuit et evaluer_nuit dans main.py")
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
    "rapport_nuit zone + infectés",
    rapport_nuit("Garage", 12),
    "Zone Garage — 12 infectés repérés",
)
_tester(
    "rapport_nuit autre zone",
    rapport_nuit("Cuisine", 3),
    "Zone Cuisine — 3 infectés repérés",
)
_tester("evaluer_nuit(8) → Tendu", evaluer_nuit(8), "Tendu")
_tester("evaluer_nuit(3) → Calme", evaluer_nuit(3), "Calme")
_tester("evaluer_nuit(22) → Critique", evaluer_nuit(22), "Critique")

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
