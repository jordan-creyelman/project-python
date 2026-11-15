# Convention de docstrings Python — anglais obligatoire

> **Toutes les docstrings Python nouvellement rédigées ou modifiées doivent
> être en anglais**, même si les échanges, le README ou les messages affichés
> à l'utilisateur sont en français. Suivre PEP 257 et la terminologie du
> projet ; conserver des formulations exactes et concises.

## Portée

- **Documenter les modules, fonctions, classes et méthodes publics**
  lorsque leur rôle ou leur contrat mérite une explication.
- Pour les fonctions privées, ajouter une docstring seulement si le
  comportement, les invariants ou les effets de bord ne sont pas évidents.
- Une docstring existante dans une portion de code **modifiée** doit être
  mise en anglais et corrigée si le contrat change ; ne pas traduire tout
  un dépôt ancien hors du périmètre demandé.
- Ne pas ajouter de docstrings artificielles aux tests ou aux accesseurs
  triviaux sans information nouvelle.
- Les annotations de types documentent les types ; les docstrings expliquent
  **le sens**, les unités, les contraintes, les erreurs et les effets de bord.

## Style

1. Utiliser des triples guillemets doubles et une **phrase de synthèse à
   l'impératif** : `"""Return the resistance in ohms."""`.
2. Respecter PEP 257 : synthèse seule si elle suffit ; pour une docstring
   multiligne, laisser une ligne vide après la synthèse.
3. Garder le texte lisible, sans paraphraser la signature ou décrire chaque
   ligne de code.
4. Employer le style **Google** (sections `Args:`, `Returns:`,
   `Raises:`, `Examples:`) quand la fonction a besoin de détails ;
   ne pas imposer ces sections aux fonctions simples.
5. Documenter particulièrement : unités physiques, plages valides,
   exceptions pertinentes, comportement de retour, I/O et effets de bord.
6. Être cohérent avec les conventions existantes du projet et avec
   [MODULAR_DESIGN.md](MODULAR_DESIGN.md). Pour une API établie en style
   NumPy ou Sphinx, **préserver son style** ; l'anglais reste obligatoire.

## Exemples

### Une ligne (suffisante pour un contrat clair)

    def ohms_to_kilohms(value: float) -> float:
        """Convert a resistance from ohms to kilohms."""
        return value / 1000

### Plusieurs lignes (unités, erreurs et conditions)

    def led_resistance(supply_v: float, forward_v: float, current_ma: float) -> float:
        """Calculate the series resistance required for an LED.

        Assume a single LED and a constant DC supply.

        Args:
            supply_v: Supply voltage in volts.
            forward_v: LED forward voltage in volts.
            current_ma: Target LED current in milliamperes.

        Returns:
            Required resistance in ohms.

        Raises:
            ValueError: If the current is not positive or the voltage
                drop across the resistor is not positive.
        """
        if current_ma <= 0 or supply_v <= forward_v:
            raise ValueError("Invalid LED electrical parameters")
        return (supply_v - forward_v) / (current_ma / 1000)

## Vérification

- Relire les docstrings des API publiques **touchées par la PR**.
- Vérifier qu'elles sont en anglais et correspondent au code testé.
- Ne pas promettre qu'un linter valide la langue : Ruff/PEP 257 peuvent
  aider sur le format, mais **l'exactitude et l'anglais requièrent une
  relecture**.
- Ne pas reformatter les messages destinés aux utilisateurs ni imposer
  l'anglais au reste de la documentation à cause de cette convention.
