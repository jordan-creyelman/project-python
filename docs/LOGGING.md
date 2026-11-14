# Logging et observabilité Python

## Règles
- Utiliser `logging` pour diagnostic ; réserver `print` à la sortie utilisateur d'une CLI ou aux scripts très simples.
- Niveaux : DEBUG (diagnostic), INFO (événement normal important), WARNING (anomalie récupérable), ERROR (échec), CRITICAL (incident grave).
- Configurer les handlers et le niveau **une fois** au point d'entrée de l'application.
- Dans un module de bibliothèque : `logger = logging.getLogger(__name__)` ; ne pas appeler `basicConfig` à l'import.
- Utiliser `logger.info("Résultat %s", value)` pour différer le formatage ; ne pas concaténer les messages par défaut.
- Journaliser des événements exploitables : action, identifiant non sensible, contexte, état, durée si utile.
- Ne pas logger le même incident à plusieurs couches ; privilégier la frontière qui sait le gérer.
- Dans un bloc `except`, `logger.exception("...")` ajoute une trace ; masquer les détails sensibles avant journalisation.
- Ne jamais logguer mots de passe, tokens, cookies d'authentification, payloads personnels ou paramètres sensibles.
- En services : corrélation request_id/trace_id, format JSON et métriques/alertes selon besoins ; ne pas imposer cela aux scripts.
- Gérer les volumes, politiques de rétention et accès aux logs en production.

## Exemple
```python
import logging

logger = logging.getLogger(__name__)


def process_item(item_id: int) -> int:
    if item_id <= 0:
        logger.warning("Identifiant invalide")
        raise ValueError("item_id doit être positif")

    logger.info("Traitement de l'élément %s", item_id)
    return item_id * 2


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    try:
        process_item(1)
    except ValueError:
        logger.exception("Le traitement a échoué")
        raise
```

Dans un CLI, choisir soit le traceback en mode debug, soit un message utilisateur propre en mode normal ; éviter de produire deux fois le même message d'erreur.

## Tests
- Utiliser `caplog` pour les événements utiles.
- Vérifier qu'aucune donnée sensible ne se retrouve dans le log.
- Ne pas tester le texte exact de tous les messages ; tester seulement les événements contractuels.

## Selon la taille
- XS : messages d'erreur simples, logging facultatif.
- S : logging standard avec option verbose/debug.
- M : niveaux cohérents, identifiants d'opérations et diagnostics.
- L/XL : logs structurés, métriques, traces distribuées, rétention et alertes mesurées.
