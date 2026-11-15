# Choisir les bibliothèques et frameworks Python

> Objectif : préférer une solution **adaptée, actuelle, stable, maintenue et
> soutenue par une communauté active et suffisamment importante**, sans
> remplacer la qualité technique par un concours de popularité.

## 1. Décider si une dépendance est nécessaire

1. Vérifier si la **bibliothèque standard Python** couvre le besoin simplement.
2. Identifier l'usage réel : CLI, API, calcul scientifique, interface, matériel,
   automatisation, persistance, contraintes de sécurité et d'exploitation.
3. Définir les contraintes : versions de Python, OS, licences, budget de
   maintenance, performances, compatibilité avec les dépendances existantes.
4. Privilégier une version **stable et prise en charge** ; éviter alpha/beta,
   logiciel abandonné et migration imposée vers une nouveauté sans bénéfice.
5. Ne pas ajouter de framework complet quand une petite bibliothèque suffit.

## 2. Grille d'évaluation

Pour un choix non trivial, comparer **deux ou trois options plausibles**,
y compris la bibliothèque standard si elle constitue une alternative réelle.

| Critère | Ce qu'il faut vérifier |
| --- | --- |
| Adéquation | Résout le besoin avec le moins de complexité et de code annexe. |
| Actualité | Releases récentes **selon le rythme du projet**, correctifs, compatibilité Python/OS et cycle de support. |
| Maintenance | Activité des mainteneurs, traitement des bugs, notes de version, capacité de réponse aux vulnérabilités. |
| Communauté | Écosystème actif, documentation, tutoriels récents, contributeurs, adoption et entraide. **Favoriser une communauté large et vivante** lorsque les choix sont comparables. |
| Stabilité | API mûre, politique de dépréciation, mises à jour compatibles et migrations raisonnables. |
| Sécurité | Avis de sécurité, failles non corrigées, chaîne de dépendances et provenance des packages. |
| Coût | Taille/complexité, dépendances transitives, installation, licence, performance, maintenance et courbe d'apprentissage. |

**Important :** étoiles GitHub, téléchargements PyPI et date de dernière
release sont des **indices**, jamais une preuve suffisante. Un projet mature
peut sortir peu de versions sans être abandonné ; un projet très populaire
peut ne pas convenir au besoin. Un outil spécialisé à communauté plus petite
reste acceptable si sa valeur et sa maintenance sont clairement justifiées.

## 3. Vérifier les faits à la date du choix

- Consulter en priorité le site et la documentation **officiels**, la page
  **PyPI**, le dépôt officiel GitHub/GitLab et ses releases/changelog.
- Examiner les versions Python prises en charge, l'état du support,
  la dernière version stable, l'activité de maintenance et les alertes.
- Vérifier la licence et les éventuelles contraintes de matériel ou système.
- Si une recherche externe est possible et que la fraîcheur compte,
  **vérifier les données à jour**, citer ou lier les sources et indiquer la
  **date de vérification**.
- Si les sources ne sont pas accessibles, **déclarer l'incertitude** :
  ne pas affirmer qu'une version est « la dernière » ou qu'un projet est
  « activement maintenu » sans vérification.
- Respecter d'abord les bibliothèques et frameworks existants du projet ;
  proposer une migration uniquement avec bénéfice concret et coûts évalués.

## 4. Décision du Tech Lead selon la taille

| Taille | Méthode attendue |
| --- | --- |
| **XS** | Standard library d'abord ; une dépendance seulement si elle simplifie réellement. Aucune étude formelle. |
| **S** | Choisir 1 outil principal par besoin ; vérifier maintenance et documentation, comparer brièvement si choix structurant. |
| **M** | Comparatif court et argumenté des options importantes : adéquation, compatibilité, sécurité, communauté et coût. |
| **L/XL** | Comparatif documenté, analyse du support, de la migration, de la sécurité, des coûts ; ADR pour les choix difficiles à inverser. |

## 5. Comment présenter la recommandation

Le Tech Lead doit préciser, quand le choix compte :
- **Choix recommandé et pourquoi** (adéquation et simplicité d'abord).
- **Alternative(s)**, avec avantage et compromis principaux.
- **Maintenance/communauté** : signaux vérifiés, limites éventuelles.
- **Compatibilité/sécurité** : contraintes de Python, OS, licence, risques.
- **Sources et date** si des faits d'actualité ont été vérifiés.

Exemple : pour une petite CLI, comparer `argparse` (standard library)
avec les outils CLI tiers pertinents, au lieu d'installer d'office un
framework complet. Le résultat dépend des fonctionnalités réellement requises.

Les règles d'installation et de versioning restent dans
[DEPENDENCIES.md](DEPENDENCIES.md). Les décisions durables peuvent être
documentées dans [ADR.md](ADR.md).
