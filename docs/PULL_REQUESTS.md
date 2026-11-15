# Convention Pull Requests

**Objectif :** des changements petits, compréhensibles et vérifiés. La stratégie de branches et de fusion reste définie par GIT_WORKFLOW.md.

## Par taille

| Taille | Pratique |
| --- | --- |
| XS | PR facultative en solo et faible risque. |
| S | PR courte vers main recommandée, avec auto-revue possible en solo. |
| M | PR exigée ; vers dev si la branche d'intégration existe ; CI avant fusion, revue en équipe. |
| L/XL | PR et contrôles requis, revues renforcées selon le risque et CODEOWNERS si utile. |

## Titre et description

- **Titre en anglais**, de préférence Conventional Commits : feat(cli): add interactive mode.
- **What changed** : changement visible, interface, fichiers et compatibilité.
- **Why** : motivation utilisateur ou issue liée.
- **How tested** : commandes réellement exécutées et résultats ; dire explicitement si non exécutées.
- **Risks / rollback** : migration, sécurité, compatibilité et retour arrière si pertinent.
- Le corps peut être écrit en français.
- Une PR = une intention cohérente. Ne pas mélanger refactorisation et fonctionnalité non liée.

## Avant fusion

1. Lire le diff et vérifier qu'aucun secret ou fichier généré inutile n'est ajouté.
2. Vérifier les critères d'acceptation et DEFINITION_OF_DONE.md.
3. Attendre uniquement les statuts CI réellement configurés et requis.
4. Pour les fonctionnalités, préférer Squash and merge ; pour les releases dev vers main, respecter GIT_WORKFLOW.md.
5. Supprimer les branches temporaires fusionnées et mettre à jour les issues pertinentes.

Le modèle .github/PULL_REQUEST_TEMPLATE.md de ce dépôt est réutilisable. Il ne crée pas à lui seul une politique de revue ni des protections.
