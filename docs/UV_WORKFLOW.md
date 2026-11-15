# Convention uv — gestionnaire Python par défaut

> **Décision : utiliser [uv](https://docs.astral.sh/uv/) comme outil
> Python privilégié** pour les nouveaux projets : versions Python,
> environnements virtuels, dépendances, exécution, tests et builds.
> Le choix doit rester proportionné à XS/S/M/L-XL et compatible avec
> les contraintes d'un dépôt existant. uv ne remplace ni Python ni Ruff.

## 1. Choix par défaut du Tech Lead

- Pour **un nouveau projet**, proposer uv comme flux de travail canonique.
- Pour **un dépôt existant**, examiner son `pyproject.toml`, son outil,
  ses lockfiles, sa CI et ses instructions avant toute migration. Si Poetry,
  pip, pip-tools ou un autre gestionnaire est déjà utilisé, **ne pas
  mélanger deux sources de vérité**. Présenter une migration explicite
  avec validation et retour arrière si elle est pertinente.
- Respecter un environnement où uv ne peut pas être installé ; indiquer
  une commande de secours seulement lorsqu'elle est nécessaire.
- Garder une **seule méthode d'installation documentée comme principale**,
  avec uv pour les nouveaux projets.
- Utiliser `uv run` pour les commandes du projet, sans demander
  d'activer manuellement `.venv`.

## 2. Stratégie selon la taille

| Taille | Usage recommandé |
| --- | --- |
| **XS** — script simple | `uv run script.py` ; `uvx` pour un outil ponctuel. Aucun `pyproject.toml` ou lockfile imposé pour un script autonome sans dépendances. |
| **S** — CLI ou bibliothèque | `uv init` si projet neuf, `pyproject.toml`, `uv add` et `uv run`. Utiliser `uv.lock` quand un environnement de travail reproductible apporte une valeur. |
| **M** — application/API | `uv.lock` commité, `uv sync --locked` en CI, dépendances de développement groupées, tests via `uv run --locked`. |
| **L/XL** — gros produit/équipes | Même base, avec matrices CI, règles de mise à jour, validation de sécurité, reproductibilité et workspaces uv **si les modules le justifient**. |

## 3. Commandes recommandées

**Installation :** installer uv depuis la [documentation officielle](https://docs.astral.sh/uv/getting-started/installation/). Vérifier `uv --version`. Ne pas supposer que uv est disponible sans vérification.

### Nouveau projet avec dépendances

```bash
uv init maker-example
cd maker-example
uv python pin 3.12           # Si cette version est adaptée au projet
uv add typer rich            # Exemple seulement si le besoin le justifie
uv add --dev pytest ruff     # Groupe de développement (nouveau projet)
uv lock                      # Génère/met à jour uv.lock
uv sync --locked
uv run --locked pytest
uv run --locked ruff check .
uv run --locked ruff format --check .
uv build                     # Seulement pour un paquet à distribuer
```

### Projet existant déjà configuré avec uv

```bash
uv sync --locked
uv run --locked python -m pytest
uv run --locked ruff check .
uv run --locked ruff format --check .
```

Le drapeau `--locked` exige un `uv.lock` présent et cohérent ; **ne pas
l'utiliser pour un simple script sans lockfile**.

### Petit script XS sans projet

```bash
uv run script.py
uvx ruff check script.py    # Facultatif, exécution ponctuelle d'un outil
```

### Entretenir les dépendances

```bash
uv add requests                  # Exemple : ajout justifié d'une dépendance
uv remove requests               # Retrait
uv lock --upgrade-package typer  # Mise à jour ciblée et contrôlée
uv sync --locked                 # Reproduction de l'environnement
```

Les commandes `uv add`/`uv remove` et `uv run` peuvent actualiser le
lockfile et l'environnement ; vérifier le diff du lockfile avant commit.

## 4. Fichiers et bonnes pratiques

- `pyproject.toml` : métadonnées et dépendances directes.
- `[dependency-groups]` avec un groupe `dev` par défaut pour les
  nouveaux projets uv, via `uv add --dev`. Respecter les extras
  `[project.optional-dependencies]` déjà utilisés par un autre projet ;
  si le projet utilise un extra `dev`, lancer par exemple
  `uv sync --extra dev --locked` et adapter la CI.
- `uv.lock` : commiter pour les projets uv gérés en équipe ou déployés
  (et pour les outils S quand la reproductibilité compte). Un lockfile
  ne remplace pas les contraintes de compatibilité publiques d'une
  bibliothèque distribuée.
- `.venv/` : toujours ignorer dans Git.
- `.python-version` : facultatif, utile pour choisir l'interpréteur
  local ; ne pas l'imposer si le projet teste plusieurs versions Python.
- Aucune obligation de créer un workspace ou de packager un script XS.
- Lors d'une migration, supprimer les lockfiles concurrents **seulement
  après validation** de la nouvelle installation et de la CI.
- Ne pas confondre `uv lock --check` (cohérence du lockfile) avec un
  contrôle de vulnérabilités ; auditer la sécurité séparément.

## 5. CI GitHub Actions

Le [modèle CI](../templates/github/workflows/python-ci.yml) utilise
`astral-sh/setup-uv` et les commandes `uv sync --locked` / `uv run
--locked`. Copier ce modèle uniquement dans un projet exécutable
avec `pyproject.toml`, `uv.lock` et les outils de test déclarés. Vérifier
le support Python et adapter les groupes de dépendances et extras.

Le workflow [docs-check.yml](../.github/workflows/docs-check.yml)
vérifie les documents et les exemples sans transformer `project-python`
en application déployable. Les pipelines applicatifs restent réservés
aux dépôts qui utilisent les modèles. Respecter
[CI_CD_STRATEGY.md](CI_CD_STRATEGY.md).

## Sources officielles

- [Installation](https://docs.astral.sh/uv/getting-started/installation/)
- [Projets et commandes](https://docs.astral.sh/uv/guides/projects/)
- [Lockfile et synchronisation](https://docs.astral.sh/uv/concepts/projects/sync/)
- [Intégration GitHub Actions](https://docs.astral.sh/uv/guides/integration/github/)

**Règle directrice : uv est le défaut des nouveaux projets, pas une
raison de casser un projet existant.**
