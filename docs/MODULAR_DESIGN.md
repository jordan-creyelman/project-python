# Fonctions et modules Python — principes de conception

## Objectif
Créer des fonctions cohérentes, faciles à lire, réutiliser et tester ; répartir le code en modules uniquement quand cela clarifie réellement le projet. Suivre `AGENTS.md`, KISS, SOLID et YAGNI.

## Fonctions
- **Une responsabilité identifiable** : une fonction réalise une opération cohérente ; la découper lorsque des étapes distinctes portent des noms métiers utiles, pas pour atteindre une limite arbitraire de lignes.
- **Noms descriptifs** : utiliser `snake_case`, préférer `load_settings` à `process_data` si le rôle est plus précis.
- **Entrées/sorties explicites** : paramètres ciblés, résultat prévisible, annotations de types aux frontières publiques, valeurs par défaut immuables.
- **Effets de bord maîtrisés** : isoler lecture/écriture, réseau, logging et mutations des calculs déterministes quand cela améliore la testabilité.
- **Éviter les booléens de mode** si une fonction effectue deux comportements différents ; préférer deux noms explicites si justifié.
- **Complexité** : utiliser des retours anticipés (guard clauses), éviter les imbrications profondes et les arguments trop nombreux ; regrouper les paramètres conceptuellement liés avec une dataclass uniquement si utile.
- **Exceptions** : documenter les erreurs attendues ; ne pas retourner `None` silencieusement après un échec. Voir `docs/ERROR_HANDLING.md`.
- **Documentation** : toutes les docstrings Python nouvelles/modifiées sont **en anglais** ; suivre PEP 257 et [DOCSTRINGS.md](DOCSTRINGS.md) pour les API publiques et comportements non évidents. Éviter les commentaires répétant le code.
- **Pas de règles rigides** sur le nombre de lignes ou de paramètres ; faire un refactoring dès que compréhension, test ou évolution deviennent difficiles.

## Modularité
- Regrouper les fonctions par **responsabilité métier ou fonctionnalité**, pas uniquement par type technique.
- Une fonction privée reste dans son module jusqu'à l'existence d'un besoin de réutilisation réel ; éviter les `helpers.py` et `utils.py` fourre-tout.
- Garder les dépendances orientées : interface/CLI/API → orchestration → logique métier ; mettre la persistance ou les services externes derrière des fonctions/adapters quand la complexité le justifie.
- Éviter les imports circulaires, les imports `*` et les effets de bord pendant l'import des modules.
- Exposer une API publique réduite, stable et documentée ; préfixer les détails internes par `_` lorsque pertinent.
- Préférer des fonctions et la composition. Introduire des classes pour état + invariants, ressources ou vrai polymorphisme, pas seulement pour ranger des fonctions.
- Injection de dépendances **simple** : passer une fonction/objet client en paramètre quand cela aide les tests ; pas de conteneur DI sans raison.
- Éviter les variables globales mutables et l'état caché.
- Bibliothèque standard d'abord ; aucune dépendance architecturale imposée.

## Exemple : séparer calcul et I/O

```python
from pathlib import Path


def total_prices(prices: list[float]) -> float:
    """Calculate the total price without performing I/O."""
    if any(price < 0 for price in prices):
        raise ValueError("Un prix ne peut pas être négatif")
    return sum(prices)


def load_prices(path: Path) -> list[float]:
    """Read one price per line from a text file."""
    return [
        float(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def total_from_file(path: Path) -> float:
    """Read prices from a file and calculate their total."""
    return total_prices(load_prices(path))
```

Pour une application plus grosse, séparer `load_prices`, `total_prices` et `total_from_file` dans des modules **uniquement** si leurs responsabilités, tests ou évolutions le justifient.

## Exemple de tests unitaires
```python
import pytest

from mon_projet.pricing import total_prices


def test_total_prices_adds_values():
    assert total_prices([10, 5]) == 15


def test_total_prices_rejects_negative_value():
    with pytest.raises(ValueError, match="négatif"):
        total_prices([10, -1])
```
Un test d'intégration avec `tmp_path` vérifiera séparément la lecture du fichier et l'orchestration.

## Structure progressive
### XS : ne pas découper artificiellement
```text
main.py
```
### S : séparer les responsabilités si elles apparaissent
```text
src/mon_projet/
├── __init__.py
├── cli.py
└── pricing.py
```
### M : différencier domaine et frontières si utile
```text
src/mon_projet/
├── domain/
│   └── pricing.py
├── services/
│   └── checkout.py
└── adapters/
    └── storage.py
```
### L/XL : préférer la modularité par domaine
```text
src/mon_projet/modules/
├── catalogue/
├── commandes/
└── facturation/
```
N'ajouter ni dossier ni couche sans responsabilité réelle.

## Checklist de revue
- [ ] Chaque fonction a un rôle compréhensible et un nom précis.
- [ ] Paramètres et résultats sont explicites ; aucun état caché inutile.
- [ ] I/O et logique métier sont séparées lorsque utile.
- [ ] Pas de duplication de logique métier stable.
- [ ] Pas de module « fourre-tout » ni import circulaire.
- [ ] Pas d'abstraction spéculative (YAGNI).
- [ ] Tests de comportement, erreurs et limites ajoutés selon le risque.
- [ ] Architecture et taille du projet restent proportionnées.
