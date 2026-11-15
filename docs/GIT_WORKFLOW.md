# Convention Git et GitHub — stratégie proportionnée

> **Objectif** : garder un historique professionnel et des livraisons fiables sans
> imposer un processus lourd aux petits projets Python. Les **noms de branches,
> messages de commit et titres de pull requests sont en anglais**. Les explications
> et la documentation peuvent rester en français.
>
> Ce guide définit une **convention**, pas une configuration automatique de GitHub.
> Appliquer la stratégie à chaque dépôt selon sa taille, son équipe et son risque.
> Ne pas créer `dev` ni modifier les protections d'un dépôt existant sans accord.

## 1. Choisir la stratégie selon la taille

La taille XS/S/M/L-XL mesure la complexité et le risque, pas seulement le nombre
de fichiers. Le Tech Lead annonce le choix au cadrage et le réévalue si nécessaire.

| Taille | Branches | Intégration / livraison | Vérifications |
| --- | --- | --- | --- |
| **XS** — script, essai | `main` ; branche temporaire facultative | Commit direct accepté pour travail solo et faible risque | Vérification manuelle et tests utiles |
| **S** — CLI, petite bibliothèque | `main` + `feature/*`, `fix/*` ; `dev` facultative | Petites PR vers `main` recommandées ; commit direct possible si solo/faible risque | Ruff + pytest si configurés, CI légère conseillée |
| **M** — API, application maintenue | `main` stable + `dev` d'intégration + branches temporaires | PR vers `dev`, puis PR de livraison `dev` → `main` | CI lint/tests requise avant fusion ; revue si équipe |
| **L/XL** — produit, plusieurs équipes ou risques élevés | `main` + `dev` + branches temporaires ; `release/*` seulement si gel nécessaire | PR obligatoires, livraison contrôlée, tags, plan de retour arrière | CI complète proportionnée, revues, protections, tests de régression |

**Principe** : `main` existe toujours et représente l'état stable. `dev` est la
branche d'intégration **uniquement quand elle est justifiée** (par défaut M/L).
Ne pas créer `dev` automatiquement pour un script XS ou une petite CLI S.
Une petite application à haut risque peut nécessiter plus de contrôles qu'une
application volumineuse mais expérimentale.

## 2. Noms de branches — toujours en anglais

| Branche | Rôle | Exemple |
| --- | --- | --- |
| `main` | Version stable / livrable ; branche par défaut | `main` |
| `dev` | Intégration continue des fonctionnalités avant livraison | `dev` |
| `feature/<short-description>` | Nouvelle fonctionnalité | `feature/led-calculator` |
| `fix/<short-description>` | Correction normale | `fix/invalid-voltage-input` |
| `hotfix/<short-description>` | Correction urgente d'une version publiée | `hotfix/startup-crash` |
| `docs/<short-description>` | Documentation | `docs/installation-guide` |
| `refactor/<short-description>` | Restructuration sans changement fonctionnel | `refactor/cli-commands` |
| `test/<short-description>` | Tests | `test/ohm-edge-cases` |
| `chore/<short-description>` | Maintenance/outillage | `chore/update-dependencies` |
| `release/vX.Y.Z` | Stabilisation facultative avant livraison | `release/v1.2.0` |

Règles : minuscules ASCII, mots séparés par des tirets, préfixe explicite,
description courte et spécifique ; éviter espaces, accents, dates arbitraires
et noms génériques comme `test2` ou `new-branch`. Ajouter un numéro d'issue
si utile : `feature/42-led-calculator`. Supprimer les branches temporaires
après fusion. Ne jamais forcer un push ni supprimer `main`/`dev` par routine.

## 3. Commits — Conventional Commits, en anglais

Format attendu :

```text
<type>(<scope>): <imperative summary>
```

- `type` en minuscules ; `scope` facultatif, court et lié au module.
- Description **en anglais**, à l'impératif, précise, sans point final ;
  viser une première ligne de **72 caractères maximum**.
- Un commit = une intention cohérente ; ne pas mélanger refactor, bug et
  fonctionnalité sans raison.
- Corps facultatif pour expliquer **pourquoi**, risques et migrations ;
  séparer du titre par une ligne vide.
- Une rupture d'API s'indique avec `!` et, si nécessaire, un paragraphe
  `BREAKING CHANGE:` dans le corps.

Types acceptés :

| Type | Usage |
| --- | --- |
| `feat` | Fonctionnalité |
| `fix` | Correction de bug |
| `docs` | Documentation |
| `refactor` | Refactorisation sans changement fonctionnel |
| `test` | Tests |
| `perf` | Performance |
| `build` | Dépendances ou packaging |
| `ci` | Automatisation CI/CD |
| `chore` | Maintenance |
| `revert` | Annulation d'un changement |

Exemples :

```text
feat(cli): add interactive calculator
fix(led): reject negative current
test(divider): cover zero resistance
docs(git): define branching conventions
ci: run lint and tests on pull requests
refactor(core): isolate calculation logic
feat(api)!: remove deprecated voltage endpoint
```

À éviter : `update`, `fix stuff`, `wip`, `final version`,
`ajout calculateur`. Les messages de commits, y compris ceux produits
par un assistant IA, respectent ces règles. Les titres des PR suivent
idéalement le même format ; le corps peut être en français.

