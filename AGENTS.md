# AGENTS.md — Contexte de développement Python

## Mission
Ce dépôt sert de base réutilisable pour créer des projets Python de tailles différentes.
Avant toute modification, lire ce fichier, puis `docs/PROJECT_CONTEXT.md` s'il existe.
Répondre et documenter en français, sauf convention contraire d'un projet.

## Priorités (dans cet ordre)
1. Fonctionnalité correcte, sécurité et simplicité.
2. Besoin réel et périmètre demandé.
3. Lisibilité, tests et maintenabilité.
4. Cohérence avec l'existant.
5. Extensibilité uniquement si justifiée.

## Principes permanents
- **PEP 8** : noms explicites, imports organisés, formatage cohérent, lignes de 88 caractères maximum avec Ruff (convention choisie).
- **PEP 257** : docstrings utiles pour les interfaces publiques et comportements non évidents.
- **KISS** : choisir la solution la plus simple répondant au problème.
- **YAGNI** : ne pas développer de fonctionnalités, abstractions ou couches sans besoin actuel.
- **DRY avec discernement** : factoriser les duplications de connaissance stables, pas deux lignes similaires sans raison.
- **SOLID proportionné** : responsabilité unique, extension contrôlée, substitutions valides, interfaces petites, dépendances inversées aux frontières quand cela réduit le couplage. Pas de classes ni d'interfaces artificielles.
- **Composition plutôt qu'héritage** quand les deux sont possibles.
- **Python idiomatique** : bibliothèque standard d'abord, `pathlib`, gestion explicite des erreurs, context managers, annotations de type aux frontières.
- **Sécurité** : aucune clé/API secret dans Git, validation des entrées externes, pas de `eval` ni d'exécution shell non justifiée, dépendances minimales.

## Choisir la taille AVANT l'architecture
La taille décrit la **complexité et les besoins**, pas seulement le nombre de fichiers.
Ne pas imposer une architecture grande taille à un petit script.

### XS — Script / prototype
Usage : automatisation ciblée, exercice, expérience rapide.
Structure typique :
```text
project/
├── main.py
├── README.md
└── tests/               # si logique non triviale
```
Règles : fonctions simples ; zéro couche de service/repository ; dépendances seulement si indispensables.

### S — Petit outil / CLI
Usage : outil personnel, intégration légère, petite bibliothèque.
```text
project/
├── pyproject.toml
├── README.md
├── src/nom_du_projet/
│   ├── __init__.py
│   ├── cli.py
│   └── core.py
└── tests/
```
Règles : séparer I/O et logique métier ; modules par responsabilité ; configuration simple.

### M — Application maintenable
Usage : API, application métier, service avec plusieurs fonctionnalités.
```text
project/
├── pyproject.toml
├── README.md
├── src/nom_du_projet/
│   ├── __init__.py
│   ├── domain/           # règles métier indépendantes
│   ├── services/         # cas d'utilisation
│   ├── adapters/         # API, base de données, fichiers
│   └── config.py
└── tests/
    ├── unit/
    └── integration/
```
Règles : frontières explicites seulement si utiles ; injection de dépendances simple ; contrats testés.

### L / XL — Produit complexe, équipe, nombreux domaines
Usage : application multi-domaines, longue durée de vie, plusieurs équipes.
```text
project/
├── pyproject.toml
├── README.md
├── docs/
│   ├── architecture.md
│   └── adr/
├── src/nom_du_projet/
│   ├── modules/
│   │   ├── domaine_a/
│   │   │   ├── domain/
│   │   │   ├── application/
│   │   │   └── infrastructure/
│   │   └── domaine_b/
│   └── shared/           # uniquement le réellement partagé
└── tests/
    ├── unit/
    ├── integration/
    └── e2e/
```
Règles : commencer par un monolithe modulaire ; documenter les décisions structurantes (ADR) ; observabilité, CI et migrations selon besoins. Microservices uniquement avec raisons opérationnelles solides.

## Règles de décision
- Une fonction simple est préférable à une classe sans état.
- Une classe est pertinente si état + invariants, ou comportement polymorphe réel.
- Une abstraction est justifiée par un besoin concret et une variation connue, pas hypothétique.
- Introduire `async` seulement pour des I/O concurrentes réellement nécessaires.
- Préférer une erreur explicite à un `except Exception: pass`.
- Pas de singleton, service locator, « utils.py » fourre-tout, framework ou ORM imposé par défaut.
- Pas de surarchitecture : augmenter la structure seulement lorsqu'une complexité observée le justifie.

## Qualité et outillage (par défaut, si projet outillé)
- Python 3.12+ recommandé pour les nouveaux projets, sauf contrainte de compatibilité documentée.
- `pyproject.toml` pour métadonnées et configuration des outils.
- **Ruff** pour lint + format ; **pytest** pour tests.
- Type checking (`mypy` ou `pyright`) quand la complexité et le contexte le justifient.
- CI légère : lint, format check, tests ; ne pas ajouter de pipeline sophistiqué sans besoin.
- Les dépendances de production doivent être motivées ; verrouiller les versions selon le mode de distribution.
- Conventions : `snake_case` (variables/fonctions/modules), `PascalCase` (classes), `UPPER_SNAKE_CASE` (constantes).
- Test unitaire pour logique métier ; test d'intégration pour DB/API/fichiers ; ne pas viser un pourcentage de couverture sans valeur.
- Noms de tests descriptifs ; pas d'accès réseau dans les tests unitaires.

## Workflow attendu de l'assistant de code
1. Lire l'objectif, les contraintes et le contexte du projet.
2. Déduire ou annoncer la taille XS/S/M/L ; privilégier la plus petite architecture suffisante.
3. Proposer brièvement les fichiers réellement nécessaires.
4. Implémenter en petites étapes sans modifier hors périmètre.
5. Ajouter des tests pertinents, documentation d'exécution et exemples.
6. Vérifier lint, format et tests quand disponibles ; signaler clairement ce qui n'a pas été exécuté.
7. Expliquer les compromis et les décisions d'architecture non évidentes.

## Définition de terminé
- Fonctionnement demandé couvert ; comportement d'erreur géré.
- Architecture proportionnelle à la taille.
- Code PEP 8, clair, testé selon le risque.
- README : installation, exécution, tests et configuration si applicables.
- Aucun secret ni fichier généré inutile commité.

## Contexte spécifique à chaque nouveau projet
Remplir `docs/PROJECT_CONTEXT.md` ou un fichier équivalent dans le sous-projet.
Si une donnée manque, faire une hypothèse explicite et réversible ; ne pas inventer de contraintes.
