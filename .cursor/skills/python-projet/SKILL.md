---
name: python-projet
description: Génère une session de 6 exercices progressifs sur un seul concept Python, style Codédex. Chaque exercice a un main.py, un tester.py et une instructions.html. Utilise quand l'utilisateur dit /python-projet.
---

# Python Projet

Session principale. L'agent génère 6 exercices progressifs sur **un seul concept**, comme un chapitre Codédex. Chaque exercice = un `main.py` où Noah code, un `tester.py` qui teste automatiquement, une page `instructions.html` avec l'explication du concept, les instructions et des indices pliables.

**Durée : ~1h30.**

---

## Gestion silencieuse (invisible pour le learner)

Tout ce qui suit se fait en arrière-plan, sans jamais en parler à Noah.

**Structure du jour :** les fichiers vont dans `YYYYMMDD/projet/` à la racine du repo (`/Users/noah/Desktop/Python/YYYYMMDD/projet/`).

**Avant de générer :**
1. `cd /Users/noah/Desktop/Python && git pull origin main` (silencieux, continuer si échec)
2. Scanner tous les dossiers `YYYYMMDD/projet/` existants pour voir les concepts déjà traités et ne pas répéter un concept des 2 dernières sessions.

**Après le débrief :**
1. Appender la section `## Projet` dans `YYYYMMDD/recap.md` (voir format ci-dessous)
2. `git add -A && git commit -m "YYYYMMDD projet" && git push origin main` (silencieux)

**Format de la section recap :**
```
## Projet
concept : [concept du jour]
exercices : [X]/6
bloqué : [exercice où il a bloqué, ou "—" si tout fini]
notes : [ce qui était solide vs ce qui reste fragile]
```

**Règle absolue : ne jamais prononcer les mots git, GitHub, commit, push, recap, synchronisation devant le learner.**

---

## Workflow

### Étape 0 — Choisir le concept du jour

Scanner les dossiers `YYYYMMDD/projet/` existants pour voir les concepts récents et **ne pas répéter un concept des 2 dernières sessions**.

Si c'est la première session : commencer par **Fonctions**.

**Pool de concepts (ordre recommandé) :**
1. Fonctions — définir, appeler, paramètres, return, scope
2. Listes avancées — trier, filtrer, accumuler, combiner avec des fonctions
3. Chaînes de caractères — upper, lower, replace, split, f-strings
4. Dictionnaires — lire/écrire des clés, boucler sur un dict
5. Modules — random, math, datetime
6. Boucles avancées — while, break, continue, enumerate
7. Fonctions avancées — valeurs par défaut, return multiple, imbrication
8. Gestion d'erreurs — try/except, raise
9. Fichiers — open, read, write

**Niveau de Noah :** il maîtrise variables, conditions, boucles, fonctions de base et listes (append, index, boucle, len, in). Ces notions peuvent être utilisées librement dans n'importe quel exercice sans être "le concept du jour".

Ne pas proposer de choix — générer directement.

---

### Étape 1 — Générer les 6 exercices

Créer `YYYYMMDD/projet/` avec 6 sous-dossiers :

```
YYYYMMDD/
└── projet/
    ├── 01_builtins/
    │   ├── main.py
    │   ├── tester.py
    │   └── instructions.html
    ├── 02_definir_appeler/
    │   ├── ...
    ...
    └── 06_programme_complet/
        ├── ...
```

**Arc de progression obligatoire :**

| # | Rôle | Ce que Noah fait |
|---|------|-----------------|
| 01 | Découverte | Utilise le concept sans le créer (built-ins, méthodes existantes...) |
| 02 | Premier pas | Crée la structure minimale (fonction sans params, liste vide...) |
| 03 | Avec input | Ajoute des paramètres / entrées |
| 04 | Avec output | Ajoute `return` / valeur de sortie réelle |
| 05 | Combinaison | Deux éléments du concept qui interagissent |
| 06 | Mini-programme | Programme complet qui combine tout ce qu'on a appris |

---

### Étape 3 — Format de chaque fichier

#### `main.py`

```python
# ============================================================
# Exercice [N]/6 — [Titre]
# ============================================================
# 📁 Dossier      : cd /Users/noah/Desktop/Python/YYYYMMDD/projet/0N_[nom]
# 📄 Instructions : open /Users/noah/Desktop/Python/YYYYMMDD/projet/0N_[nom]/instructions.html
# 🧪 Tester       : python3 tester.py
# ============================================================
```

