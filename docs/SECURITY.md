# Sécurité Python — règles proportionnées au risque

## Principes
- Traiter toutes les entrées externes (CLI, API, fichiers, environnement, DB) comme non fiables.
- Principe du moindre privilège ; limiter les accès disque, réseau et comptes techniques.
- Ne jamais commiter de secrets ; utiliser variables d'environnement ou gestionnaire de secrets.
- Ne jamais afficher tokens, mots de passe, données personnelles ou secrets dans erreurs, logs et traces.
- Mettre à jour les dépendances et vérifier leur provenance ; limiter le nombre de paquets.
- Éviter `eval`, `exec`, la désérialisation `pickle` de données non fiables et `shell=True` avec entrées externes.
- Utiliser requêtes SQL paramétrées, pas l'interpolation de chaînes.
- Pour les appels HTTP : HTTPS, timeouts explicites, contrôle des redirections/URL, vérification TLS active.
- Pour les fichiers : valider noms et chemins fournis par l'utilisateur ; attention au path traversal, aux liens symboliques et permissions.
- N'utiliser ni cryptographie maison ni comparaison naïve de secrets ; préférer des bibliothèques éprouvées et `hmac.compare_digest` pour des comparaisons sensibles appropriées.
- Définir authentification, autorisation et limites de débit si exposition réseau ; ne pas confondre connexion et permission.
- Configurer les erreurs pour ne pas divulguer l'implémentation interne ; voir `ERROR_HANDLING.md`.

## Checklist avant merge
- [ ] Aucun secret dans le code, les tests, les fixtures ou les commits.
- [ ] Entrées externes validées et sorties sensibles protégées.
- [ ] SQL/shell/fichiers/HTTP traités avec primitives sûres.
- [ ] Dépendances nécessaires et maintenues.
- [ ] Permissions minimales.
- [ ] Scénarios d'abus pertinents couverts par des tests.

## Exemple : SQL paramétré
```python
def get_user(connection, user_id: int):
    return connection.execute(
        "SELECT id, name FROM users WHERE id = ?", (user_id,)
    ).fetchone()
```
Le placeholder varie selon le driver.

## Exemple : appel externe avec timeout
```python
from urllib.request import urlopen

def fetch_text(url: str) -> str:
    # Appeler seulement après validation de la provenance / destination de l'URL.
    with urlopen(url, timeout=5) as response:
        return response.read(1024 * 1024).decode("utf-8")
```
Pour une URL contrôlée par un utilisateur, ajouter une défense SSRF adaptée (destinations autorisées, contrôles réseau, redirections, résolution DNS et taille maximale).

## Selon la taille
- XS : validation, pas de secrets hardcodés, pas d'exécution dangereuse.
- S : vérifier dépendances et permissions, tests des entrées malformées.
- M : revues d'accès, audit de dépendances, gestion de secrets et sécurité des API si présentes.
- L/XL : modélisation de menaces, automatisation des contrôles et surveillance selon exposition.

Ne pas installer un scanner, une politique complexe ou des couches de sécurité décoratives sans risque identifiable.

## Signalement et divulgation de vulnérabilités

La procédure de signalement confidentiel, de triage et de correction
est définie dans [SECURITY_POLICY.md](SECURITY_POLICY.md).
