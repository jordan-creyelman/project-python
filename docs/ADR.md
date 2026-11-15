# Architecture Decision Records (ADR)

Un ADR documente **pourquoi** un choix technique structurant a été adopté, quelles options ont été examinées et quelles conséquences sont acceptées.

| Taille | Usage |
| --- | --- |
| XS | Aucun ADR par défaut. |
| S | Facultatif pour une décision coûteuse à inverser. |
| M | Recommandé pour architecture, stockage, API, sécurité ou dépendance majeure. |
| L/XL | Attendu pour les décisions transverses ou difficiles à inverser. |

## Format

1. **Context** : problème, contraintes et objectif.
2. **Options considered** : alternatives réalistes et compromis.
3. **Decision** : solution retenue et justification.
4. **Consequences** : avantages, limitations, migration et risques.
5. **Status** : Proposed, Accepted, Superseded ou Deprecated.
6. **References** : issue, PR, autre ADR et code concerné.

Dans le projet cible, placer les ADR dans docs/adr/ et nommer les fichiers en anglais, par exemple 0001-use-typer-for-cli.md. Garder les décisions précédentes lorsqu'une nouvelle les remplace : utiliser le statut Superseded et un lien vers le nouvel ADR.

Le modèle templates/adr/0000-template.md est à copier et remplir. Ne pas fabriquer des ADR pour des choix triviaux ni prétendre qu'un ADR a été approuvé sans validation.
