# project-python — Contexte Python pour ChatGPT

Ce dépôt est **mon guide de programmation Python pour ChatGPT**. Il fournit des règles de qualité (PEP 8, KISS, SOLID, YAGNI, DRY), de conception modulaire, de sécurité, de gestion d'erreurs et de tests, adaptées aux petits scripts comme aux grandes applications.

**Ce dépôt ne contient pas un programme Python à installer ou exécuter.** C'est une bibliothèque d'instructions pour guider la génération et la modification de code.

## Démarrage rapide — comment l'utiliser

### 1. Ouvrir ChatGPT

Démarrer une conversation et copier cette demande :

```text
Utilise mon contexte de développement Python :
https://github.com/jordan-creyelman/project-python/blob/main/CHATGPT_CONTEXT.md

Lis le contexte et les guides pertinents avant de coder.
Mon besoin : [décrire précisément le programme Python souhaité].
```

ChatGPT peut alors consulter les règles et les appliquer au programme demandé. Si l'accès au lien échoue, coller le contenu de `CHATGPT_CONTEXT.md` dans la conversation.

### 2. Décrire le besoin

Préciser si possible :
- ce que le programme doit faire ;
- les entrées et sorties attendues ;
- la version Python, le système et les contraintes éventuelles ;
- s'il s'agit d'un nouveau programme ou d'une modification d'un code existant.

La **taille XS/S/M/L** peut être déduite par l'assistant ; inutile de la choisir à chaque fois. L'architecture doit rester proportionnée au besoin.

### 3. Recevoir et vérifier le programme

Demander un code directement utilisable, une explication courte, les instructions d'installation/exécution et les tests utiles. Les tests non exécutés doivent être signalés comme tels.

## Exemple 1 — petit script

```text
Utilise mon contexte Python :
https://github.com/jordan-creyelman/project-python/blob/main/CHATGPT_CONTEXT.md

Crée un script qui renomme les fichiers d'un dossier selon leur date.
Prévois un mode simulation pour éviter les modifications accidentelles.
Reste simple, utilise pathlib et gère les erreurs de fichiers.
```

## Exemple 2 — application plus importante

```text
Utilise mon contexte Python :
https://github.com/jordan-creyelman/project-python/blob/main/CHATGPT_CONTEXT.md

Crée une API Python pour gérer des tâches.
Choisis l'architecture adaptée, avec des fonctions modulaires,
configuration claire, validation des entrées, tests pytest
et une gestion des erreurs cohérente.
Évite les abstractions inutiles.
```

## Exemple 3 — corriger un programme existant

```text
Utilise mon contexte Python :
https://github.com/jordan-creyelman/project-python/blob/main/CHATGPT_CONTEXT.md

Voici mon code et l'erreur rencontrée : [coller le code et l'erreur].
Corrige le problème sans changer les fonctionnalités non concernées.
Ajoute un test de régression si pertinent et explique la correction.
```

## Gestionnaire Python par défaut : uv

