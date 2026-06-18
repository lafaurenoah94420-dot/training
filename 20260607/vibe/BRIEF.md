# Nahla cache-cache — reste invisible

## Vision

Vue du dessus dans l'appart : Nahla se faufile entre les meubles. Des humains (Malik/Kays) patrouillent avec une zone de vue. Reste hors de leur champ de vision le plus longtemps possible — score = secondes cachées.

## Stack

Python 3 + pygame

## Feuille de route

1. ✅ Fenêtre + salon (sol, murs, meubles obstacles)
2. ✅ Nahla (sprite) + déplacement ZQSD / flèches
3. ✅ Malik patrouille + cône de vision
4. ✅ Détection + barre de stress
5. ✅ Meubles bloquent la ligne de vue
6. ✅ Timer 90s + score temps caché + record
7. ✅ Menu + fin de partie + R pour rejouer
8. ✅ Kays (2e garde, patrouille diagonale)
9. ✅ Croquettes (stress -, mode fantôme 2s)
10. ✅ Malik enquête sur dernière position vue
11. ✅ Répliques Nahla / Malik / Kays

## Lancer

```bash
cd 20260607/vibe && python3 main.py
```
