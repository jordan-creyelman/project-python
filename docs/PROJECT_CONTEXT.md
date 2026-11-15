# Contexte du projet — modèle à copier et compléter

> Ce fichier est un modèle. Le remplir pour chaque projet, ou le copier dans son dossier.
> Les règles générales sont dans `AGENTS.md` ; les documents de référence
> sont listés dans `docs/STANDARDS_INDEX.md`.

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
- Gestionnaire Python : **uv par défaut pour un nouveau projet** ; autre gestionnaire existant à respecter/justifier
- Workflow uv : script XS simple / projet `pyproject.toml` + `uv.lock` selon taille
- Commandes d'installation et test : `uv sync` et `uv run` si uv est adopté
- Version Python et `uv.lock` : À définir ; migration éventuelle : À valider
- Référence : `docs/UV_WORKFLOW.md`
- Variables d'environnement : nécessaires ou non ; préfixe propre au projet
- Sources et priorité de configuration : CLI / environnement / défauts, à préciser
- Secrets : uniquement via canal sécurisé, jamais dans `.env.example`
- Référence : `docs/CONFIGURATION.md`
- Dépendances autorisées : bibliothèque standard d'abord
- Bibliothèques/frameworks envisagés : adéquation et alternatives à préciser
- Vérification des versions, maintenance, communauté et sécurité : source/date à renseigner si nécessaire
- Référence : `docs/LIBRARY_SELECTION.md`
- Persistance / API / UI : aucune, sauf besoin explicite
- Sécurité, confidentialité, performances : À définir

## Architecture décidée
- Style : script / paquet CLI / application modulaire / monolithe modulaire
- Modules essentiels : À définir
- Frontières I/O / métier : À définir
- Pourquoi pas une architecture plus lourde : À définir
- Décisions (ADR si nécessaire) : À définir

## Stratégie Git et GitHub
- Taille et risque justifiant le workflow : À définir (XS / S / M / L-XL)
- Branche stable : `main`
- Branche d'intégration `dev` : oui / non (justification : À définir)
- Branches temporaires : `feature/*`, `fix/*`, `hotfix/*`, etc.
- Messages de commit : Conventional Commits, **en anglais**
- Cible des PR : `main` (XS/S) ou `dev` (M/L) ; à confirmer
- CI, protections et revues : À définir selon la taille et le risque
- Tags et releases : À définir
- Référence : `docs/GIT_WORKFLOW.md`

## Conventions GitHub et livraison du projet

- Issues : aucune / bugs / backlog ; critères d'acceptation : À définir.
- PR : facultatives / recommandées / requises ; revue et cible : À définir.
- CI/CD : contrôles disponibles, déploiement et rollback : À définir.
- Versioning : tags / SemVer / releases / changelog : À définir.
- Dépendances : **uv par défaut**, pyproject, uv.lock et mises à jour : À définir ; préserver les outils existants sans migration validée.
- Security Policy : versions supportées et canal privé réel : À définir.
- Definition of Done : tests, documentation et critères de livraison : À définir.
- ADR : décisions structurantes qui doivent être enregistrées : À définir.
- Guides : GITHUB_ISSUES.md, PULL_REQUESTS.md, CI_CD_STRATEGY.md,
  VERSIONING.md, DEPENDENCIES.md, SECURITY_POLICY.md,
  DEFINITION_OF_DONE.md et ADR.md (tous dans docs/).

Ne pas mettre en place des automatisations ou procédures fictives par
simple copie de modèles. Adapter au contexte XS/S/M/L-XL.

## Conception modulaire
- Responsabilités principales des fonctions : À définir
- Modules nécessaires actuellement : À définir
- Fonctions publiques et contrats : À définir
- Frontières de logique pure / I/O : À définir
- Dépendances entre modules / risques de cycles : À définir
- Choix fonctions, composition ou classes : À justifier selon besoin
- Référence : `docs/MODULAR_DESIGN.md`

## Qualité
- Ruff : lint et format
- pytest : tests utiles
- Typage statique : selon risque/complexité
- Docstrings Python nouvelles/modifiées : **anglais**, PEP 257, style Google si utile
- Référence : `docs/DOCSTRINGS.md`
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

## Sécurité
- Données sensibles et secrets : À définir
- Entrées non fiables et permissions : À définir
- Risques spécifiques (SQL, fichiers, réseau, API) : À définir
- Contrôles/tests de sécurité utiles : À définir
- Référence : `docs/SECURITY.md`

## Configuration
- Sources de configuration (CLI, environnement, fichier) : À définir
- Valeurs requises, défauts sûrs et validation : À définir
- Gestion des secrets et environnements : À définir
- Référence : `docs/CONFIGURATION.md`

## Logging et diagnostic
- Niveau de log par défaut : À définir
- Événements importants à observer : À définir
- Données interdites dans les logs : À définir
- Identifiant de corrélation, métriques et alertes : selon le besoin
- Référence : `docs/LOGGING.md`

## Workflow IA et validation
- Fichiers du projet à examiner avant de coder : À définir
- Contraintes de compatibilité et de périmètre : À définir
- Vérifications réellement exécutables : À définir
- Format de compte rendu / décisions d'architecture : À définir
- Référence : `docs/AI_WORKFLOW.md`

## Commandes
- Installation : À définir
- Exécution : À définir
- Installation/synchronisation : `uv sync --locked` (si projet uv avec lockfile)
- Tests : `uv run --locked python -m pytest` (si pytest et lockfile configurés)
- Lint : `uv run --locked ruff check .` (si Ruff et lockfile configurés)
- Format : `uv run --locked ruff format --check .` (idem)
- Pour script XS sans projet/lockfile : `uv run script.py`
- Pour dépôt existant non uv : documenter ses commandes réelles

## Plan de mise en œuvre
1. Construire le plus petit chemin fonctionnel.
2. Tester les règles métier et erreurs importantes.
3. Refactoriser seulement si une duplication ou complexité réelle apparaît.
4. Ajouter des fonctionnalités uniquement selon les besoins validés.

## Questions ouvertes
- Aucune pour le moment.
