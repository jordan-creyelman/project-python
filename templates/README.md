# Templates de projets Python avec uv

Ces **trois exemples exécutables** illustrent les conventions sans imposer
une architecture ou un framework inutile. Choisir la taille selon le besoin,
pas selon le nombre de fichiers. Voir [les sources de vérité](../docs/STANDARDS_INDEX.md).

| Modèle | Usage | Code et vérification |
| --- | --- | --- |
| [XS](xs/README.md) | Script autonome sans dépendance | `uv run main.py` ; unittest facultatif |
| [S](s/README.md) | Petite CLI empaquetée, logique séparée | `uv sync`, `uv run pytest`, Ruff |
| [M](m/README.md) | Application légère à séparation domaine/I/O | `uv sync`, `uv run pytest`, Ruff |

## Créer automatiquement le projet

Depuis la racine de `project-python`, avec uv installé :

```bash
uv run --no-project python scripts/create_project.py sensor-cli --size s
uv run --no-project python scripts/create_project.py task-manager --size m
uv run --no-project python scripts/create_project.py line-counter --size xs
```

Pour S/M, le générateur **génère `uv.lock`, les contrôles
des conventions et la CI**, en renommant le package et les imports.
Il refuse les dossiers existants et n'accède pas à GitHub.
Utiliser `--no-ci --no-lock` pour un simple squelette sans dépendances
résolues et sans workflow CI ; il faudra terminer ces étapes plus tard.

Lire [PROJECT_AUTOMATION.md](../docs/PROJECT_AUTOMATION.md).

## Créer son propre dépôt à partir d'un modèle

1. Copier **le contenu** du dossier souhaité dans le nouveau dépôt.
2. Renommer le package `example_cli` ou `example_app` et mettre à
   jour `pyproject.toml`, README et points d'entrée si nécessaire.
3. Pour S/M, exécuter `uv lock`, puis **commiter `uv.lock`** et
   lancer `uv sync --locked`.
4. Copier le [workflow CI réutilisable](github/workflows/python-ci.yml)
   dans `.github/workflows/python-ci.yml` **après** génération du
   lockfile ; adapter versions Python, branches et groupe dev.
5. Consulter [UV_WORKFLOW.md](../docs/UV_WORKFLOW.md) et
   [CI_CD_STRATEGY.md](../docs/CI_CD_STRATEGY.md).
6. Utiliser le workflow GitHub de taille adaptée ; ne pas créer `dev`
   pour un petit script.

Les fichiers `uv.lock` ne sont pas inclus dans S/M pour éviter un
verrouillage périmé dans un modèle générique ; ils doivent être **générés
et commités dans le projet créé**. La CI de `project-python` vérifie la
capacité des exemples à générer leur environnement et à passer leurs tests.

**Aucune publication PyPI ou déploiement automatique n'est fourni.**
