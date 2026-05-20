---
name: python-vibe
description: Session vibe coding avec l'agent Cursor. L'agent propose 3 projets ambitieux, Noah choisit. Noah dirige étape par étape en français dans le chat ; l'agent crée le code dans YYYYMMDD/vibe/. Noah n'écrit pas de code lui-même. Utilise quand l'utilisateur dit /python-vibe.
---

# Python Vibe

Session vibe coding **dans ce chat**. Noah ne tape pas de code — il **donne des consignes** à l'agent, étape par étape, en français naturel (« crée le fond noir », « ajoute le serpent », « accélère un peu »). **C'est l'agent qui crée** les fichiers dans `YYYYMMDD/vibe/`.

Noah apprend à **penser comme un chef de projet** : découper, demander, itérer, corriger la direction — sans écrire le code lui-même.

**Une seule règle : aller le plus loin possible.**

**Durée : ~1h, pas de limite.**

---

## Gestion silencieuse (invisible pour le learner)

**Structure du jour :** `YYYYMMDD/vibe/` à la racine du repo.

**Avant de proposer :**
1. `cd /Users/noah/Desktop/Python && git pull origin main` (silencieux)
2. Scanner `*/vibe/` et recaps récents pour varier les types de projets

**Après le débrief :**
1. Appender `## Vibe` dans `YYYYMMDD/recap.md`
2. `git add -A && git commit -m "YYYYMMDD vibe" && git push origin main` (silencieux)

**Format recap :**
```
## Vibe
projet : [titre]
stack : [techno]
jusqu'où : [ce qui tourne à la fin]
consignes qui ont bien marché : [1-2 formulations de Noah en français]
notes : [clarté des demandes, ce qui bloque encore]
```

**Ne jamais prononcer git, recap, commit devant le learner.**

---

## Workflow

### Étape 0 — Proposer 3 projets

**3 propositions** (A, B, C), catégories différentes, stack annoncée par l'agent. **Attendre le choix.** Rien ne créer avant.

Noah peut aussi **proposer son idée** (ex. « un Snake ») — l'agent valide, fixe la stack, et on part là-dessus.

Format :
```
Voici 3 projets vibe — choisis A, B ou C (ou dis ton idée) :

**A — [Titre]**
[2-3 phrases visuelles]
Stack : [techno]

**B — ...**
**C — ...**
```

### Étape 1 — Briefing + premier pas

Après le choix :

1. Créer `YYYYMMDD/vibe/` et `BRIEF.md` (vision + stack + **feuille de route** en étapes, pas un prompt à coller ailleurs)
2. Expliquer à Noah : **tu me dis quoi faire, je code ici**, une brique à la fois
3. **Lancer la première brique** si Noah dit « go » — typiquement : fenêtre + fond (pygame) ou squelette HTML — selon le projet

**BRIEF.md contient :**
- Titre, accroche, stack
- Liste d'étapes suggérées (5-8 lignes) que Noah pourra demander une par une
- Pas de code de départ dans le BRIEF (l'agent le génère au fil de la session)

Format oral :
```
VIBE — [Titre]

[accroche]

Stack : [techno]
Dossier : YYYYMMDD/vibe/

Tu me guides en français, étape par étape — je crée les fichiers.
On peut commencer par : [première étape concrète].

Dis-moi la suite quand tu veux.
```

### Étape 2 — Pendant la session (cœur du vibe)

**Noah parle, l'agent code** dans `YYYYMMDD/vibe/`.

**L'agent DOIT :**
- Implémenter ce que Noah demande (ou la variante la plus proche réaliste)
- Créer / modifier les fichiers du projet (main.py, index.html, etc.)
- Ajouter un README avec comment lancer si pertinent
- Après chaque étape livrée : rappeler **une phrase** pour lancer/tester (`python3 main.py`, ouvrir index.html…)
- Proposer **1-2 prochaines étapes possibles** en français (« tu veux qu'on ajoute… ? ») sans imposer

**L'agent NE DOIT PAS :**
- Refuser de coder en renvoyant Noah vers « un autre Agent » ou « colle ce prompt »
- Tout construire d'un coup sans que Noah ait au moins validé la direction (sauf si Noah dit « fais tout le snake de base »)
- Remplir des explications de code longues — Noah n'écrit pas le code, il n'a pas besoin d'un cours ligne par ligne

**Si Noah est vague** (« améliore ») → l'agent pose **une question courte** ou propose 2 options concrètes avant de coder.

**Si Noah est bloqué** → l'agent suggère 2-3 consignes qu'il pourrait dire telles quelles.

**Professeur.mdc** : les règles « ne pas écrire le code de l'exercice » **ne s'appliquent pas** à `YYYYMMDD/vibe/` — ici l'agent code, Noah dirige.

### Étape 3 — Débrief

Quand Noah a fini :
- Ce qui tourne à l'écran
- **Quelle formulation** de sa part a le mieux marché (« quand j'ai dit X, tu as fait exactement ce que je voulais »)

Feedback court (5 lignes), puis recap + git push.

---

## Banque de projets (inspiration)

- Simulation pygame (fourmis, boids, feu, Game of Life)
- Jeu 2D pygame (shooter, snake amélioré, tower defense, casse-briques)
- Outil visuel pygame (fractales, tris animés, gravité)
- Site web (cyberpunk, jeu canvas, dashboard)
- Terminal rich (dashboard animé, RPG texte)

## Feuille de route type — Snake (pygame)

1. Fenêtre + fond noir + fermeture propre
2. Grille + serpent immobile au centre
3. Déplacement continu (flèches, pas demi-tour instantané)
4. Pomme aléatoire + croissance + score
5. Collisions (murs, soi) + Game Over + R pour rejouer
6. Polish (couleurs, vitesse, power-ups si Noah demande)
