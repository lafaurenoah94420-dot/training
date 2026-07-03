# ============================================================
# Tester — Split et compter
# ============================================================
import sys

try:
    from main import compter_unites
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Vérifie que tu as bien défini la fonction compter_unites dans main.py")
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
    "trois divisions séparées par des virgules",
    compter_unites("infanterie,cavalerie,artillerie"),
    3,
)
_tester("une seule division", compter_unites("chars"), 1)
_tester("cinq divisions", compter_unites("inf,inf,cav,art,aviation"), 5)
_tester("texte vide — zéro division", compter_unites(""), 0)

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
