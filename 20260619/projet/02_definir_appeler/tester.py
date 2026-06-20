# ============================================================
# Tester — Ta première fonction
# ============================================================
import sys

try:
    from main import titre_jeu
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Vérifie que tu as bien défini la fonction titre_jeu dans main.py")
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
_tester("titre_jeu() retourne le bon texte", titre_jeu(), "Project Zomboid — Veille de nuit")
_tester("titre_jeu est bien une fonction", callable(titre_jeu), True)

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
