# Chapitre 1 — Installation environnement Odoo 19

## Objectif

Créer un environnement Docker
pour développer GreenCheck.

## Technologies

- Docker Compose
- Odoo 19
- PostgreSQL 16

## Structure

greencheck-odoo

├── addons
├── config
└── docker-compose.yml


## Création du projet

Commandes :

mkdir greencheck-odoo
cd greencheck-odoo

## Lancement

docker compose up -d


## Résultat

Odoo accessible :

http://localhost:8070