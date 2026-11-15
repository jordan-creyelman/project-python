# Changelog — project-python standards

Les versions concernent **les conventions et modèles de ce dépôt**, pas les
applications Python qui les adoptent. Les changements futurs sont consignés
ici avant publication d'une nouvelle version documentaire.

## [Unreleased]

### Planned
- Poursuivre les améliorations après retour d'expérience des projets réels.

## [0.3.0] - 2026-11-15

### Added
- Convention de nommage des variables d'environnement et règles
  de validation, priorité de configuration et protection des secrets.
- Option `--with-env` du générateur S/M : `config.py`, `.env.example`
  et tests pytest, avec préfixes propres à chaque projet.
- Contrôle automatique des fichiers de configuration et tests CI.

### Changed
- Exclusion systématique des fichiers `.env` locaux dans les modèles.
- Version des standards 0.2.0 → 0.3.0 ; aucune release publiée automatiquement.

## [0.2.0] - 2026-11-15

### Added
- Générateur XS/S/M via uv : renommage automatique du package, README,
  configuration de conventions, lockfile et CI par défaut pour S/M.
- Contrôle portable des standards des projets selon leur taille,
  intégré aux workflows des projets générés.
- Tests unitaires et smoke tests des projets générés.
- Procédure de publication GitHub Release manuelle, vérifiée
  par VERSION, changelog et CI réussie sur le commit publié.

### Changed
- Documentation du générateur, de la validation et des releases.
- Bump documentaire 0.1.0 → 0.2.0 (aucun tag créé automatiquement).

## [0.1.0] - 2026-11-15

### Added
- Standards Python XS/S/M/L-XL, cadrage Tech Lead, GitHub, CI/CD et sécurité.
- Gestionnaire uv par défaut, sélection de bibliothèques, docstrings en anglais.
- Modèles exécutables de démarrage XS, S et M, sans imposer un framework.
- Validation automatique des liens Markdown, YAML, TOML et syntaxe Python.
- Vérification CI des exemples avec uv, pytest et Ruff.

### Changed
- Identification des documents de référence afin de réduire les incohérences.

Cette version **documentaire** ne crée ni tag Git ni GitHub Release.
