# Automatiser la création et la validation des projets Python

Ce guide concerne les **nouveaux projets**. Ne jamais exécuter le générateur
dans un dépôt existant sans en avoir vérifié les fichiers et les contraintes.

## 1. Générateur XS/S/M

Depuis le clone de project-python, avec uv installé :

```bash
uv run --no-project python scripts/create_project.py line-counter --size xs
uv run --no-project python scripts/create_project.py sensor-cli --size s
uv run --no-project python scripts/create_project.py task-manager --size m

# Configuration d'environnement uniquement sur demande
uv run --no-project python scripts/create_project.py sensor-cli --size s --with-env
uv run --no-project python scripts/create_project.py task-manager --size m --with-env

# Alternative : choisir le dossier parent
uv run --no-project python scripts/create_project.py sensor-cli --size s --parent ~/projects

# Squelette uniquement (aucune résolution de dépendances, aucune CI)
uv run --no-project python scripts/create_project.py sensor-cli --size s --no-ci --no-lock
```

Un nom est accepté uniquement s'il correspond à `sensor-cli` (minuscules,
chiffres et tirets simples). Le générateur **refuse les chemins dangereux,
les dossiers déjà existants et l'écrasement de fichiers** ; en cas d'échec
d'`uv lock`, le dossier temporaire est supprimé. Il n'accède pas à GitHub.

| Taille | Résultat par défaut |
| --- | --- |
| XS | Script autonome, test unittest, marqueur de standards ; pas de lock ni CI |
| S | Package/CLI renommé, README, tests, Ruff/pytest, uv.lock et CI |
| M | Package modulaire renommé, README, tests, Ruff/pytest, uv.lock et CI |

Le générateur fournit un README initial en français, avec les
commandes de ses modèles. Il doit être **adapté au besoin réel**
du programme avant livraison : [README_STANDARDS.md](README_STANDARDS.md).

Le fichier `.project-python.toml` enregistre la taille et la version
des standards utilisés ; il n'installe aucun outil à lui seul.
Avec `--with-env` pour S/M, il précise `environment-config = true`.
Le contrôle portable vérifie alors `config.py`, `.env.example`, les
tests de configuration et les règles d'ignorance Git. Le générateur
ne crée jamais de `.env` réel ni de secret.
Les projets générés S/M embarquent leur propre
`scripts/check_project.py` et une CI qui lance ce contrôle.

## 2. Vérifier un projet existant

Le contrôle portable accepte les tailles `xs`, `s`, `m` et `l` :

```bash
python scripts/check_project.py --path . --size s
python scripts/check_project.py --path . --size s --strict
python scripts/check_project.py --path . --size m --json
```

Lorsqu'un `.project-python.toml` est présent, `--size` est facultatif.
Les erreurs rendent un code de sortie non nul. Avec `--strict`, les
recommandations deviennent également bloquantes. La vérification couvre
les fichiers attendus, métadonnées, dépendances dev, lockfile uv, CI
et syntaxe Python. **Elle ne prouve pas** que les tests passent, que les
docstrings sont correctement rédigées ou qu'un framework est maintenu.

Pour un projet existant utilisant pip/Poetry, les règles uv ne doivent
pas être appliquées sans migration choisie ; préférer une revue manuelle
des différences et adapter le contrôleur plutôt que fausser les résultats.

## 3. GitHub Actions

Le générateur S/M installe
[python-ci.yml](../templates/github/workflows/python-ci.yml) dans
`.github/workflows/` et un script local de contrôle des conventions.
La CI exécute uv, Ruff, pytest et le validateur statique à chaque push
sur les branches configurées et à chaque PR. Le fichier `uv.lock`
est généré avant le premier commit, pour éviter une CI non fonctionnelle.

XS peut rester un simple script : ne pas ajouter une CI par principe.
Un projet L/XL mérite un cadrage de ses modules et n'est pas généré
automatiquement par un modèle simpliste.

## 4. Limites et sécurité

- Une CI écrite ne remplace ni la revue des PR ni la validation sur le matériel.
- La génération résout les dépendances via uv ; elle peut nécessiter le réseau.
- Les scripts ne créent ni dépôt GitHub, ni secrets, ni règles de protection.
- Un projet déjà existant doit conserver ses conventions tant qu'une migration
  n'a pas été validée.
- Les versions des frameworks et leur sécurité nécessitent une vérification
  spécifique au projet.

Voir [UV_WORKFLOW.md](UV_WORKFLOW.md),
[CI_CD_STRATEGY.md](CI_CD_STRATEGY.md) et
[RELEASE_PROCESS.md](RELEASE_PROCESS.md).
