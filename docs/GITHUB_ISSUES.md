# Convention GitHub Issues

**Objectif :** cadrer les demandes et bugs avec une traçabilité proportionnée au projet. Voir aussi GIT_WORKFLOW.md.

## Politique par taille

| Taille | Pratique |
| --- | --- |
| XS | Issue facultative ; un commit explicite suffit pour une petite tâche solo. |
| S | Issue recommandée pour bug ou évolution non triviale ; pas nécessaire pour une correction minime. |
| M | Issue avant les changements fonctionnels significatifs ; critères d'acceptation et priorité clairs. |
| L/XL | Issues liées aux jalons, dépendances, responsabilités et objectifs métier. |

## Règles

- Titre court et **en anglais** : Add battery-life estimator, Fix invalid voltage input.
- Décrire **pourquoi** la demande existe, son public et le résultat observable attendu.
- Bug : étapes de reproduction, attendu/réel, version, environnement et traces assainies.
- Fonctionnalité : problème, MVP, critères d'acceptation et hors périmètre.
- Priorité si utile : P0 bloquant, P1 haute, P2 normale, P3 amélioration.
- Labels recommandés uniquement s'ils sont réellement utilisés : bug, enhancement, documentation, priority:p1. Les labels doivent exister dans le dépôt avant usage automatisé.
- Lier la PR avec Closes #123 uniquement lorsque la PR résout entièrement l'issue.
- Ne jamais ouvrir une issue publique pour une faille de sécurité exploitable et non corrigée : suivre SECURITY_POLICY.md.

## Modèles

Les formulaires .github/ISSUE_TEMPLATE/bug_report.yml et feature_request.yml sont utilisables dans ce dépôt. Les copier ou adapter dans les autres dépôts. Leurs champs restent courts pour ne pas compliquer le travail XS/S.

La fin de l'issue suit DEFINITION_OF_DONE.md et PULL_REQUESTS.md.
