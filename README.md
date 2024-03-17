# Projet de Scraping de Données de Films

## Introduction

L'objectif de ce projet est de scraper des données à partir du site IMDb. Mais qu'est-ce que le scraping exactement ? Le scraping consiste à extraire des données d'une page HTML. Sur IMDb, nous chercherons à récupérer les informations suivantes (au minimum) pour chaque film :

- Titre
- Titre original
- Score
- Genre
- Année
- Durée
- Description (synopsis)
- Acteurs (casting principal)
- Public
- Pays
- [Facultatif] Langue d'origine

Pour les séries, nous pourrions également récupérer les informations suivantes :

- Nombre de saisons
- Nombre d'épisodes

## Objectifs

1. **Scraper les données et les sauvegarder dans un fichier .csv** : Dans un premier temps, l'objectif est de sauvegarder les informations scrapées dans un fichier CSV distinct pour les films et les séries.

2. **Stocker les données directement en BDD** : Dans un second temps, au lieu de stocker les données dans un fichier CSV, nous allons les stocker directement dans une base de données. Pour cela, nous utiliserons un pipeline Scrapy. Ce pipeline agira comme un processus ETL (Extract Transform Load), en extrayant les informations, en les nettoyant et en les stockant dans la base de données.

## Pipeline ETL

Le pipeline ETL se déroule en trois étapes :

1. **Extract (Extraction)** : Extraction des informations en les scrapant depuis la page IMDb.
2. **Transform (Transformation)** : Nettoyage et préparation des données pour qu'elles soient prêtes à être stockées.
3. **Load (Chargement)** : Stockage des données dans la base de données.

Nous veillerons à nettoyer les données dans le fichier pipeline.py avant de les sauvegarder dans la base de données.

## Objectifs du Projet

- Apprendre à scraper des données avec Scrapy.
- Maîtriser la sélection de données avec MongoDB.
- Gérer un projet avec GitHub.
- Déboguer le code.
