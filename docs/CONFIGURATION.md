# Configuration Python — variables d'environnement

Ce document est la **source de vérité** pour la configuration d'exécution.
La configuration dépend du projet et du déploiement : **aucun `.env`
n'est obligatoire** pour un programme qui n'en a pas besoin.

## 1. Convention de nommage

- Noms en **anglais, majuscules, `UPPER_SNAKE_CASE`**.
- Préfixe stable propre au projet : `<PROJECT>_<SETTING>`.
- Exemple : `SENSOR_CLI_LOG_LEVEL` et `SENSOR_CLI_TIMEOUT_SECONDS`.
- Éviter des noms trop génériques comme `DEBUG` ou `TOKEN` qui peuvent
  entrer en conflit avec un autre service.
- Indiquer les unités : `TIMEOUT_SECONDS`, `RETRY_COUNT`, etc.
- Pour une clé d'API nécessaire, utiliser l'environnement ou un
  gestionnaire de secrets, jamais une valeur réelle dans les exemples.

## 2. Principes

1. Séparer **configuration**, code, données et secrets.
2. Préférer les arguments CLI explicites pour les options choisies
   à chaque exécution ; utiliser l'environnement pour les paramètres
   dépendant du déploiement.
3. Lire les variables à **une seule frontière d'entrée**, puis passer
   un `Settings` immuable ou les valeurs nécessaires aux fonctions métier.
4. Définir et tester la **priorité des sources par projet** : par exemple
   arguments CLI explicites > environnement > défauts sûrs.
5. Valider types, plages, unités et variables obligatoires au démarrage.
   Variable absente et variable vide peuvent demander des traitements différents.
6. Rendre les erreurs compréhensibles **sans afficher de valeur sensible**.
7. Ne pas charger `.env` implicitement ni installer un framework de
   configuration lorsque `os.environ` et `dataclass` suffisent.

## 3. `.env`, `.env.example` et secrets

Un `.env` est un **fichier local de confort, pas un coffre-fort**.
Dans le `.gitignore` du projet :

```gitignore
.env
.env.*
!.env.example
```

Commiter **uniquement** `.env.example` avec des valeurs publiques ou
fictives. Ne jamais y placer un vrai token, mot de passe ou certificat.
Ne pas commiter `.env`, `.env.local`, `.env.production` ni les secrets CI.
En production, préférer un gestionnaire de secrets et le principe du
moindre privilège. Les variables d'environnement ne suffisent pas à
protéger les secrets des journaux, processus ou dumps mémoire.

Charger explicitement un fichier local avec uv :

```bash
cp .env.example .env
uv run --env-file .env --locked python -m my_project
```

Ne pas supposer que `uv run` charge `.env` automatiquement. Adapter
la commande au projet réel ; utiliser `--locked` uniquement si
un `uv.lock` valide existe.

## 4. Modèle optionnel testé

Le [modèle d'environnement](../templates/config/README.md) comprend :

- [`config.py`](../templates/config/config.py) : `Settings` immuable,
  `os.environ`, validation explicite, sans dépendance supplémentaire.
- [`test_config.py`](../templates/config/test_config.py) : tests de
  valeurs manquantes, incorrectes, hors limites, overrides et erreurs
  qui ne répètent pas les valeurs sensibles.
- [`.env.example`](../templates/config/.env.example) : exemples sûrs.

Ce modèle n'est **pas installé par défaut**. Pour les nouveaux projets
S/M qui ont besoin de configuration :

```bash
uv run --no-project python scripts/create_project.py sensor-cli --size s --with-env
uv run --no-project python scripts/create_project.py task-manager --size m --with-env
```

Le générateur adapte le préfixe de `PROJECT_` en `SENSOR_CLI_` ou
`TASK_MANAGER_`. Il ajoute les tests mais **ne relie pas automatiquement**
la configuration au comportement de la CLI, qui doit rester une
décision propre à l'application.

## 5. Tests de configuration

- Défauts lorsque les variables optionnelles sont absentes.
- Erreur lisible si une variable obligatoire manque, le cas échéant.
- Valeurs mal formées, chaînes vides, types invalides et plages.
- Injection d'environnement de test via `monkeypatch` ou mapping.
- Absence de secrets dans les erreurs, traces et logs.
- Priorité des sources quand plusieurs sources sont disponibles.

## 6. Taille du projet

| Taille | Recommandation |
| --- | --- |
| XS | Constantes ou arguments CLI, aucun `.env` obligatoire. |
| S | `os.environ` et validation ciblée, `--with-env` uniquement si utile. |
| M | `Settings` typé et immuable, validation au démarrage et séparation dev/test/prod. |
| L/XL | Gestionnaire de secrets et politiques de déploiement selon le risque. |

Voir aussi [SECURITY.md](SECURITY.md) et
[MODULAR_DESIGN.md](MODULAR_DESIGN.md).
