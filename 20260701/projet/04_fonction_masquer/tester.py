# ============================================================
# Tester — Fonction masquer
# ============================================================
import sys

try:
    from main import masquer_mot
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Vérifie que tu as bien défini la fonction masquer_mot dans main.py")
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
    "un seul mot masqué",
    masquer_mot("zombie dans la cuisine", "zombie"),
    "*** dans la cuisine",
)
_tester(
    "deux occurrences masquées",
    masquer_mot("zombie et zombie", "zombie"),
    "*** et ***",
)
_tester(
    "mot absent — texte inchangé",
    masquer_mot("cuisine propre", "zombie"),
    "cuisine propre",
)
_tester("texte vide", masquer_mot("", "zombie"), "")

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
