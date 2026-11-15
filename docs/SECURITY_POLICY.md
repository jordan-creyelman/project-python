# Security Policy — divulgation et correction

Ce guide complète SECURITY.md : le premier décrit la **réponse aux vulnérabilités**, le second les règles de **programmation sécurisée**.

| Taille | Politique |
| --- | --- |
| XS | En cas de faille, contact privé du mainteneur si possible ; ne pas divulguer un exploit sensible. |
| S | Un canal de signalement privé et les versions supportées si le projet est distribué. |
| M | Un fichier SECURITY.md, triage, correctifs et avis de sécurité selon impact. |
| L/XL | Escalade, responsables, publication coordonnée et suivi des correctifs. |

## Processus recommandé

1. **Recevoir confidentiellement** via GitHub Private Vulnerability Reporting si activé, ou un canal privé réel et maintenu. Ne jamais inventer d'adresse email.
2. Demander version affectée, impact, étapes minimales et éléments de preuve ne contenant pas de secrets.
3. Qualifier l'impact, la sévérité et les versions affectées ; ne promettre aucun délai sans validation.
4. Corriger avec tests de régression, en limitant la diffusion des détails si la faille n'est pas encore publique.
5. Publier le correctif et, si pertinent, un avis de sécurité coordonné avec les personnes concernées.
6. Mettre à jour la documentation et les pratiques pour éviter une répétition.

## Modèle à personnaliser

Copier templates/SECURITY.md dans SECURITY.md ou .github/SECURITY.md du projet distribué. **Avant publication**, remplacer le canal privé et les versions prises en charge par des informations vérifiées. Un placeholder n'est pas un moyen de signalement fonctionnel.

Éviter toute issue publique pour une vulnérabilité exploitable non corrigée.
