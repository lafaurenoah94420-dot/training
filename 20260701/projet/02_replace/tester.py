# ============================================================
# Tester — Remplacer dans un texte
# ============================================================
import sys

try:
    from main import rapport_censure, code_masque
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Définis rapport_censure et code_masque dans main.py")
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
    "Umbrella remplacé par [CENSURÉ]",
    rapport_censure,
    "[CENSURÉ] a perdu le contrôle du T-Virus à Raccoon City",
)
_tester("007 remplacé par ███", code_masque, "STARS-███")
_tester("le mot Umbrella a disparu du rapport", "Umbrella" not in rapport_censure, True)

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