**Règles strictes pour `main.py` :**
- **Rien d'autre que le header.** Pas de `def`, pas de variables, pas de `pass`, pas de commentaires supplémentaires, pas d'exemples d'appel.
- Noah lit `instructions.html` pour savoir quoi écrire — il part d'une page blanche.
- Le nom exact des fonctions et variables à créer est indiqué dans `instructions.html`, pas dans `main.py`.
- Les chemins dans le header sont toujours absolus — jamais relatifs.

#### `tester.py`

```python
# ============================================================
# Tester — [Titre]
# ============================================================
import sys

try:
    from main import [nom_fonction_ou_variable]
except ImportError as e:
    print(f"❌ Erreur d'import : {e}")
    print("   → Vérifie que tu as bien défini [ce qu'on attend] dans main.py")
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
_tester("[description en français]", [appel_fonction(args)], [valeur_attendue])

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
```

**Règles pour les tests :**
- 3 à 5 tests par exercice — cas normaux ET cas limites (0, valeur max, string vide...).
- Ne jamais tester des fonctions qui utilisent `input()` — uniquement les fonctions pures.
- Si l'exercice 01 est exploratoire (pas de fonction à tester) : tester des variables assignées dans `main.py`.
- Les messages de test sont en français et décrivent ce qu'on attend : `"soigner(60, 20) → 80"` pas `"Test 1"`.

#### `instructions.html`

