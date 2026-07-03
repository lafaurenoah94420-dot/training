# ============================================================
# Tester — Boucle complète
# ============================================================
import sys

try:
    from main import raid_final
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Vérifie que tu as bien défini la fonction raid_final dans main.py")
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
    "trois vagues réussies, 10 PV restants",
    raid_final(100, [30, 40, 20]),
    (10, 3),
)
_tester(
    "mort à la troisième vague",
    raid_final(100, [30, 40, 35]),
    (0, 2),
)
_tester(
    "vague vide ignorée avec continue",
    raid_final(50, [0, 10, 20]),
    (20, 2),
)
_tester(
    "aucune vague — vie intacte",
    raid_final(80, []),
    (80, 0),
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
