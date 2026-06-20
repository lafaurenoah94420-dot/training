# ============================================================
# Tester — Présence et position
# ============================================================
import sys

try:
    from main import contient, index_de
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


inv = ["eau", "conserve", "bandage", "eau"]
_tester("contient eau", contient(inv, "eau"), True)
_tester("contient fusil", contient(inv, "fusil"), False)
_tester("index eau → 0", index_de(inv, "eau"), 0)
_tester("index bandage → 2", index_de(inv, "bandage"), 2)
_tester("index absent → -1", index_de(inv, "croquette"), -1)

_passes = sum(_resultats)
_total = len(_resultats)
print(f"\n{'─' * 40}")
print(f"  {_passes}/{_total} tests passés")
if _passes == _total:
    print("  🎉 Parfait !")
else:
    print(f"  {_total - _passes} test(s) à corriger.")
print('─' * 40)
