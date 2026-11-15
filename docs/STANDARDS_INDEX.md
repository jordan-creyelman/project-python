# Sources de vérité des conventions

Ce document indique **où modifier chaque règle** pour éviter les répétitions
contradictoires. `CHATGPT_CONTEXT.md` résume les principes pour ChatGPT,
`AGENTS.md` les rend opérationnels pour les assistants de code, et
`README.md` explique l'utilisation humaine. Les **guides thématiques
font autorité sur les détails de leur sujet**.

| Sujet | Document de référence |
| --- | --- |
| Classification XS/S/M/L | [AGENTS.md](../AGENTS.md) |
| Pilotage Tech Lead | [CHATGPT_CONTEXT.md](../CHATGPT_CONTEXT.md) |
| Git, branches, commits | [GIT_WORKFLOW.md](GIT_WORKFLOW.md) |
| Issues | [GITHUB_ISSUES.md](GITHUB_ISSUES.md) |
| Pull requests | [PULL_REQUESTS.md](PULL_REQUESTS.md) |
| CI/CD | [CI_CD_STRATEGY.md](CI_CD_STRATEGY.md) |
| Dépendances | [DEPENDENCIES.md](DEPENDENCIES.md) |
| Gestionnaire uv | [UV_WORKFLOW.md](UV_WORKFLOW.md) |
| Choix de bibliothèques | [LIBRARY_SELECTION.md](LIBRARY_SELECTION.md) |
| Docstrings | [DOCSTRINGS.md](DOCSTRINGS.md) |
| Tests | [TESTING_STRATEGY.md](TESTING_STRATEGY.md) |
| Sécurité du code | [SECURITY.md](SECURITY.md) |
| Divulgation de vulnérabilités | [SECURITY_POLICY.md](SECURITY_POLICY.md) |
| Definition of Done | [DEFINITION_OF_DONE.md](DEFINITION_OF_DONE.md) |
| ADR | [ADR.md](ADR.md) |
| Conception modulaire | [MODULAR_DESIGN.md](MODULAR_DESIGN.md) |
| Erreurs, configuration et logs | [ERROR_HANDLING.md](ERROR_HANDLING.md), [CONFIGURATION.md](CONFIGURATION.md), [LOGGING.md](LOGGING.md) |
| Procédure de travail IA | [AI_WORKFLOW.md](AI_WORKFLOW.md) |
| Contexte propre à un projet | [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md) |

## Maintenir les conventions sans duplication

1. Mettre les **règles détaillées** uniquement dans le guide concerné.
2. Dans `CHATGPT_CONTEXT.md`, `AGENTS.md` et `README.md`, ne conserver
   qu'un **résumé et un lien** vers le guide.
3. Éviter deux recommandations incompatibles : si une règle change,
   corriger d'abord sa source de vérité, puis les résumés.
4. Tester les changements avec [le validateur](../scripts/validate_repo.py)
   et la CI avant de les déclarer prêts.
5. Mettre à jour [CHANGELOG.md](../CHANGELOG.md) et [VERSION](../VERSION)
   lorsqu'une évolution de standard est publiée.
6. Les exigences explicites et contraintes du **projet qui adopte ces
   standards** restent prioritaires sur les valeurs par défaut de ce dépôt.
   Une migration n'est jamais implicite.

## Modèles

- [Exemples de démarrage](../templates/README.md) : XS, S et M.
- [Modèle CI Python](../templates/github/workflows/python-ci.yml) :
  à copier dans un vrai projet, pas dans ce dépôt documentaire.
- Les modèles sont **des points de départ**, pas une structure imposée.
