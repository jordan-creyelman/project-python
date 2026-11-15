# Definition of Done — critères de livraison

Une tâche est terminée lorsque les comportements attendus ont été livrés **et vérifiés**, pas lorsque le code a simplement été écrit.

## Socle commun

- [ ] Le besoin utilisateur et les critères d'acceptation sont satisfaits.
- [ ] Les principales erreurs, limites et régressions sont traitées.
- [ ] Le diff est cohérent, lisible et sans secret ni artefact inutile.
- [ ] Les dépendances nouvellement choisies sont adaptées, maintenues et compatibles ; toute incertitude sur leur actualité est déclarée.
- [ ] Les docstrings Python ajoutées ou modifiées sont en anglais, exactes et conformes à PEP 257.
- [ ] La documentation est à jour si l'usage ou l'interface a changé.
- [ ] Les tests et vérifications **réellement exécutés** sont rapportés.
- [ ] Les limites non vérifiées et risques restants sont déclarés.

## Preuves selon la taille

| Taille | Attendus supplémentaires |
| --- | --- |
| XS | Essai manuel documenté ou tests ciblés pour logique non triviale. |
| S | Tests pertinents, Ruff/pytest si configurés, README et aide CLI corrects. |
| M | CI avant fusion, intégration testée aux frontières, PR et revue selon équipe. |
| L/XL | Contrats, migrations, sécurité et performance selon risque, revue et rollback si nécessaires. |

## Règles de transparence

- Test non exécuté = **non vérifié**, jamais réussi par supposition.
- Workflow créé =/= workflow exécuté ; workflow exécuté =/= workflow réussi.
- PR créée =/= PR fusionnée ; documentation =/= protection GitHub activée.
- Une tâche documentaire exige des liens et contenus cohérents ; dans
  `project-python`, le workflow de validation vérifie aussi les
  exemples exécutables XS/S/M avec uv.
- Les exigences de sécurité peuvent être fortes même dans un projet XS.

À rapprocher de TESTING_STRATEGY.md, CI_CD_STRATEGY.md et PULL_REQUESTS.md.
