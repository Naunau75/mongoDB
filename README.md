# OpenFoodFacts Explorer (Mongo Project)

Un projet Python simple pour explorer l'API [Open Food Facts](https://world.openfoodfacts.org/) et récupérer des informations nutritionnelles détaillées sur les produits alimentaires.

## 📋 Fonctionnalités

- **Récupération de produit** : Obtient les détails d'un produit spécifique via son code-barres (ex: Nutella).
- **Analyse détaillée** : Affiche la composition (ingrédients) et les données nutritionnelles.
- **Recherche textuelle** : Permet de rechercher des produits par mots-clés (ex: "mineral water").

## 🛠 Prérequis

- **Python** (géré automatiquement via `uv`)
- **uv** (Gestionnaire de paquets Python performant)

## 🚀 Installation

Ce projet utilise [uv](https://github.com/astral-sh/uv) pour la gestion des dépendances.

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/Naunau75/mongoDB.git
   cd mongoDB
   ```

2. **Installer les dépendances :**
   ```bash
   uv sync
   ```

## 💻 Utilisation

Pour lancer le script principal :

```bash
uv run main.py
```

## 📦 Dépendances

Les bibliothèques principales utilisées sont :
- `openfoodfacts` : Client API officiel.
- `pandas` & `numpy` : Pour la manipulation de données (inclus dans l'environnement).

## 📄 Licence

Ce projet est sous licence standard pour un usage éducatif.
