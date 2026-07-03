# ============================================================
# Tester — Fonction majuscules
# ============================================================
import sys

try:
    from main import crier_rue
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Vérifie que tu as bien défini la fonction crier_rue dans main.py")
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
_tester("crier_rue('franklin') → 'FRANKLIN'", crier_rue("franklin"), "FRANKLIN")
_tester("crier_rue('trevor') → 'TREVOR'", crier_rue("trevor"), "TREVOR")
_tester("crier_rue('cj') → 'CJ'", crier_rue("cj"), "CJ")
_tester("crier_rue('') → texte vide", crier_rue(""), "")

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
