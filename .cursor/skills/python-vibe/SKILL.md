---
name: python-vibe
description: Session vibe coding. L'agent propose 3 projets ambitieux (jeu 2D, simulation, site…), Noah choisit. L'agent fournit la stack et un premier prompt en français. Noah pilote une IA pour construire sans coder. Utilise quand l'utilisateur dit /python-vibe.
---

# Python Vibe

Session vibe coding. Noah ne code pas — il **dirige**. Il prompt une IA (Cursor, ChatGPT, Claude) pour construire quelque chose d'ambitieux et d'impressionnant.

**L'agent propose 3 projets, Noah choisit.** L'agent fixe la stack technique et les specs — Noah n'a pas à y penser. Il reçoit un **premier prompt en français** à coller, puis il pousse aussi loin que possible.

**Une seule règle : aller le plus loin possible. Le reste, c'est l'IA qui s'en charge.**

**Durée : ~1h, pas de limite.**

---

## Gestion silencieuse (invisible pour le learner)

Tout ce qui suit se fait en arrière-plan, sans jamais en parler à Noah.

**Structure du jour :** le dossier va dans `YYYYMMDD/vibe/` à la racine du repo.

**Avant de proposer :**
1. `cd /Users/noah/Desktop/Python && git pull origin main` (silencieux, continuer si échec)
2. Scanner les dossiers `*/vibe/` et `recap.md` récents pour ne pas reproposer le même type de projet deux sessions d'affilée

**Après le débrief :**
1. Appender la section `## Vibe` dans `YYYYMMDD/recap.md`
2. `git add -A && git commit -m "YYYYMMDD vibe" && git push origin main` (silencieux)

**Format de la section recap :**
```
## Vibe
projet : [titre]
stack : [techno choisie par l'agent]
jusqu'où : [ce que Noah a réussi à construire]
prompts qui ont marché : [1-2 exemples de prompts efficaces en français]
notes : [observations sur sa façon de prompter]
```

**Règle absolue : ne jamais prononcer les mots git, GitHub, commit, push, recap devant le learner.**

---

## Workflow

### Étape 0 — Proposer 3 projets

Proposer **exactement 3 projets** ambitieux et **attendre le choix** (A, B ou C) avant de créer quoi que ce soit.

**Règles pour les 3 propositions :**
- Chaque projet doit être **visuellement impressionnant** ou **techniquement bluffant**
- Pas de mini-apps, pas de calculatrices, pas de programmes console basiques
- Les 3 options doivent être de **catégories différentes** (ex. simulation pygame + jeu 2D + site web)
- L'agent annonce la **stack** dans chaque proposition (pygame, HTML/CSS/JS, rich terminal, etc.) — Noah ne choisit pas la techno, seulement le projet
- Varier par rapport aux sessions vibe précédentes

**Banque d'inspiration (l'agent pioche et adapte) :**
- **Simulation pygame** : fourmis (stigmergie), boids, feu de forêt, Game of Life, évolution de créatures
- **Jeu 2D pygame** : shooter spatial, platformer, tower defense, casse-briques power-ups, vue de dessus arcade
- **Outil visuel pygame** : fractales interactives, visualiseur de tris animé, simulateur de gravité
- **Site web** : portfolio cyberpunk, jeu canvas dans le navigateur, dashboard fictif animé
- **Terminal rich/curses** : dashboard animé, jeu de rôle textuel avec interface soignée

Format :
```
Voici 3 projets vibe — choisis A, B ou C :

**A — [Titre accrocheur]**
[2-3 phrases : ce qu'on voit à l'écran, pourquoi c'est impressionnant]
Stack : [techno fixée par l'agent]

**B — [Titre accrocheur]**
[2-3 phrases]
Stack : [techno]

**C — [Titre accrocheur]**
[2-3 phrases]
Stack : [techno]
```

**Ne rien générer** (pas de dossier, pas de BRIEF.md) tant que Noah n'a pas choisi.

