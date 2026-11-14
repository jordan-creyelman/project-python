# project-python

Base de contexte pour développer des projets Python **de toute taille** sans surarchitecture.

## Fichiers
- [AGENTS.md](AGENTS.md) : instructions pour assistants de code et conventions générales (PEP 8, PEP 257, KISS, SOLID, YAGNI, DRY).
- [docs/PROJECT_CONTEXT.md](docs/PROJECT_CONTEXT.md) : modèle à compléter pour chaque projet (objectif, taille, contraintes, architecture, tests).

## Comment commencer un projet
1. Créer un dossier pour le projet (par ex. `projects/mon-outil/`) ou utiliser ces règles dans un dépôt Python dédié.
2. Choisir la taille **XS**, **S**, **M** ou **L/XL** selon les besoins, pas seulement les lignes de code.
3. Copier le modèle de contexte dans le projet et remplir uniquement les sections utiles.
4. Demander à l'assistant : « Lis AGENTS.md et le contexte du projet, puis implémente le MVP avec la plus petite architecture adaptée. »
5. Garder les tests, la documentation et les dépendances proportionnels à la complexité.

## Philosophie
**Simple d'abord, structuré quand nécessaire.** Les exemples de structures sont des guides, pas des dossiers à créer obligatoirement. Le dépôt ne contient pas de squelette applicatif imposé.

## Exemple de demande
> Crée un outil CLI Python pour renommer des fichiers. Taille S. Respecte AGENTS.md et docs/PROJECT_CONTEXT.md. Utilise pathlib, Ruff et pytest. Commence par le MVP et n'ajoute pas de couche repository/service sans besoin.
