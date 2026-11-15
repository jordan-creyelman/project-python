# Versionner et publier les standards project-python

Ce processus concerne uniquement les **conventions de project-python**, pas
les versions des applications créées avec ses modèles.

## Préparer une version

1. Dans une branche `docs/*` ou `chore/*`, mettre à jour `VERSION`,
   la section datée correspondante de `CHANGELOG.md`, le lien du README
   et la version intégrée au générateur si les standards changent.
2. Créer une PR avec un titre en anglais et vérifier le diff.
3. Attendre le succès de
   [docs-check.yml](../.github/workflows/docs-check.yml) sur la PR.
4. Fusionner dans `main` et attendre **une CI réussie sur le commit main**.
5. Vérifier :

```bash
python scripts/check_release.py --version 0.3.0
```

## Publier uniquement sur demande

Le workflow [release.yml](../.github/workflows/release.yml) fonctionne
uniquement avec une action **manuelle** depuis GitHub Actions :

1. Ouvrir GitHub → Actions → **Publish standards release**.
2. Choisir **Run workflow**, branche `main`, saisir la version sans `v`.
3. Le workflow vérifie la concordance avec `VERSION`, les notes du changelog,
   le succès d'une CI du commit et l'absence de tag Git existant.
4. Si tous les contrôles passent, il crée **le tag `vX.Y.Z` et une GitHub
   Release** à partir du commit de `main`, avec les notes validées.

Un commit ou une PR ne publie **rien automatiquement**. Aucune publication
PyPI n'est incluse. Pour un projet issu des templates, choisir sa propre
stratégie de versions selon [VERSIONING.md](VERSIONING.md).

## Sécurité et retour arrière

- Les tags déjà publiés ne doivent pas être déplacés ou écrasés.
- Si un contrôle échoue, corriger la branche et faire repasser la CI.
- Une correction ultérieure doit faire l'objet d'une nouvelle version.
- Aucune release n'est créée tant que l'utilisateur ne lance pas le workflow.
