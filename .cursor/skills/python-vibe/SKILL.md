---
name: python-vibe
description: Session vibe coding. L'agent choisit un projet ambitieux (jeu 2D, simulation, outil visuel…) avec toutes les specs techniques. Noah pilote une IA par ses prompts pour construire quelque chose d'impressionnant — sans écrire de code lui-même. L'objectif : apprendre à penser, prompter et créer avec l'IA. Utilise quand l'utilisateur dit /python-vibe.
---

# Python Vibe

Session vibe coding. Noah ne code pas — il **dirige**. Il prompt une IA (Cursor, ChatGPT, Claude) pour construire quelque chose d'ambitieux et d'impressionnant. L'agent choisit le projet, la stack, les specs. Noah n'a qu'à pousser aussi loin que possible dans sa créativité.

**Une seule règle : aller le plus loin possible. Le reste, c'est l'IA qui s'en charge.**

**Durée : ~1h, pas de limite.**

---

## Gestion silencieuse (invisible pour le learner)

Tout ce qui suit se fait en arrière-plan, sans jamais en parler à Noah.

**Structure du jour :** le dossier va dans `YYYYMMDD/vibe/` à la racine du repo.

**Après le débrief :**
1. Appender la section `## Vibe` dans `YYYYMMDD/recap.md`
2. `git add -A && git commit -m "YYYYMMDD vibe" && git push origin main` (silencieux)

**Format de la section recap :**
```
## Vibe
projet : [titre]
stack : [ce que l'agent a choisi comme techno]
jusqu'où : [ce que Noah a réussi à construire]
prompts qui ont marché : [1-2 exemples de prompts efficaces]
notes : [observations sur sa façon de prompter]
```

**Règle absolue : ne jamais prononcer les mots git, GitHub, commit, push, recap devant le learner.**

---

## Workflow

### Étape 0 — Choisir le projet

L'agent choisit **seul** un projet parmi la banque ci-dessous (ou une variante originale). Il sélectionne aussi la **stack technique** sans demander l'avis de Noah.

**Règles de choix :**
- Le projet doit être **visuellement impressionnant** ou **techniquement bluffant** — quelque chose qui donne envie de montrer à ses amis
- Pas de mini-apps, pas de calculatrices, pas de programmes en console basiques
- Varier les types entre les sessions (ne pas reproposer la même catégorie deux fois d'affilée)
- La stack doit être **accessible depuis Cursor** : Python avec pygame / tkinter, HTML/CSS/JS vanilla, ou Python terminal avancé (curses, rich) — pas de frameworks complexes qui nécessitent 2h de setup

**Banque de projets (varier à chaque session) :**

- **Jeu 2D pygame** : platformer, shooter spatial, snake amélioré avec obstacles, tower defense, casse-briques avec power-ups, jeu de voiture en vue de dessus
- **Simulation pygame** : simulation de fourmis (stigmergie), boids (nuée d'oiseaux), feu de forêt qui se propage, automate cellulaire (Game of Life), évolution de créatures
- **Outil visuel pygame** : générateur de fractales interactif, visualiseur de tri en temps réel (bulles, rapide, fusion), simulateur de gravité avec des planètes
- **Site web** : page perso dark/neon avec animations CSS, jeu dans le navigateur (canvas JS), générateur de cartes de profil stylées, tableau de bord fictif animé
- **Terminal visuel (rich/curses)** : dashboard de monitoring fictif animé, visualiseur de données ASCII en temps réel, jeu de rôle textuel avec interface soignée

### Étape 1 — Briefing

Présenter le projet à Noah avec :
1. **Le titre** — accrocheur et concret
2. **Ce que ça fait** — 3-4 phrases qui donnent envie, avec des détails visuels précis (couleurs, animations, ce qu'on voit à l'écran)
3. **La stack choisie** — annoncée simplement : « tu vas coder ça en Python avec pygame » ou « c'est un site HTML/CSS/JS »
4. **Le dossier de travail** — `YYYYMMDD/vibe/`
5. **Le premier prompt à tester** — une seule phrase de départ concrète que Noah peut coller dans l'IA pour commencer (pas un plan, juste le déclencheur initial)

Format :
```
🎮  VIBE — [Titre du projet]

[3-4 phrases d'accroche visuelles et concrètes. Ce qu'on voit à l'écran, les animations, le sentiment quand ça tourne.]

Stack : [techno choisie par l'agent]
Dossier : YYYYMMDD/vibe/

Pour démarrer, colle ce prompt dans Cursor (ou l'IA de ton choix) :

"[Un prompt de départ précis, ambitieux, en français ou anglais selon ce qui marche mieux pour la techno]"

Ensuite c'est toi. Pousse aussi loin que tu veux.
Dis-moi ce que t'as réussi à faire ou ce qui bloque.
```

### Étape 2 — Pendant la session

Noah est en autonomie. L'agent intervient **uniquement si Noah le demande**, et de façon minimaliste :

- **Si Noah est bloqué sur un prompt** → l'agent propose une reformulation plus précise (pas du code, juste une meilleure façon de demander à l'IA)
- **Si Noah veut ajouter une feature** → l'agent suggère comment la décrire à l'IA en une phrase
- **Si Noah ne sait pas quoi faire ensuite** → l'agent propose 2-3 directions créatives très concrètes (« tu pourrais demander à l'IA d'ajouter des explosions quand les fourmis se croisent »)
- **Jamais** : expliquer du code, corriger du code, écrire du code, entrer dans les détails techniques

### Étape 3 — Débrief

Quand Noah dit qu'il a fini (ou arrêté), demander :
- Une capture ou description de ce qu'il a construit
- Le prompt qui a le mieux fonctionné

Feedback court (5 lignes max) :
- Ce qu'il a réussi à construire depuis zéro avec des prompts
- La qualité de ses prompts (trop vague ? trop précis ? bien ciblés ?)
- Une technique de prompting à retenir pour la prochaine fois

Ensuite, silencieusement : appender `## Vibe` dans `YYYYMMDD/recap.md` et git push.

---

## Banque de premiers prompts (exemples)

Pour une **simulation de fourmis pygame** :
> "Create a Python pygame simulation of an ant colony using stigmergy. Ants leave pheromone trails that evaporate over time. When an ant finds food, it returns to the nest leaving a strong trail. Other ants follow the strongest trail. Start with 100 ants, a nest in the center, and 5 food sources randomly placed. Show pheromone trails as colored gradients."

Pour un **jeu de tir spatial pygame** :
> "Create a pygame space shooter. The player controls a spaceship at the bottom, shoots upward, enemies come in waves from the top. Add particle explosions when enemies die, a score counter, and make the background a scrolling starfield. Start simple and make it feel juicy."

Pour une **simulation Game of Life pygame** :
> "Create Conway's Game of Life in pygame. The grid should be 100x100 cells, display in a 800x800 window. Add controls: Space to pause/resume, R to randomize, C to clear. Show a generation counter. Make alive cells bright green on black background. Add a speed slider."

Pour un **site perso dark/neon** :
> "Create a personal portfolio page with a dark cyberpunk aesthetic. Neon green and purple colors, animated glitch effect on the title, smooth scroll between sections (About, Projects, Contact). Add a typing animation on the hero text. Make it look like something from a hacker movie."

Pour un **visualiseur de tri pygame** :
> "Create a sorting visualizer in pygame. Show bars representing an array of 100 elements. Animate bubble sort, merge sort, and quick sort. Highlight the elements being compared in red, sorted elements in green. Add buttons to switch between algorithms and a speed control."