### Étape 1 — Briefing (après le choix)

Une fois Noah a choisi A, B ou C :

1. Créer `YYYYMMDD/vibe/` et `YYYYMMDD/vibe/BRIEF.md`
2. Présenter le briefing oral + le contenu du BRIEF

**BRIEF.md contient :**
- Titre du projet
- 3-4 phrases d'accroche (visuel, concret)
- Stack (déjà annoncée dans la proposition)
- **Premier prompt en français** — bloc prêt à copier-coller, détaillé et ambitieux (5-8 lignes max, pas un roman)
- 2-3 idées de features à demander ensuite à l'IA (en français, en une phrase chacune)

**Règle absolue pour les prompts :** tous les prompts fournis à Noah (premier prompt + suggestions de suite) sont **en français**. Pas de code dans le BRIEF — zéro fichier de départ.

Format affiché à Noah :
```
VIBE — [Titre du projet]

[3-4 phrases d'accroche]

Stack : [techno]
Dossier : /Users/noah/Desktop/Python/YYYYMMDD/vibe/

Pour démarrer, colle ce prompt dans Cursor (mode Agent, dossier vibe ouvert) :

[le prompt en français, entre guillemets ou en bloc]

Ensuite c'est toi. Pousse aussi loin que tu veux.
Dis-moi ce que t'as réussi à faire ou ce qui bloque.
```

### Étape 2 — Pendant la session

Noah est en autonomie. L'agent intervient **uniquement si Noah le demande**, et de façon minimaliste :

- **Prompt bloqué** → reformulation plus précise **en français** (pas de code)
- **Feature à ajouter** → une phrase type à dire à l'IA, **en français**
- **Ne sait pas quoi faire** → 2-3 directions créatives concrètes, formulées comme des prompts possibles **en français**
- **Jamais** : expliquer du code, corriger du code, écrire du code

### Étape 3 — Débrief

Quand Noah dit qu'il a fini (ou arrêté) :
- Description ou capture de ce qu'il a construit
- Le prompt (en français) qui a le mieux fonctionné

Feedback court (5 lignes max), puis silencieusement recap + git push.

---

## Banque de premiers prompts en français (exemples)

**Simulation de fourmis (pygame) :**
> Crée une simulation pygame d'une colonie de fourmis avec stigmergie. Les fourmis laissent des traces de phéromones qui s'évaporent. Quand une fourmi trouve de la nourriture, elle retourne au nid en laissant une piste forte ; les autres suivent la piste la plus intense. 100 fourmis, nid au centre, 5 sources de nourriture aléatoires. Affiche les phéromones en dégradés de couleur sur fond sombre. Fenêtre 1000x700.

**Shooter spatial (pygame) :**
> Crée un shooter spatial en pygame. Le joueur pilote un vaisseau en bas, tire vers le haut, des vagues d'ennemis descendent. Explosions en particules, score à l'écran, fond étoilé qui défile. Commence simple mais que ce soit satisfaisant visuellement (effets, sons optionnels).

**Game of Life (pygame) :**
> Crée le Jeu de la Vie de Conway en pygame. Grille 100x100, fenêtre 800x800. Espace pour pause, R pour randomiser, C pour effacer. Compteur de générations. Cellules vivantes vert fluo sur fond noir. Curseur pour la vitesse.

**Site cyberpunk (HTML/CSS/JS) :**
> Crée une page portfolio style cyberpunk : fond noir, néons vert et violet, effet glitch sur le titre, scroll fluide entre sections (À propos, Projets, Contact). Animation machine à écrire sur le texte d'accueil. Que ça fasse film de hacker.

**Visualiseur de tris (pygame) :**
> Crée un visualiseur de tris en pygame : 100 barres, anime tri à bulles, tri fusion et tri rapide. Barres comparées en rouge, triées en vert. Boutons pour changer d'algorithme et régler la vitesse.
