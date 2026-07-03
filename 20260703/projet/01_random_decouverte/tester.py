# ============================================================
# Tester — Butin aléatoire
# ============================================================
import sys

try:
    from main import armes, arme_trouvee, nb_zombies
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Vérifie que tu as bien défini armes, arme_trouvee et nb_zombies dans main.py")
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


def _tester_vrai(description, condition):
    if condition:
        print(f"✅ {description}")
        _resultats.append(True)
    else:
        print(f"❌ {description}")
        _resultats.append(False)


# ---- Tests ----
_tester_vrai("armes contient au moins une arme", isinstance(armes, list) and len(armes) >= 1)
_tester_vrai("arme_trouvee est bien dans la liste armes", arme_trouvee in armes)
_tester_vrai("nb_zombies est entre 2 et 8", 2 <= nb_zombies <= 8)
_tester_vrai("nb_zombies est un nombre entier", isinstance(nb_zombies, int))

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
