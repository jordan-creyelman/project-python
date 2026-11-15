# Gestion des dépendances Python

**Principe :** bibliothèque standard d'abord, dépendances justifiées, installation reproductible et vulnérabilités suivies.

| Taille | Convention |
| --- | --- |
| XS | Dépendances minimales et installation simple. |
| S | pyproject.toml pour l'outillage, outils dev séparés, mises à jour selon usage. |
| M | Dépendances suivies, compatibilité Python définie, reproduction des builds. |
| L/XL | Gouvernance des versions, licences, audits et mises à jour de sécurité. |

## Choix et actualité des bibliothèques/frameworks

Appliquer [LIBRARY_SELECTION.md](LIBRARY_SELECTION.md) **avant** d'ajouter
une dépendance majeure : adéquation au besoin, versions Python/OS,
release stable supportée, maintenance et sécurité réelles, licence,
stabilité et coût. Donner la préférence à une bibliothèque avec **une
communauté large et active** lorsque plusieurs choix sont similaires.
Vérifier les faits récents sur la documentation officielle, PyPI et
le dépôt source ; dater la vérification et signaler l'incertitude
si les sources n'ont pas été consultées.

## Règles

1. Déclarer les dépendances de production dans pyproject.toml et les dépendances de développement dans un extra dev ou un groupe dédié ; choisir une seule méthode.
2. Pour une **bibliothèque**, déclarer des plages de compatibilité raisonnables plutôt que figer toutes les dépendances transitives.
3. Pour une **application**, enregistrer le lockfile si l'outil choisi en produit un et si cela sert la reproductibilité.
4. Éviter de mélanger plusieurs gestionnaires de paquets ; documenter une commande d'installation canonique.
5. Vérifier maintenance, licence, provenance et dépendances transitives avant ajout.
6. Tester les mises à jour et lire les notes de rupture ; retirer les dépendances inutilisées.
7. Dependabot peut ouvrir des PR de mise à jour, mais **ne remplace pas la revue ni les tests**.

Le modèle templates/github/dependabot.yml doit être copié en .github/dependabot.yml du projet concerné, puis ajusté. La section github-actions n'est utile que si le dépôt contient des workflows GitHub Actions.

Les audits de dépendances et la déclaration de vulnérabilités suivent SECURITY.md et SECURITY_POLICY.md. Aucun bot n'est activé dans les autres dépôts par cette documentation.
