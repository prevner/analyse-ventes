
# 📊 Analyse des ventes d’une PME
**Projet Data Engineer – Architecture Docker & SQLite**

## 🧭 Contexte du projet

Ce projet s’inscrit dans le cadre d’un **exercice de positionnement Data Engineer**.  
L’objectif est de mettre en place une **architecture data simple, conteneurisée**, permettant à une PME d’analyser ses ventes afin de faciliter la prise de décision stratégique.

Les données exploitées concernent :
- les ventes sur une période de 30 jours,
- les produits,
- les magasins répartis dans plusieurs villes.

---

## 🎯 Objectifs

- Concevoir une architecture Docker à deux services
- Stocker les données dans une base SQLite
- Importer les données depuis des fichiers CSV
- Garantir l’unicité des ventes (absence de doublons)
- Réaliser des analyses SQL
- Produire des indicateurs business exploitables

---

## 🏗️ Architecture technique

### Services

| Service | Rôle |
|------|----|
| data_runner | Exécution des scripts Python (création DB, import, analyses) |
| sqlite_db | Stockage persistant des données SQLite |

### Fonctionnement
- Communication via un volume Docker partagé
- Le service `data_runner` démarre après `sqlite_db`

---

## 📁 Structure du projet

```
projet-ventes-pme/
│
├── Dockerfile
├── docker-compose.yml
│
├── data/
│   ├── magasins.csv
│   ├── produits.csv
│   └── ventes.csv
│
├── scripts/
│   ├── init_db.py
│   ├── import_data.py
│   └── run_analysis.py
│
└── README.md
```

---

## 🗃️ Modélisation des données

### Table magasins
- id_magasin (clé primaire)
- ville
- nombre_salaries

### Table produits
- id_produit (clé primaire)
- nom
- prix
- stock

### Table ventes
- id_vente (clé primaire)
- date
- id_produit (clé étrangère)
- quantite
- id_magasin (clé étrangère)

✅ Une contrainte d’unicité est appliquée sur (date, id_produit, id_magasin).

---

## 🚀 Lancement du projet

### Prérequis
- Docker
- Docker Compose

### Commande

```bash
docker-compose up --build
```

Cette commande permet de :
- créer la base de données,
- importer les données,
- exécuter les analyses.

---

## 📊 Analyses réalisées

- Chiffre d’affaires total
- Chiffre d’affaires par produit
- Chiffre d’affaires par ville

---

## 📈 Résultats clés

- **Chiffre d’affaires total** : 5 268,78 €
- **Produit le plus rentable** : Produit D
- **Villes les plus performantes** : Lyon et Marseille

---

## ✅ Compétences mises en œuvre

- Docker & Docker Compose
- Modélisation relationnelle
- SQLite
- Python (ingestion & automatisation)
- SQL analytique

---

## 🔮 Améliorations possibles

- Ajout d’un outil de visualisation (Metabase, Power BI)
- Migration vers PostgreSQL
- Orchestration avec Airflow

---

## 👤 Auteur

Projet réalisé dans le cadre d’un **positionnement Data Engineer – Simplon.co**
