# Nahla vs le laser — chase & combo

Nahla traque un (ou deux) lasers dans le salon. Combo, griffures, dash, ronron, Malik, canapé refuge.

**Lancer :**
```bash
cd 20260606/vibe && python3 main.py
```

**Menu**
- **← / →** — difficulté Normal / Difficile
- **↑ / ↓** — mode Chrono (90s) / Infini
- **Entrée / Espace** — jouer

**Contrôles en jeu**
- **ZQSD / flèches** — bouger
- **Espace** — dash (cooldown)
- **F** — ronron : fige les lasers 1 s (cooldown)
- **Échap** — quitter (en mode Infini : fin de partie + grade)
- **R** — retour menu après la partie

**Features**
- 2e laser après 30 s · boss laser géant les 10 dernières secondes (chrono)
- Croquettes au sol : +score et dash recharge plus vite
- Combo &gt; 30 : laser se split en 2 mini lasers si tu le tiens assez longtemps
- Zones dorées sur le tapis : score x2 pendant 5 s
- Traînée rouge · canapé refuge · Malik · sons · 4 tailles Nahla
- Barre combo · grades · record dans `highscore.json`
