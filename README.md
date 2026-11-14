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
