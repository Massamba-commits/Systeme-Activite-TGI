# Application Web d'Authentification

Application web moderne avec système d'authentification sécurisé.

## 🚀 Technologies

### Backend
- Python 3.11+
- Flask
- PostgreSQL/Mysql
- JWT Authentication

### Frontend
- React 18
- Tailwind CSS
- Vite

## 📋 Prérequis

- Node.js 18+
- Python 3.11+
- PostgreSQL 15+
- Git

## 🛠️ Installation

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## 👥 Auteur

Votre Massamba et autres

## 📄 Licence

MIT License. 

Backend – Plateforme de gestion des utilisateurs et projets


===Description

Ce backend est développé avec Python et Flask.
Il permet la gestion des utilisateurs (stagiaires / admin), l’authentification, ainsi que les transactions ou dépôts de projets reliés aux utilisateurs inscrits dans la base de données MySQL.

L’architecture suit une séparation claire des responsabilités (MVC simplifié).

===Structure du projet
backend/
│── app.py
│── database/
│   └── db.py
│── models/
│   ├── user.py
│   └── transaction.py
│── auth/
│   └── auth.py
│── controllers/
│   ├── user_controller.py
│   └── transaction_controller.py
│── routes/
│   ├── user_routes.py
│   └── transaction_routes.py
│── uploads/

===Architecture et rôle des dossiers
🔹 app.py

Point d’entrée de l’application Flask
Initialise Flask
Enregistre les routes
Lance le serveur backend

🔹 database/db.py

Gère la connexion à la base de données MySQL
Centralise la configuration (host, user, password, database)
Fournit une connexion réutilisable aux autres classes

🔹 models/

Contient les classes métier qui interagissent directement avec la base de données.
user.py
Création des utilisateurs
Vérification de l’existence d’un email
Récupération des utilisateurs
Mise à jour et suppression
transaction.py
Gestion des transactions ou dépôts
Ajout d’un dépôt lié à un utilisateur
Liste des transactions par utilisateur

🔹 auth/auth.py

Gestion de l’authentification
Hashage sécurisé des mots de passe avec bcrypt
Vérification des identifiants lors de la connexion

🔹 controllers/

Contient la logique métier
Fait le lien entre les routes et les models
Traite les données avant l’accès à la base

🔹 routes/

Définit les endpoints de l’API REST
Reçoit les requêtes HTTP (GET, POST, PUT, DELETE)
Appelle les controllers correspondants
Exemples :
/register
/login
/users
/transactions

🔹 uploads/

Dossier destiné au stockage des fichiers uploadés
Exemple : dépôts de projets, documents, rapports

===Technologies utilisées

Python 3
Flask
MySQL
bcrypt (sécurité des mots de passe)
mysql-connector-python

====Équipe de développement

Ce backend a été réalisé en groupe de 3 personnes :
Fred Bello
Amdy Diokhane
Abdallah Fall

===Sécurité

Mots de passe hashés avec bcrypt
Séparation logique entre routes, contrôleurs et modèles
Les utilisateurs inscrits peuvent déposer leurs projets

===Explication simple pour l’oral

« Le backend est structuré en plusieurs couches.
Les routes reçoivent les requêtes, les contrôleurs traitent la logique, les modèles communiquent avec la base de données et l’authentification sécurise les accès.
Cette organisation rend le projet clair, sécurisé et facile à maintenir. »