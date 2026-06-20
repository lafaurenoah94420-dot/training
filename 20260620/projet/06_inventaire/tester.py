# ============================================================
# Tester — Mini inventaire
# ============================================================
import sys

try:
    from main import ajouter, resume_inventaire
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
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


inv = []
inv = ajouter(inv, "batte")
inv = ajouter(inv, "hache")
inv = ajouter(inv, "batte")
_tester("après 3 ajouts", inv, ["batte", "hache", "batte"])
_tester("resume 3 objets", resume_inventaire(inv), "Inventaire : 3 objets")
_tester("resume vide", resume_inventaire([]), "Inventaire : 0 objets")

_passes = sum(_resultats)
_total = len(_resultats)
print(f"\n{'─' * 40}")
print(f"  {_passes}/{_total} tests passés")
if _passes == _total:
    print("  🎉 Parfait !")
else:
    print(f"  {_total - _passes} test(s) à corriger.")
print('─' * 40)
