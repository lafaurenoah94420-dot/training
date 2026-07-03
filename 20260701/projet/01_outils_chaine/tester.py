# ============================================================
# Tester — Outils sur une chaîne
# ============================================================
import sys

try:
    from main import nom_cri, nom_chuchote, taille_nom
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Définis nom_cri, nom_chuchote et taille_nom dans main.py")
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
_tester("nom_cri vaut 'CLICKER'", nom_cri, "CLICKER")
_tester("nom_chuchote vaut 'fedra'", nom_chuchote, "fedra")
_tester("taille_nom vaut 7", taille_nom, 7)

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