Style : fond blanc (#ffffff), police Lora (Google Fonts), coloration syntaxique Python via highlight.js thème github. Les blocs de résultat terminal ont un fond sombre pour les distinguer visuellement du code Python.

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Exercice [N]/6 — [Titre]</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      background: #ffffff;
      color: #1a1a1a;
      font-family: 'Lora', Georgia, serif;
      font-size: 0.9375rem;
      line-height: 1.75;
      padding: clamp(2rem, 6vmin, 4rem) 1.5rem 6rem;
      max-width: 700px;
      margin: 0 auto;
    }

    /* ── Header ── */
    header { margin-bottom: 2.5rem; padding-bottom: 1.5rem; border-bottom: 1px solid #e8e7e2; }
    .badge {
      display: inline-block;
      font-family: ui-monospace, 'SF Mono', monospace;
      font-size: 0.68rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.09em;
      color: #999;
      background: #f5f5f3;
      border: 1px solid #e2e1db;
      padding: 0.18rem 0.6rem;
      border-radius: 999px;
      margin-bottom: 0.9rem;
    }
    h1 { font-size: clamp(1.4rem, 3vw, 1.9rem); font-weight: 500; line-height: 1.2; letter-spacing: -0.01em; margin-bottom: 0.35rem; }
    .concept-tag { font-family: ui-monospace, 'SF Mono', monospace; font-size: 0.72rem; color: #aaa; }

    /* ── Sections ── */
    section { margin-bottom: 2.5rem; }
    h2 {
      font-family: ui-monospace, 'SF Mono', monospace;
      font-size: 0.68rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: #aaa;
      margin-bottom: 1.1rem;
      padding-bottom: 0.45rem;
      border-bottom: 1px solid #ebebeb;
    }
    h3 { font-size: 0.95rem; font-weight: 600; margin: 1.75rem 0 0.6rem; color: #1a1a1a; }
    p { margin-bottom: 1rem; color: #2a2a2a; }
    ol, ul { padding-left: 1.4rem; margin-bottom: 1rem; }
    li { margin-bottom: 0.5rem; color: #2a2a2a; line-height: 1.65; }
    strong { font-weight: 600; color: #1a1a1a; }

    /* ── Code inline ── */
    code {
      font-family: ui-monospace, 'SF Mono', monospace;
      font-size: 0.82em;
      background: #f0efea;
      padding: 0.1em 0.3em;
      border-radius: 3px;
      color: #1a1a1a;
    }

    /* ── Code blocks (Python) — highlight.js thème github ── */
    pre {
      background: #f7f7f5;
      border: 1px solid #e8e7e2;
      border-radius: 6px;
      padding: 1.1rem 1.25rem;
      overflow-x: auto;
      margin: 1rem 0;
      font-size: 0.855rem;
      line-height: 1.6;
    }
    pre code { background: transparent; padding: 0; font-size: inherit; border-radius: 0; color: inherit; }
    .hljs { background: transparent !important; padding: 0 !important; }

    /* ── Terminal output (résultat attendu) — fond sombre ── */
    pre.terminal {
      background: #1e1e1e;
      border-color: #333;
      color: #d4d4d4;
    }
    pre.terminal code { color: #d4d4d4; }

    /* ── Task box ── */
    .task-box {
      border-left: 2px solid #1a1a1a;
      padding: 0.9rem 1.2rem;
      margin: 1.25rem 0;
      background: #fafaf8;
    }
    .task-box .task-title {
      font-family: ui-monospace, 'SF Mono', monospace;
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.07em;
      color: #666;
      margin-bottom: 0.75rem;
    }
    .task-box ul { margin-bottom: 0; }
    .task-box li { font-size: 0.9rem; }

    /* ── Callouts ── */
    .warn {
      font-size: 0.875rem;
      background: #fffbeb;
      border: 1px solid #e9c46a;
      border-radius: 5px;
      padding: 0.6rem 1rem;
      margin: 1rem 0;
      color: #7a5800;
      line-height: 1.55;
    }
    .info {
      font-size: 0.875rem;
      background: #f0f7ff;
      border: 1px solid #b3d4f5;
      border-radius: 5px;
      padding: 0.6rem 1rem;
      margin: 1rem 0;
      color: #1a4a7a;
      line-height: 1.55;
    }

    /* ── Commands ── */
    .commands-box {
      background: #f7f7f5;
      border: 1px solid #e8e7e2;
      border-radius: 6px;
      padding: 0.9rem 1.2rem;
    }
    .cmd-line { display: flex; align-items: center; gap: 0.7rem; margin: 0.4rem 0; flex-wrap: wrap; }
    .cmd-line .label { font-size: 0.85rem; color: #999; min-width: 8.5rem; }
    .cmd-line code { background: #ebebeb; color: #1a1a1a; font-size: 0.85rem; }
    .copy-btn {
      font-family: ui-monospace, 'SF Mono', monospace;
      font-size: 0.68rem;
      background: #fff;
      border: 1px solid #d5d4ce;
      color: #999;
      border-radius: 4px;
      padding: 0.18rem 0.5rem;
      cursor: pointer;
      transition: all 0.15s;
      white-space: nowrap;
    }
    .copy-btn:hover, .copy-btn.copied { background: #1a1a1a; color: #fff; border-color: #1a1a1a; }

    /* ── Hints ── */
    details {
      border: 1px solid #e8e7e2;
      border-radius: 6px;
      margin-bottom: 0.65rem;
      padding: 0.8rem 1rem;
    }
    summary {
      cursor: pointer;
      font-family: ui-monospace, 'SF Mono', monospace;
      font-size: 0.78rem;
      font-weight: 600;
      color: #666;
      list-style: none;
      user-select: none;
    }
    summary::-webkit-details-marker { display: none; }
    summary::before { content: '▶ '; font-size: 0.6em; color: #bbb; }
    details[open] summary::before { content: '▼ '; }
    details > *:not(summary) { margin-top: 0.8rem; }
    .hint-content { font-size: 0.9rem; color: #333; line-height: 1.65; }
    .hint-content code { background: #f0efea; }
  </style>
</head>
<body>

  <header>
    <div class="badge">Exercice [N] / 6 — [Concept]</div>
    <h1>[Titre de l'exercice]</h1>
    <div class="concept-tag">[Notion ciblée]</div>
  </header>

  <section>
    <h2>Le concept</h2>
    <p>[Explication claire du concept — 3 à 5 phrases. Explique le pourquoi avant le comment. Pas condescendant, pas scolaire.]</p>
    <pre><code class="language-python">[Exemple de code Python minimal illustrant le concept]</code></pre>
    <p>[Suite ou complément si nécessaire.]</p>
  </section>

  <section>
    <h2>Instructions</h2>
    <p>[Contexte narratif — 1 à 2 phrases pour planter le décor du thème (jeu vidéo ou monde réel).]</p>

    <!-- Pour chaque fonction à écrire, utiliser ce bloc : -->
    <h3>La fonction <code>[nom_fonction]</code></h3>
    <p>[Description en phrases complètes de ce que fait cette fonction dans le contexte du thème.]</p>
    <p>Cette fonction reçoit [N] paramètre(s). Le premier s'appelle <code>[param1]</code> — c'est un nombre qui représente [ce que c'est]. Il peut valoir [plage de valeurs expliquée en mots, pas en notation mathématique]. Le deuxième s'appelle <code>[param2]</code> — c'est [description complète].</p>
    <p>La fonction doit [expliquer ce qu'elle calcule ou fait, en langage naturel, sans code]. Elle doit retourner [description complète de ce qu'elle retourne].</p>
    <p>Attention : [décrire le ou les cas particuliers en phrases complètes, sans raccourcis].</p>
    <p>Voici des exemples pour vérifier que ta logique est correcte :</p>
    <pre><code class="language-python">[nom_fonction]([val1], [val2])   # → [résultat]
[nom_fonction]([val3], [val4])   # → [résultat]  (cas limite)</code></pre>

    <!-- Résultat terminal attendu — utiliser pre.terminal pour le fond sombre -->
    <p>Quand tu lances <code>python3 tester.py</code>, tu dois voir :</p>
    <pre class="terminal"><code>[sortie exacte du terminal]</code></pre>
  </section>

  <section>
    <h2>Commandes</h2>
    <div class="commands-box">
      <div class="cmd-line">
        <span class="label">📁 Dossier</span>
        <code>cd /Users/noah/Desktop/Python/YYYYMMDD/projet/0N_[nom]</code>
        <button class="copy-btn" onclick="copier(this, 'cd /Users/noah/Desktop/Python/YYYYMMDD/projet/0N_[nom]')">⎘ copier</button>
      </div>
      <div class="cmd-line">
        <span class="label">📄 Instructions</span>
        <code>open /Users/noah/Desktop/Python/YYYYMMDD/projet/0N_[nom]/instructions.html</code>
        <button class="copy-btn" onclick="copier(this, 'open /Users/noah/Desktop/Python/YYYYMMDD/projet/0N_[nom]/instructions.html')">⎘ copier</button>
      </div>
      <div class="cmd-line">
        <span class="label">🧪 Tester</span>
        <code>python3 tester.py</code>
        <button class="copy-btn" onclick="copier(this, 'python3 tester.py')">⎘ copier</button>
      </div>
    </div>
  </section>

  <section>
    <h2>Indices</h2>

    <details>
      <summary>💡 Indice 1 — [titre en une phrase courte]</summary>
      <div class="hint-content">
        <p>[Premier indice — oriente vers le bon outil Python ou la bonne façon de penser le problème. Pas de code complet.]</p>
      </div>
    </details>

    <details>
      <summary>💡 Indice 2 — [titre plus précis]</summary>
      <div class="hint-content">
        <p>[Deuxième indice plus précis — peut montrer la structure sans donner la solution complète.]</p>
        <pre><code class="language-python">[Structure partielle ou pseudo-code si vraiment nécessaire]</code></pre>
      </div>
    </details>

  </section>

  <script>hljs.highlightAll();</script>
  <script>
    function copier(btn, texte) {
      navigator.clipboard.writeText(texte).then(() => {
        btn.textContent = '✓ copié';
        btn.classList.add('copied');
        setTimeout(() => { btn.textContent = '⎘ copier'; btn.classList.remove('copied'); }, 1500);
      });
    }
  </script>
</body>
</html>
```

---

### Étape 4 — Lancement

Après avoir généré tous les fichiers, afficher :

```
📁  Session générée — [Concept] — 6 exercices.

Pour chaque exercice, dans l'ordre, copie-colle ces commandes :

  Exercice 01 :
    cd /Users/noah/Desktop/Python/YYYYMMDD/projet/01_[nom]
    open instructions.html
    python3 tester.py

  Exercice 02 :
    cd /Users/noah/Desktop/Python/YYYYMMDD/projet/02_[nom]
    open instructions.html
    python3 tester.py

  Exercice 03 :
    cd /Users/noah/Desktop/Python/YYYYMMDD/projet/03_[nom]
    open instructions.html
    python3 tester.py

  Exercice 04 :
    cd /Users/noah/Desktop/Python/YYYYMMDD/projet/04_[nom]
    open instructions.html
    python3 tester.py

  Exercice 05 :
    cd /Users/noah/Desktop/Python/YYYYMMDD/projet/05_[nom]
    open instructions.html
    python3 tester.py

  Exercice 06 :
    cd /Users/noah/Desktop/Python/YYYYMMDD/projet/06_[nom]
    open instructions.html
    python3 tester.py

Lis les instructions d'abord, code dans main.py, puis teste.
Passe à l'exercice suivant quand tous les tests sont verts.

Dis-moi quand t'as fini ou si tu bloques depuis plus de 15 min.
```

### Étape 5 — Débrief (quand Noah a fini)

Demander jusqu'à quel exercice il est allé et si tous les tests sont passés.

Feedback ciblé (8 à 10 lignes max) :
- Quel exercice a demandé le plus de réflexion et pourquoi
- Le concept ou l'outil Python utilisé pour la première fois
- Ce qu'il faut retenir avant la prochaine session
- 1 chose à creuser si un exercice n'a pas été fini

Ensuite, silencieusement :
1. Appender la section `## Projet` dans `YYYYMMDD/recap.md`
2. `git add -A && git commit -m "YYYYMMDD projet" && git push origin main`

---

## Règles générales

**Niveau :** Noah maîtrise variables, conditions, boucles, fonctions de base et listes (append, index, boucle, len, in, sort). Les exercices peuvent utiliser toutes ces notions librement — le concept du jour est ce qu'on *approfondit*, pas la seule chose qu'on utilise.

**Langue :** instructions, commentaires et textes en français — noms de variables et fonctions en anglais.

**Interdits :** classes, décorateurs, générateurs, async/await, compréhensions de liste (sauf si c'est le concept du jour).

**Style des exercices :** concrets, contextualisés, variés. Pas de "calcule 2 + 2". Un exercice doit avoir un vrai contexte narratif qui donne envie de le résoudre.

---

## Règles de rédaction des instructions HTML

Ces règles s'appliquent à tout le texte écrit dans les pages `instructions.html`. Elles sont strictes.

### Phrases complètes, jamais d'abréviations

Toujours écrire des phrases complètes avec sujet, verbe, complément. Jamais de style liste compressée ou de notation raccourcie.

**Interdit :**
> Paramètre `faim` : entier entre 0 et 100 — niveau de faim (100 = très affamé)

**Correct :**
> Cette fonction reçoit un paramètre qui s'appelle `faim`. C'est un nombre qui représente le niveau de faim actuel du joueur. Il peut valoir entre zéro et cent. Quand ce nombre vaut cent, le joueur est en train de mourir de faim. Quand il vaut zéro, il est complètement rassasié.

### Vocabulaire adapté à un débutant de 16 ans

- Dire **"nombre"** — jamais "entier", jamais "int"
- Dire **"texte"** ou **"chaîne de caractères"** — jamais "string"
- Dire **"vrai ou faux"** — jamais "booléen" ou "bool"
- Expliquer les plages de valeurs en mots : "entre zéro et cent" — jamais "0 ≤ x ≤ 100"
- Expliquer les cas limites avec un exemple concret : "par exemple, si le joueur mange 50 points de nourriture alors qu'il n'a que 10 points de faim, le résultat ne peut pas être négatif, donc la fonction doit retourner zéro"

### Jamais de notation `param=valeur` dans les explications

Pour décrire ce qu'il faut passer à une fonction, écrire en français, pas en code.

**Interdit :**
> Appelle la fonction trois fois : pour Kyle (faim=90, nourriture=30), Rose (faim=55, nourriture=60), Mark (faim=20, nourriture=5).

**Correct :**
> Une fois que tout fonctionne, appelle la fonction trois fois dans ton fichier. La première fois, passe-lui les données de Kyle : il a un niveau de faim de quatre-vingt-dix et il mange une nourriture d'une valeur de trente. La deuxième fois, c'est Rose : sa faim est à cinquante-cinq et elle mange une nourriture de valeur soixante. La troisième fois, c'est Mark : sa faim est à vingt et il mange une nourriture de valeur cinq.

### Expliquer le "pourquoi" pas seulement le "quoi"

Ne pas se contenter de lister ce qu'il faut faire. Expliquer pourquoi cette règle existe, avec une analogie ou un exemple du monde réel quand c'est possible.

**Interdit :**
> Si faim - valeur < 0, retourner 0.

**Correct :**
> Quand on mange, la faim diminue. Mais la faim ne peut jamais descendre en dessous de zéro — dans la vraie vie, on ne peut pas être "moins qu'affamé". Donc si le calcul donne un nombre négatif, ta fonction doit retourner zéro à la place.