Pour les **nouveaux projets Python**, le Tech Lead utilise
[uv](https://docs.astral.sh/uv/) comme gestionnaire d'environnements,
dépendances, scripts, tests et builds, **en adaptant l'outillage à la taille**.

```bash
# Petit script XS, sans projet packagé
uv run script.py

# Projet S/M/L existant configuré avec uv et uv.lock
uv sync --locked
uv run --locked pytest
uv run --locked ruff check .
uv run --locked ruff format --check .
```

Pour les nouveaux projets plus structurés : `uv init`, `uv add`,
`uv add --dev`, `uv lock` et `uv build` si distribution nécessaire.
Ne jamais imposer une migration à un dépôt existant sans évaluer sa
configuration et ses contraintes.

Lire le [guide uv complet](docs/UV_WORKFLOW.md).

## Convention GitHub pour les projets Python

Les **noms de branches, messages de commit et titres de PR** sont en anglais.
Les commits suivent **Conventional Commits**, par exemple :

```text
feat(cli): add interactive mode
fix(led): reject negative current
docs(git): document branching strategy
```

`main` est toujours la branche stable ; `dev` est une branche d'intégration
pour les projets M/L-XL, facultative pour les petits scripts et outils.
Les branches temporaires suivent `feature/*`, `fix/*`, `hotfix/*`,
`docs/*`, etc. Le niveau de CI, les revues et les protections augmentent
avec la complexité et le risque.

Lire la [convention Git et GitHub complète](docs/GIT_WORKFLOW.md).

## Huit conventions de qualité et de collaboration

Ces conventions **complètent** la stratégie Git et GitHub et s'adaptent à la
taille **XS/S/M/L-XL** et au risque du projet :

1. [Gestion des issues](docs/GITHUB_ISSUES.md) : bugs, fonctionnalités, priorités et critères d'acceptation.
2. [Pull requests](docs/PULL_REQUESTS.md) : description, revue et vérifications.
3. [CI/CD](docs/CI_CD_STRATEGY.md) : automatisation des contrôles et livraison maîtrisée.
4. [Versioning](docs/VERSIONING.md) : SemVer, tags, releases et changelog.
5. [Dépendances](docs/DEPENDENCIES.md) : pyproject.toml, versions et Dependabot.
6. [Security Policy](docs/SECURITY_POLICY.md) : signalement privé, triage et correction.
7. [Definition of Done](docs/DEFINITION_OF_DONE.md) : critères avant livraison.
8. [ADR](docs/ADR.md) : documentation des choix structurants.

**Modèles prêts à adapter :** [Issues](.github/ISSUE_TEMPLATE/),
[Pull Request](.github/PULL_REQUEST_TEMPLATE.md),
[CI Python](templates/github/workflows/python-ci.yml),
[Dependabot](templates/github/dependabot.yml),
[Security Policy](templates/SECURITY.md),
[ADR](templates/adr/0000-template.md),
[Changelog](templates/CHANGELOG.md).

Les modèles d'issues et de PR sont actifs pour ce dépôt de documentation.
Les fichiers sous **templates/** ne sont pas actifs : les copier et adapter
dans chaque projet Python concerné. Aucun workflow CI de Python ni déploiement
automatique n'est activé dans project-python.

## Conventions de choix technique et de documentation du code

- [Choix des bibliothèques et frameworks](docs/LIBRARY_SELECTION.md) :
  préférer des solutions adaptées, stables, récentes et maintenues,
  avec une **communauté active et importante** si plusieurs options
  répondent au besoin. Vérifier les versions et la maintenance au moment
  de recommander ; ne pas choisir uniquement sur la popularité.
- [Docstrings Python en anglais](docs/DOCSTRINGS.md) :
  PEP 257, docstrings explicites pour les API publiques et les comportements
  non évidents ; style Google si des sections sont utiles. Les échanges
  et la documentation utilisateur peuvent rester en français.

Les décisions restent proportionnées à XS/S/M/L-XL. Ces conventions
s'appliquent aux futurs projets quand le contexte est utilisé, sans
modifier automatiquement leurs dépendances ou leur code existant.

## Utilisation sur plusieurs conversations

**Important : le dépôt GitHub n'est pas automatiquement chargé dans toutes les conversations ChatGPT.**

Options possibles :
1. **Conversation ponctuelle** : donner le lien vers `CHATGPT_CONTEXT.md` au début de la demande.
2. **Projet ChatGPT dédié à Python** : si la fonctionnalité est disponible, ajouter `CHATGPT_CONTEXT.md` et, au besoin, les autres guides aux instructions/fichiers du projet ; travailler ensuite dans ce projet.
3. **Projet de code disposant de son propre dépôt** : copier ou référencer les règles pertinentes et les adapter aux contraintes réelles du programme.

Si le fichier GitHub change, demander à ChatGPT de le relire ; une copie déjà fournie dans un projet ou une conversation ne se met pas nécessairement à jour automatiquement.

## Organisation des instructions

| Fichier | Rôle |
| --- | --- |
| [CHATGPT_CONTEXT.md](CHATGPT_CONTEXT.md) | **Point d'entrée recommandé** pour toutes les demandes Python |
| [AGENTS.md](AGENTS.md) | Règles générales détaillées, choix d'architecture XS à XL |
| [docs/MODULAR_DESIGN.md](docs/MODULAR_DESIGN.md) | Fonctions modulaires et séparation des responsabilités |
| [docs/ERROR_HANDLING.md](docs/ERROR_HANDLING.md) | Exceptions, validation, retries et erreurs I/O |
| [docs/TESTING_STRATEGY.md](docs/TESTING_STRATEGY.md) | Tests unitaires, intégration, E2E et régression |
| [docs/SECURITY.md](docs/SECURITY.md) | Secrets, entrées non fiables, permissions et injections |
| [docs/CONFIGURATION.md](docs/CONFIGURATION.md) | Variables d'environnement, validation et paramètres |
| [docs/LOGGING.md](docs/LOGGING.md) | Journalisation et diagnostic |
| [docs/LIBRARY_SELECTION.md](docs/LIBRARY_SELECTION.md) | Choix de bibliothèques/frameworks actuels et maintenus |
| [docs/DOCSTRINGS.md](docs/DOCSTRINGS.md) | Docstrings Python en anglais (PEP 257, style Google proportionné) |
| [docs/UV_WORKFLOW.md](docs/UV_WORKFLOW.md) | **uv par défaut** : création, dépendances, exécution, lockfile, builds, CI |
| [docs/GIT_WORKFLOW.md](docs/GIT_WORKFLOW.md) | Stratégie GitHub XS/S/M/L-XL, branches, commits en anglais, PR et releases |
| [docs/AI_WORKFLOW.md](docs/AI_WORKFLOW.md) | Méthode de travail, vérifications et compte rendu |
| [docs/PROJECT_CONTEXT.md](docs/PROJECT_CONTEXT.md) | Modèle **facultatif** pour préciser un programme particulier |

**Il n'est pas nécessaire de lire tous les documents pour un script simple** : commencer par `CHATGPT_CONTEXT.md`, puis consulter les guides liés à la tâche.

## Philosophie

- **KISS** : la solution la plus simple qui résout le problème.
- **YAGNI** : aucune fonctionnalité anticipée inutile.
- **SOLID / DRY** : à appliquer avec discernement, sans surarchitecture.
- **PEP 8 / PEP 257** : code lisible et conventions cohérentes.
- **Fiabilité** : erreurs prévisibles, tests adaptés, sécurité dès le départ.
- **Transparence** : ne jamais annoncer des tests réussis sans les avoir exécutés.

Le but est d'obtenir un **bon programme Python**, pas de multiplier les fichiers, les classes et les frameworks.
