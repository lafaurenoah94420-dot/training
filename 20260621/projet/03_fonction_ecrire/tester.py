# ============================================================
# Tester — Écrire dans un dictionnaire
# ============================================================
import sys

try:
    from main import mettre_a_jour
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Définis la fonction mettre_a_jour dans main.py")
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


stock = {"haricots": 2}
mettre_a_jour(stock, "haricots", 5)
_tester("haricots mis à jour → 5", stock["haricots"], 5)

mettre_a_jour(stock, "eau", 3)
_tester("eau ajoutée → 3", stock["eau"], 3)

mettre_a_jour(stock, "bandage", 1)
_tester("bandage ajouté → 1", stock["bandage"], 1)

_passes = sum(_resultats)
_total = len(_resultats)
print(f"\n{'─' * 40}")
print(f"  {_passes}/{_total} tests passés")
if _passes == _total:
    print("  🎉 Parfait !")
else:
    print(f"  {_total - _passes} test(s) à corriger.")
print('─' * 40)
