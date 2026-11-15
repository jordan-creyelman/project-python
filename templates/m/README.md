# M — Application modulaire Python

Exemple léger de gestion de tâches en JSON. Il montre une séparation
**domaine → service → stockage** sans framework web ni base de données.

## Exécuter avec uv

```bash
uv lock
uv sync --locked
uv run --locked example-app --file tasks.json "Review schematic"
uv run --locked python -m pytest -q
uv run --locked ruff check .
uv run --locked ruff format --check .
uv build
```

Le fichier `tasks.json` est créé au chemin indiqué par l'utilisateur.
Les fonctions métier n'effectuent aucune I/O.

Les nouveaux projets issus de ce modèle doivent **commiter leur
`uv.lock`**, puis adapter la CI de
[templates/github/workflows/python-ci.yml](../github/workflows/python-ci.yml).
N'ajouter d'autres couches qu'en cas de besoin démontré.
