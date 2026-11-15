# Versioning et releases

Définir une version lorsqu'un projet livre une interface, un outil ou un package. Ne pas imposer des releases inutiles à un prototype.

| Taille | Convention |
| --- | --- |
| XS | Pas de version imposée ; tags facultatifs. |
| S | Tags v0.x.y pratiques pour les outils CLI distribués. |
| M | SemVer, releases et historique des changements. |
| L/XL | SemVer, migrations, compatibilité, notes et retour arrière documentés. |

## Semantic Versioning

- **MAJOR** : interface publique incompatible.
- **MINOR** : fonctionnalité rétrocompatible.
- **PATCH** : correctif rétrocompatible.
- Avant 1.0.0, signaler les ruptures même si l'interface est encore instable.
- Les Conventional Commits n'incrémentent pas automatiquement les versions sans outil configuré.

Exemples de tags : v0.1.0 pour un MVP, v0.2.0 pour une fonctionnalité, v0.2.1 pour un correctif, v1.0.0 pour une première interface stabilisée.

## Checklist de release

1. Vérifier main, dev si utilisée, tests, sécurité et compatibilité.
2. Mettre à jour la version déclarée dans le projet et le changelog/notes.
3. Créer un tag **sur le commit réellement publié de main**, après validation.
4. Publier une GitHub Release si les utilisateurs en ont besoin.
5. Prévoir revert ou hotfix en cas de régression ; synchroniser dev si elle existe.

Le modèle templates/CHANGELOG.md peut être copié et simplifié selon le projet. Les tags, releases et publications exigent une action explicite ; cette convention ne les crée pas.
