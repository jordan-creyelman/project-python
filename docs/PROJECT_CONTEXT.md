# Contexte du projet — modèle à copier et compléter

> Ce fichier est un modèle. Le remplir pour chaque projet, ou le copier dans son dossier.
> Les règles générales sont dans `AGENTS.md`.

## Identité
- Nom : À définir
- Objectif en une phrase : À définir
- Utilisateurs : À définir
- Statut : idée / prototype / production
- Taille estimée : XS / S / M / L-XL
- Pourquoi cette taille : À définir

## Fonctionnalités
### Inclus maintenant (MVP)
- [ ] Fonctionnalité 1

### Explicitement exclu (YAGNI)
- Fonctionnalité future non demandée

## Contraintes
- Version Python : 3.12+ par défaut, à adapter
- Plateformes : À définir
- Entrées / sorties : À définir
- Dépendances autorisées : bibliothèque standard d'abord
- Persistance / API / UI : aucune, sauf besoin explicite
- Sécurité, confidentialité, performances : À définir

## Architecture décidée
- Style : script / paquet CLI / application modulaire / monolithe modulaire
- Modules essentiels : À définir
- Frontières I/O / métier : À définir
- Pourquoi pas une architecture plus lourde : À définir
- Décisions (ADR si nécessaire) : À définir

## Qualité
- Ruff : lint et format
- pytest : tests utiles
- Typage statique : selon risque/complexité
- Critères d'acceptation : À définir

## Gestion des erreurs
- Entrées à valider : À définir
- Exceptions attendues et messages utilisateur : À définir
- Comportement si dépendance externe indisponible : À définir
- Logs / métriques / retry nécessaires : À définir
- Référence : `docs/ERROR_HANDLING.md`

## Stratégie de tests
- Tests unitaires : À définir
- Tests d'intégration : À définir
- Tests E2E / contrat : seulement si justifiés
- Cas limites et défaillances critiques : À définir
- Tests de régression pour bugs corrigés : oui si possible
- Performance / sécurité / compatibilité : selon risques
- Référence : `docs/TESTING_STRATEGY.md`

## Commandes
- Installation : À définir
- Exécution : À définir
- Tests : `pytest` (si configuré)
- Lint : `ruff check .` (si installé)
- Format : `ruff format --check .` (si installé)

## Plan de mise en œuvre
1. Construire le plus petit chemin fonctionnel.
2. Tester les règles métier et erreurs importantes.
3. Refactoriser seulement si une duplication ou complexité réelle apparaît.
4. Ajouter des fonctionnalités uniquement selon les besoins validés.

## Questions ouvertes
- Aucune pour le moment.
