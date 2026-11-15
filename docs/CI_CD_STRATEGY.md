# Convention CI/CD Python

La **CI** valide un changement ; la **CD** distribue ou déploie un livrable. Aucun déploiement automatique ne doit être ajouté implicitement.

## Niveau adapté

| Taille | Intégration continue | Livraison |
| --- | --- | --- |
| XS | Facultative ; tests manuels ou ciblés. | Publication manuelle si nécessaire. |
| S | Ruff et pytest si configurés, sur push/PR. | Tag ou release manuels. |
| M | CI requise avant fusion : lint, format, tests, build/smoke si pertinent. | Release validée depuis main. |
| L/XL | CI requise avec intégration/contrats, sécurité, matrices ciblées selon risques. | Approbations, environnements et rollback adaptés. |

La criticité prime sur la taille : un script exposé à Internet peut exiger davantage de contrôles.

## Utiliser le modèle

Le fichier templates/github/workflows/python-ci.yml est un **modèle inactif** ici. Pour un vrai projet Python, le copier vers .github/workflows/python-ci.yml, puis :

1. Adapter les branches main/dev et la version de Python.
2. Pour un nouveau projet uv, vérifier `pyproject.toml`, un groupe de
   développement `dev` (par exemple `uv add --dev pytest ruff`) et
   un `uv.lock` **commité** et cohérent. Si le projet existant utilise
   un extra `dev`, adapter le modèle (`uv sync --extra dev --locked`)
   au lieu de changer arbitrairement ses dépendances.
3. Le modèle emploie `astral-sh/setup-uv`, `uv sync --locked` et
   `uv run --locked`. Vérifier que Ruff/pytest sont déclarés et que
   les tests ciblent le code réel. Sans `uv.lock`, ne pas utiliser
   l'option `--locked` avant d'avoir généré et commité le fichier.
4. Faire tourner le workflow sur une PR avant d'exiger son statut en protection de branche.
5. Limiter les permissions du token et éviter les secrets sur du code de PR non fiable.
6. Épingler les actions à des commits SHA complets si la politique de sécurité l'exige.

## Critères

- Une CI rédigée mais non activée n'est pas une CI exécutée.
- Ne pas exiger des statuts qui n'existent pas.
- Publier seulement depuis une référence stable validée ; les tags et releases suivent VERSIONING.md.
- Pas de déploiement automatique depuis ce dépôt d'instructions.

**project-python n'est pas un projet exécutable : aucun workflow actif n'est placé dans .github/workflows ici.**
