# ============================================================
# Tester — Lire avec une fonction
# ============================================================
import sys

try:
    from main import prix_infraction
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Définis la fonction prix_infraction dans main.py")
    sys.exit(1)

_resultats = []

TABLE = {
    "stationnement": 80,
    "exces_vitesse": 250,
    "feu_rouge": 135,
}


def _tester(description, obtenu, attendu):
    if obtenu == attendu:
        print(f"✅ {description}")
        _resultats.append(True)
    else:
        print(f"❌ {description}")
        print(f"   Attendu : {attendu!r}")
        print(f"   Obtenu  : {obtenu!r}")
        _resultats.append(False)


_tester("prix_infraction exces_vitesse → 250", prix_infraction(TABLE, "exces_vitesse"), 250)
_tester("prix_infraction stationnement → 80", prix_infraction(TABLE, "stationnement"), 80)
_tester("prix_infraction feu_rouge → 135", prix_infraction(TABLE, "feu_rouge"), 135)

_passes = sum(_resultats)
_total = len(_resultats)
print(f"\n{'─' * 40}")
print(f"  {_passes}/{_total} tests passés")
if _passes == _total:
    print("  🎉 Parfait !")
else:
    print(f"  {_total - _passes} test(s) à corriger.")
print('─' * 40)
