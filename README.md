# project-python

**Référentiel d'instructions pour guider ChatGPT lors de mes demandes de programmation Python**, de XS à XL, sans surarchitecture. Ce dépôt n'est pas un projet applicatif à exécuter.

## Utiliser avec ChatGPT
Dans une nouvelle conversation, écrire :

> Utilise mon contexte Python : https://github.com/jordan-creyelman/project-python/blob/main/CHATGPT_CONTEXT.md. Lis-le, puis programme [décrire le besoin] en respectant ses règles.

ChatGPT ne charge **pas automatiquement** ce dépôt dans toutes les nouvelles conversations : donner le lien ou le fichier au début d'une demande (ou l'inclure dans les instructions d'un projet ChatGPT, si disponible).

## Fichiers
- [CHATGPT_CONTEXT.md](CHATGPT_CONTEXT.md) : **point d'entrée court recommandé pour ChatGPT** ; règles et consignes réutilisables.
- [AGENTS.md](AGENTS.md) : instructions pour assistants de code et conventions générales (PEP 8, PEP 257, KISS, SOLID, YAGNI, DRY).
- [docs/PROJECT_CONTEXT.md](docs/PROJECT_CONTEXT.md) : modèle à compléter pour chaque projet (objectif, taille, contraintes, architecture, tests).

- [docs/MODULAR_DESIGN.md](docs/MODULAR_DESIGN.md) : fonctions modulaires, responsabilités, API publiques, séparation logique/I-O et architecture progressive.
- [docs/ERROR_HANDLING.md](docs/ERROR_HANDLING.md) : gestion des exceptions, validation, logs, défaillances externes, sécurité.
- [docs/TESTING_STRATEGY.md](docs/TESTING_STRATEGY.md) : stratégie de tests unitaires, intégration, E2E, régression, contrats, sécurité et performance.

- [docs/SECURITY.md](docs/SECURITY.md) : secrets, validation, injections, permissions et risques.
- [docs/CONFIGURATION.md](docs/CONFIGURATION.md) : variables d'environnement, configuration typée, validations.
- [docs/LOGGING.md](docs/LOGGING.md) : événements, niveaux de logs et observabilité.
- [docs/AI_WORKFLOW.md](docs/AI_WORKFLOW.md) : étapes et checklist pour les assistants de développement.

## Pour un projet Python particulier
1. Décrire le programme à ChatGPT en lui indiquant le lien vers `CHATGPT_CONTEXT.md`.
2. Choisir la taille **XS**, **S**, **M** ou **L/XL** selon les besoins, pas seulement les lignes de code.
3. Remplir `docs/PROJECT_CONTEXT.md` **uniquement si nécessaire** pour documenter des contraintes spécifiques.
4. Demander à l'assistant de consulter `AGENTS.md` et les guides spécialisés pertinents, puis de coder le MVP avec l'architecture minimale.
5. Garder les tests, la documentation et les dépendances proportionnels à la complexité.

## Philosophie
**Simple d'abord, structuré quand nécessaire.** Les exemples de structures sont des guides, pas des dossiers à créer obligatoirement. Le dépôt ne contient pas de squelette applicatif imposé.

## Exemple de demande
> Crée un outil CLI Python pour renommer des fichiers. Taille S. Respecte AGENTS.md et docs/PROJECT_CONTEXT.md. Utilise pathlib, Ruff et pytest. Commence par le MVP et n'ajoute pas de couche repository/service sans besoin.
