# Configuration Python — fiable et simple

## Principes
- Séparer configuration, code et secrets.
- Préférer les paramètres explicites ; utiliser les variables d'environnement pour les valeurs dépendant du déploiement.
- Centraliser la lecture et la validation à la frontière de l'application, pas dans chaque module.
- Valider au démarrage les valeurs obligatoires ; échouer avec un message clair, sans révéler de secret.
- Les valeurs par défaut doivent être sûres ; la configuration de production doit être explicite.
- Garder un `.env.example` documenté avec valeurs factices seulement ; ignorer `.env` et les autres fichiers secrets dans Git.
- Un fichier `.env` est une commodité locale, **pas** un coffre-fort ; le chargement automatique est optionnel et ne doit pas être présumé.
- Ne pas lire l'environnement dans des fonctions métier pures ; passer un objet de configuration ou les paramètres nécessaires.
- Éviter les frameworks et hiérarchies de configuration si `os.environ` + `dataclass` suffisent.

## Exemple standard library
```python
import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    endpoint: str
    timeout_seconds: int = 5


def load_settings() -> Settings:
    endpoint = os.environ.get("APP_ENDPOINT", "").strip()
    if not endpoint:
        raise ValueError("APP_ENDPOINT est obligatoire")

    raw_timeout = os.environ.get("APP_TIMEOUT_SECONDS", "5")
    try:
        timeout = int(raw_timeout)
    except ValueError as exc:
        raise ValueError("APP_TIMEOUT_SECONDS doit être un entier") from exc

    if timeout <= 0:
        raise ValueError("APP_TIMEOUT_SECONDS doit être positif")
    return Settings(endpoint=endpoint, timeout_seconds=timeout)
```

## Exemple de fichier local non sensible
```dotenv
# .env.example — documentation, pas de secrets réels
APP_ENDPOINT=https://example.org
APP_TIMEOUT_SECONDS=5
```

## Tests
- Variable requise absente.
- Valeur de type incorrect, valeur hors limites.
- Valeur par défaut correcte.
- Aucun secret dans les messages d'erreur.
- Utiliser `monkeypatch` pour contrôler l'environnement dans pytest.

## Selon la taille
- XS : constantes explicites ou arguments CLI.
- S : configuration d'entrée unique ; variables d'environnement si utiles.
- M : `Settings` immuable et validation au démarrage, séparation dev/test/prod.
- L/XL : gestionnaire de secrets, schémas versionnés et contrôles de déploiement si nécessaires.
