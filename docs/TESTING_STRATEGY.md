# Stratégie de tests Python

## Principe directeur
Tester les comportements et risques réels, pas les détails d'implémentation.
Préférer quelques tests pertinents et fiables à une pyramide artificielle de tests lents.
`pytest` est le choix par défaut pour les nouveaux projets ; `unittest` standard reste valable si aucune dépendance n'est souhaitée.

## Types de tests et quand les utiliser
| Type | Cible | Quand |
| --- | --- | --- |
| **Unitaires** | Fonction / classe isolée, règles métier, valeurs limites | Dès que la logique n'est pas triviale |
| **Intégration** | Base de données, système de fichiers, HTTP client, composants réels | Dès qu'une frontière I/O peut échouer |
| **Contrat** | Format d'API/événement entre producteurs et consommateurs | Si des services ou clients évoluent indépendamment |
| **End-to-end (E2E)** | Parcours complet de l'utilisateur | Quelques parcours critiques sur une vraie application |
| **Régression** | Bug corrigé qui ne doit pas revenir | À chaque correction de bug significative |
| **Paramétrés** | Beaucoup de cas d'entrée et de limites | Pour réduire la duplication des tests |
| **Property-based** | Invariants sur de nombreuses valeurs générées | Algorithmes, parseurs, calculs complexes ; `hypothesis` si justifié |
| **Performance / charge** | Latence, débit, mémoire, comportement sous charge | Seulement si exigences mesurables |
| **Sécurité** | Validation, permissions, authentification, dépendances | Selon exposition et risque |
| **Smoke** | Vérification rapide que l'app démarre | Application packagée ou déployée |
| **Compatibilité** | Versions Python, OS, formats de données | Lorsqu'un support multi-environnement est promis |

Les tests de mutation peuvent servir sur code critique, sans en faire une obligation.
Les tests manuels/exploratoires complètent l'automatisation pour les interfaces complexes.

## Règles des tests
- Nommer `test_<comportement>_<situation>`; organiser les tests par fonctionnalité.
- Un test = une intention claire ; étapes Arrange / Act / Assert lisibles.
- Vérifier succès, erreur, cas limite et comportement observable.
- Déterministes, indépendants, répétables ; pas de `sleep` ni dépendance à l'ordre des tests.
- Pas de réseau réel dans les unitaires ; utiliser fakes/mocks aux frontières **seulement si nécessaire**.
- Utiliser `tmp_path` pour fichiers temporaires, `monkeypatch` pour variables d'environnement, `pytest.raises` pour erreurs.
- Préférer une base de test isolée pour l'intégration ; ne jamais pointer une base de production.
- Exécuter E2E et performance séparément si cela ralentit trop la boucle de développement.
- Corriger les tests instables au lieu de multiplier les retries.
- Une couverture élevée n'implique pas une bonne qualité : prioriser chemins critiques et branches d'échec.
- Ne pas transformer une fonction privée en API publique juste pour la tester.

## Exemple unitaire simple
```python
import pytest


def discount(price: float, rate: float) -> float:
    if price < 0 or not 0 <= rate <= 1:
        raise ValueError("Paramètres invalides")
    return price * (1 - rate)


@pytest.mark.parametrize(
    ("price", "rate", "expected"),
    [(100, 0.2, 80), (100, 0, 100), (0, 0.5, 0)],
)
def test_discount_valid_cases(price, rate, expected):
    assert discount(price, rate) == pytest.approx(expected)


@pytest.mark.parametrize(("price", "rate"), [(-1, 0.2), (100, -0.1), (100, 1.1)])
def test_discount_rejects_invalid_input(price, rate):
    with pytest.raises(ValueError, match="Paramètres invalides"):
        discount(price, rate)
```
Exemple pédagogique autonome ; dans une application, importer `discount` depuis son module plutôt que la redéfinir dans le test.

## Exemple d'intégration de fichier
```python
from pathlib import Path


def save_message(path: Path, message: str) -> None:
    path.write_text(message, encoding="utf-8")


def test_save_message_writes_utf8(tmp_path):
    output = tmp_path / "message.txt"
    save_message(output, "équipe")
    assert output.read_text(encoding="utf-8") == "équipe"
```

## Organisation suggérée
```text
tests/
├── unit/
│   └── test_rules.py
├── integration/
│   └── test_storage.py
├── e2e/                 # seulement si justifié
│   └── test_main_flow.py
└── conftest.py          # fixtures partagées seulement si nécessaires
```
En XS/S, un simple `tests/test_core.py` suffit.

## Commandes usuelles (si outils installés)
```bash
python -m pytest
python -m pytest -q
python -m pytest tests/unit
python -m pytest --maxfail=1
ruff check .
ruff format --check .
```
Pour une mesure de couverture **facultative**, installer `pytest-cov` puis lancer `python -m pytest --cov=nom_du_projet --cov-report=term-missing`. Ne pas définir de seuil universel par défaut.

## Matrice de stratégie par taille
| Taille | Tests attendus |
| --- | --- |
| XS | Vérification manuelle documentée ; unitaires pour logique non triviale |
| S | Unitaires + tests d'erreurs + intégration I/O si présente |
| M | Unitaires + intégration + quelques parcours E2E critiques si pertinents |
| L/XL | Tous les types pertinents selon risques : contrat, E2E ciblés, sécurité, performance, compatibilité, CI multi-environnement |

## Pipeline CI minimal à adapter
1. Installer les dépendances de test du projet.
2. Vérifier `ruff check .` et `ruff format --check .`.
3. Lancer `python -m pytest`.
4. Ajouter typage, matrices Python, couverture et audits uniquement selon besoin.

Ne pas activer une CI non fonctionnelle dans ce dépôt de documentation : créer les workflows lorsqu'un projet exécutable est ajouté.

## Critères d'acceptation
- Les scénarios utilisateurs importants passent.
- Chaque bug corrigé possède, si possible, un test de régression.
- Les erreurs et limites importantes sont testées.
- Pas de tests dépendants du réseau ou du temps non contrôlés.
- Les tests sont exécutés ou leur non-exécution est signalée explicitement.

## Automatisation et critères de livraison

Adapter les vérifications aux risques selon [CI_CD_STRATEGY.md](CI_CD_STRATEGY.md)
et [DEFINITION_OF_DONE.md](DEFINITION_OF_DONE.md).