## 4. Workflow de développement

### XS / S : flux simple

1. Partir de `main` à jour.
2. Pour un changement significatif, créer `feature/*` ou `fix/*`.
3. Commiter en anglais, exécuter les contrôles pertinents.
4. Ouvrir une PR courte vers `main` si utile ; privilégier **Squash and merge**
   pour conserver un historique lisible.
5. Supprimer la branche après fusion.

```bash
git switch main
git pull --ff-only
git switch -c feature/led-calculator
# develop, test and commit
git add .
git commit -m "feat(led): add resistor calculator"
git push -u origin feature/led-calculator
# Open a pull request targeting main
```

Le commit direct sur `main` reste acceptable pour XS et S solo à faible
risque ; ne pas multiplier les PR sans bénéfice réel.

### M / L / XL : intégration puis livraison

1. Créer `dev` une fois, à partir de `main`, lors de l'adoption du workflow.
2. Partir de `dev` à jour pour chaque `feature/*`, `fix/*`, `docs/*`, etc.
3. Ouvrir une PR vers `dev` ; exécuter CI et revue adaptée au risque.
4. Fusionner les PR de fonctionnalités par **Squash and merge** dans `dev`.
5. Pour publier, ouvrir une PR **`dev` → `main`**. Après validation, utiliser
   un **merge commit** pour conserver la relation entre les branches, puis taguer
   le commit publié sur `main`.
6. Resynchroniser `dev` depuis `main` si nécessaire (notamment après hotfix).
   Ne pas écraser l'historique partagé par un rebase/force-push.

```bash
git switch dev
git pull --ff-only
git switch -c feature/led-calculator
# develop, test and commit
git add .
git commit -m "feat(led): add resistor calculator"
git push -u origin feature/led-calculator
# Open a pull request targeting dev
```

Une branche `release/vX.Y.Z` n'est utile que si une stabilisation longue
ou des corrections de release doivent avancer en parallèle du développement.
Sans ce besoin, une PR `dev` → `main` suffit. Si l'on conserve des merge
commits pour les releases, **ne pas imposer « Require linear history » à
`main`**, car cette protection refuserait ces fusions.

### Hotfix de production

1. Créer `hotfix/*` **depuis `main`** (pas `dev`).
2. Corriger le strict nécessaire et ajouter un test de régression si possible.
3. Ouvrir une PR vers `main`, vérifier, fusionner et publier un tag correctif.
4. Reporter la correction sur `dev` par PR/synchronisation pour éviter
   qu'une prochaine release ne réintroduise le bug.

## 5. Pull requests, revues et CI

Chaque PR significative devrait indiquer : **What changed**, **Why**,
**How tested**, **Risks / rollback** (si pertinent) et l'issue liée.
Préférer des PR petites, cohérentes et révisables.

| Taille | Contrôles et protections recommandés |
| --- | --- |
| XS | Tests manuels ou automatisés pertinents ; pas de PR/CI imposée |
| S | CI Ruff + pytest si outillé ; PR recommandée, revue non obligatoire en solo |
| M | Protéger `main` et `dev` ; PR et statuts CI requis ; au moins une revue si plusieurs contributeurs |
| L/XL | Protections `main`/`dev`, CI requise, revues par pairs et CODEOWNERS si utile ; revues renforcées pour changements critiques |

Configurer dans GitHub les **branch protection rules** ou **rulesets**
selon les permissions et l'offre disponibles. Interdire les force-pushes
et suppressions des branches protégées, exiger les checks réellement
présents et ne pas imposer une approbation externe impossible pour un
développeur solo. Une convention écrite ne protège **pas** une branche
tant que les règles GitHub ne sont pas configurées.

Documentation officielle :
- [Protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- [Rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)

## 6. Releases, versions et traçabilité

- Taguer les versions livrées sur `main` : `v0.1.0`, `v1.0.0`,
  `v1.0.1` ; utiliser **SemVer** quand le projet distribue des versions.
- Documenter les changements significatifs (release notes ou CHANGELOG
  selon la taille). Pour XS, les tags/releases sont facultatifs.
- En M/L, publier uniquement après les checks et la validation des risques.
- En cas de régression, privilégier un `revert` ou un correctif traçable
  plutôt qu'une réécriture d'historique partagé.

## 7. Consignes aux assistants IA

Avant toute action GitHub :
1. Inspecter les branches, le dépôt, ses règles et son CI ; ne pas supposer
   que `dev` existe ou qu'une branche est protégée.
2. Déterminer la taille du projet et annoncer le workflow retenu.
3. Respecter les conventions existantes si elles diffèrent ; proposer une
   migration avant de changer les pratiques.
4. Nommer **branches, commits et titres de PR en anglais** et appliquer
   Conventional Commits aux commits créés.
5. Utiliser la branche de base appropriée : `main` pour XS/S,
   `dev` pour M/L quand elle existe, `main` pour les hotfixes.
6. Ne jamais créer `dev`, changer la branche par défaut, modifier
   protections/rulesets, forcer un push, fusionner une PR ou publier une
   release **sans demande ou validation explicite**.
7. Rapporter exactement ce qui a été changé, les contrôles exécutés et
   ce qui reste à faire.

**Règle directrice : la fiabilité et la clarté priment sur la complexité
du processus.**
