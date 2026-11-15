# S — CLI Python empaquetée

Exemple de petite calculatrice de puissance électrique, avec
**logique indépendante de la CLI** et tests d'erreur. `argparse`
suffit ici ; ne pas introduire Typer/Rich sans besoin réel.

## Exécuter avec uv

```bash
uv lock
uv sync --locked
uv run --locked example-cli 5 0.02
uv run --locked python -m pytest -q
uv run --locked ruff check .
uv run --locked ruff format --check .
uv build
```

La CLI affiche `0.1 W` pour 5 V et 0,02 A.
Renommer le package, les métadonnées et la commande du projet
avant réutilisation. **Commiter le `uv.lock` créé** dans le nouveau dépôt.

Pour GitHub Actions, copier
[le modèle central CI](../github/workflows/python-ci.yml)
dans `.github/workflows/python-ci.yml` du projet.
