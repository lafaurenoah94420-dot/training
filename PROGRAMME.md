# Programme de formation Python

## Règles générales

- **Du mardi au samedi** — 5 sessions par semaine
- Chaque jour : exos → projet → libre → vibe, dans cet ordre
- Chaque jour a son propre dossier — tu travailles dedans toute la journée

---

## Chaque jour (Mardi → Samedi)

### Partie 1 — Exos (~45 min)

> 5 petits exercices indépendants, un par fichier, difficulté croissante. Tu t'arrêtes où tu bloques.

1. Lance `/python-exos` — l'agent génère 5 fichiers directement
2. Lance `python 01_[notion].py`, corrige jusqu'à voir `✅ Correct !`
3. Passe au fichier suivant
4. Arrête-toi quand tu bloques — c'est normal de pas finir les 5

**Objectif de progression :**

- Semaines 1-2 : finir les 3 premiers fichiers
- Semaines 3+ : finir les 5 sans chercher dans la doc

---

### Partie 2 — Projet (~1h30)

> 6 exercices progressifs sur un seul concept Python, style Codédex. Chaque exercice a ses instructions, ses tests automatiques et une page HTML.

1. Lance `/python-projet` — l'agent génère 6 exercices sur le concept du jour
2. Pour chaque exercice : lis `instructions.html`, code dans `main.py`, lance `tester.py`
3. Passe à l'exercice suivant quand tous les tests sont verts
4. Dis-moi quand tu as fini ou si tu bloques depuis plus de 15 min

**Objectif de progression :**

- Semaines 1-2 : finir les 4 premiers exercices
- Semaines 3+ : finir les 6 sans demander d'indices

---

### Partie 3 — Libre (~1h)

> Tu codes ce que tu veux autour de Nahla, Malik et Kays. From scratch, pas de scaffold.

1. Lance `/python-libre` — l'agent propose 3 idées, tu choisis
2. Tu pars d'un fichier vide et tu codes
3. Tu peux demander de l'aide — tu auras des indices, pas du code
4. Le programme doit tourner à la fin

**Objectif de progression :**

- Semaines 1-2 : arriver à un programme qui tourne même si c'est simple
- Semaines 3+ : coder sans demander d'aide

---

### Partie 4 — Vibe (~1h)

> Tu ne codes pas. Tu diriges une IA pour construire quelque chose d'ambitieux et d'impressionnant.

1. Lance `/python-vibe` — l'agent choisit le projet et toutes les specs techniques
2. Tu lis le briefing et le premier prompt de départ
3. Tu colles le prompt dans Cursor (ou l'IA de ton choix) et tu construis
4. Tu pousses aussi loin que tu veux — l'agent est là uniquement si tu bloques sur comment formuler une demande

**Objectif de progression :**

- Semaines 1-2 : réussir à faire tourner quelque chose d'impressionnant avec des prompts simples
- Semaines 3+ : maîtriser la précision des prompts, empiler les features sans perdre le fil, diriger l'IA comme un vrai chef de projet

---

## Récap hebdomadaire

| Jour     | Partie 1          | Partie 2             | Partie 3          | Partie 4         | Total  |
| -------- | ----------------- | -------------------- | ----------------- | ---------------- | ------ |
| Mardi    | `/python-exos`    | `/python-projet`     | `/python-libre`   | `/python-vibe`   | ~4h30  |
| Mercredi | `/python-exos`    | `/python-projet`     | `/python-libre`   | `/python-vibe`   | ~4h30  |
| Jeudi    | `/python-exos`    | `/python-projet`     | `/python-libre`   | `/python-vibe`   | ~4h30  |
| Vendredi | `/python-exos`    | `/python-projet`     | `/python-libre`   | `/python-vibe`   | ~4h30  |
| Samedi   | `/python-exos`    | `/python-projet`     | `/python-libre`   | `/python-vibe`   | ~4h30  |

**Total : ~22h30/semaine**

---

## Signaux de progression

Tu es à l'aise en Python quand :

- **Exos** : tu finis les 5 fichiers sans chercher dans la doc
- **Build** : tu lis un stub de fonction et tu sais quoi écrire du premier coup
- **Projet** : tu lis les instructions d'un exercice et tu codes sans indices
- **Global** : tu arrives sur du code que tu n'as pas écrit, tu comprends ce qu'il fait et tu sais où ajouter le tien

Tu maîtrises le vibe coding quand :

- **Vibe** : tu décris une feature en une phrase et l'IA la construit exactement comme tu l'imaginais
- **Vibe** : tu sais itérer — un prompt, tu vois le résultat, tu corriges la direction, tu relances
- **Vibe** : tu arrives à construire quelque chose que tu n'aurais jamais pu coder toi-même
