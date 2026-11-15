# XS — Script Python autonome

Exemple minimal sans framework, package, `pyproject.toml` ou lockfile.

```bash
uv run main.py example.txt
uv run python -m unittest discover -s tests -v
```

Le programme compte les lignes non vides d'un fichier texte.
Remplacer `example.txt` par un chemin réel.

**À copier :** `main.py`, et `tests/` seulement si les tests
apportent de la valeur. Ne pas créer de structure S/M pour un script XS.
