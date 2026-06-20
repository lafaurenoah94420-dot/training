# ============================================================
# Tester — Fonction avec paramètres
# ============================================================
import sys

try:
    from main import alerte_zone
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Vérifie que tu as bien défini la fonction alerte_zone dans main.py")
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
_tester("alerte_zone('Garage', 3)", alerte_zone("Garage", 3), "Zone Garage — danger 3/5")
_tester("alerte_zone('Cuisine', 1)", alerte_zone("Cuisine", 1), "Zone Cuisine — danger 1/5")
_tester("alerte_zone('Toit', 5)", alerte_zone("Toit", 5), "Zone Toit — danger 5/5")

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
