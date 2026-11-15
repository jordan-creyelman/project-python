# Convention README.md — projets Python

Ce guide est la **source de vérité** pour rédiger et maintenir le
`README.md` des projets créés ou modifiés avec `project-python`.
Il concerne le **README de chaque application**, pas uniquement
le README du dépôt de standards.

## Objectif et règles non négociables

- Expliquer **à qui sert le projet, pourquoi et comment le lancer**.
- Rédiger en **français par défaut**, sauf langue explicitement choisie
  par le projet. Garder les noms de fichiers, commandes, options CLI et
  identifiants Python dans leur forme technique réelle.
- Décrire **uniquement les fonctionnalités implémentées**. Les idées
  futures et les limites doivent être séparées du fonctionnement actuel.
- Donner des commandes **copiables et adaptées à la vraie structure**
  du dépôt : entry points, chemins, options, version Python et outils.
- Préférer `uv` pour les **nouveaux** projets selon
  [UV_WORKFLOW.md](UV_WORKFLOW.md), sans modifier le gestionnaire d'un
  dépôt existant uniquement pour harmoniser le README.
- Ne pas présenter une CI écrite comme réussie, ni un test non exécuté
  comme vérifié. Distinguer clairement *prévu*, *codé* et *testé*.
- Ne jamais écrire d'identifiant secret, token, mot de passe réel,
  clé privée ni valeur d'environnement sensible dans un exemple.
- Conserver une entrée de lecture claire : pas de badge non vérifié,
  de marketing vague, ni de sections vides ou décoratives.

## Structure recommandée, proportionnée à la taille

| Taille | Minimum utile | Compléments seulement si nécessaires |
| --- | --- | --- |
| **XS** | Titre, objectif en 1–2 phrases, commande d'exécution, entrées/sorties ou limites pertinentes | Test ciblé ou avertissement de sécurité |
| **S** | Présentation, fonctionnalités réelles, prérequis, installation, utilisation avec exemples, tests | Configuration, sécurité et limitations si applicables |
| **M** | Comme S, plus configuration, structure d'ensemble, tests/CI, limites et précautions pertinentes | Décisions, déploiement, références vers `docs/` |
| **L/XL** | Page d'accueil courte : objectif, démarrage rapide et liens vers la documentation | Guides détaillés, architecture, exploitation, ADR et politique de sécurité dans `docs/` |

Cette table est **un guide éditorial**, pas un nombre de titres à
imposer mécaniquement. Une bibliothèque peut nécessiter un exemple
d'import plutôt qu'une commande CLI ; une application sans configuration
n'a pas besoin d'une section `.env`.

## Exemples de commandes

Pour un nouveau projet S/M **ayant réellement `uv.lock`** :

```bash
uv sync --locked
uv run --locked <commande-reelle> --help
uv run --locked python -m pytest -q
uv run --locked ruff check .
uv run --locked ruff format --check .
```

Remplacer `<commande-reelle>` par le **point d'entrée réel** défini dans
`pyproject.toml`. Ne pas copier littéralement un placeholder dans
un README livré. Pour XS, un simple `uv run main.py <fichier-existant>`
suffit si l'exemple reflète le code. Pour un projet existant utilisant
`pip`/`pipx`/Poetry, documenter son installation actuelle, sans
prétendre qu'il utilise uv.

### Variables d'environnement

Ajouter une section *Configuration* seulement si l'application lit
réellement ces valeurs. Préciser les noms, valeurs obligatoires, défauts
et unités. Utiliser un `.env.example` **sans secret** ; ne pas affirmer
que `uv` charge `.env` automatiquement. Suivre
[CONFIGURATION.md](CONFIGURATION.md).

### Tests, statut et CI

Expliquer **comment exécuter** les vérifications localement et, si
pertinent, pointer vers le workflow réel. Ne pas inventer de résultat
ou de pourcentage de couverture. Les résultats rapportés doivent
correspondre à une exécution réellement observée.

### Sécurité et limites

Documenter les précautions proportionnées au risque : données
sensibles, droits sur les fichiers, réseau, matériel, API et
autorisations de test si nécessaires. Pour un projet de sécurité
ou de pentest, préciser le **périmètre autorisé** et les limites
de l'outil sans déclarer une analyse exhaustive.

## Workflow du Tech Lead

1. **Avant de rédiger :** lire `pyproject.toml`, la CLI/API, les
   tests, la configuration et les commandes réellement disponibles.
2. **Créer le README** dès le MVP, avec le strict nécessaire selon XS/S/M/L.
3. **Pendant une modification :** actualiser le README si le point
   d'entrée, les paramètres, dépendances, configuration, comportements
   ou limites changent ; retirer les instructions obsolètes.
4. **Avant de livrer :** vérifier les liens et, quand l'environnement
   le permet, essayer les commandes documentées ; signaler celles
   qui n'ont pas pu être exécutées.
5. **Ne pas remplacer** le README d'un dépôt existant par un modèle
   générique : préserver le contexte, la langue et le public du projet.

## Checklist de revue README

- [ ] L'objectif et les fonctionnalités **actuelles** sont clairs.
- [ ] La taille et les sections sont proportionnées au projet.
- [ ] Les noms de commandes, fichiers, options et unités sont exacts.
- [ ] Les étapes d'installation correspondent au gestionnaire utilisé.
- [ ] La configuration est documentée uniquement si elle existe.
- [ ] Aucun secret, faux statut de CI ou résultat inventé.
- [ ] La procédure de test correspond aux scripts réellement présents.
- [ ] Les limites et risques importants sont expliqués.
- [ ] Les liens relatifs fonctionnent et les exemples ne sont pas périmés.

Voir les [modèles XS/S/M](../templates/README.md), la
[Definition of Done](DEFINITION_OF_DONE.md) et la
[stratégie de tests](TESTING_STRATEGY.md).
