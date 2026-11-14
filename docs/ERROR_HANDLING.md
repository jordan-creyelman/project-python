# Gestion des erreurs Python

## Objectif
Faire échouer le programme clairement et de façon prévisible, sans cacher les bugs.
Appliquer ces règles proportionnellement à la taille du projet (voir `AGENTS.md`).

## Règles
1. **Prévenir à la frontière** : valider entrées CLI, requêtes HTTP, variables d'environnement, fichiers et données externes.
2. **Lever une exception précise** : `ValueError`, `TypeError`, `FileNotFoundError`, `TimeoutError`, ou exception métier dédiée si le domaine le justifie.
3. **Intercepter au bon niveau** : capturer une erreur uniquement quand on peut la traiter, la transformer avec du contexte ou la présenter à l'utilisateur.
4. **Ne jamais masquer** : interdire `except: pass` et `except Exception: pass`. Éviter `except Exception` sauf à la frontière de l'application (journalisation + sortie maîtrisée).
5. **Conserver la cause** : `raise ErreurMetier("contexte") from exc` lorsque l'on traduit une erreur technique.
6. **Séparer métier et interface** : la logique métier lève ; CLI/API traduit en message et code retour/statut approprié.
7. **Ne pas divulguer** : jamais de secrets, tokens, mots de passe ou données personnelles dans les messages d'erreur/logs.
8. **Récupération limitée** : retry seulement pour erreurs transitoires connues, avec timeout, nombre maximum de tentatives et backoff ; jamais pour validation ou erreurs de programmation.
9. **Nettoyage garanti** : `with` pour fichiers/transactions/verrous ; rollback et état cohérent en cas d'échec.
10. **Pas de résultat ambigu** : ne pas renvoyer `None` à la place d'un échec sauf si `None` est une valeur métier attendue et documentée.

## Exemple : exception métier et chaînage
```python
from pathlib import Path


class ConfigurationError(Exception):
    """Configuration invalide ou inaccessible."""


def read_config(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise ConfigurationError(f"Configuration introuvable : {path.name}") from exc
    except PermissionError as exc:
        raise ConfigurationError("Accès à la configuration refusé") from exc
```

Capturer `ConfigurationError` à la frontière (CLI / API), sans afficher une trace interne à l'utilisateur normal. En développement, garder le traceback accessible de façon contrôlée.

## Exemples de validation
```python
def percentage(value: float) -> float:
    if not 0 <= value <= 100:
        raise ValueError("Le pourcentage doit être entre 0 et 100")
    return value
```

## Journalisation et observabilité
- Utiliser `logging`, pas `print`, pour diagnostiquer les erreurs d'une application (un script XS peut rester simple).
- Utiliser `logger.exception(...)` dans un `except` lorsqu'un traceback est nécessaire ; ne pas logger la même exception à tous les étages.
- Pour les services : identifiant de corrélation, contexte non sensible, métriques d'erreur et alertes selon criticité.
- API : erreurs client 4xx distinctes des erreurs serveur 5xx ; réponse générique côté client pour les détails internes.
- CLI : message clair sur stderr et code de sortie non nul en cas d'échec.

## Tester les erreurs
- Entrée absente, invalide, limite, vide, mauvais format.
- Fichier manquant, droits insuffisants, timeout, indisponibilité externe.
- Préservation de l'état et absence d'effets secondaires lors d'un échec.
- Messages compréhensibles et non sensibles.
- Retry borné seulement si prévu dans le besoin.

## Selon la taille
| Taille | Gestion minimale suffisante |
| --- | --- |
| XS | Validation + exceptions standard + messages lisibles |
| S | Exceptions ciblées + frontière CLI + quelques tests d'erreur |
| M | Exceptions métier où pertinentes + logs structurés si utiles + tests de défaillance |
| L/XL | Contrats d'erreur, traçabilité, observabilité, résilience et alerting basés sur risques |

Ne pas créer un catalogue d'exceptions, un bus d'événements ou un framework de retry sans besoin réel.
