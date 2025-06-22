import mysql.connector
from mysql.connector import Error

import os
from dotenv import load_dotenv

# Charger les variables du fichier .env
load_dotenv()

paris_activities_data_list = [
    {"ville":"paris","nom": "Promenade sur les quais de Seine","budget":"faible", "type_activite": "journee", "prix": 0, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Visite du Sacré-Cœur", "budget":"faible","type_activite": "journee", "prix": 0, "duree": 90, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Flânerie dans le quartier Latin","budget":"faible", "type_activite": "journee", "prix": 0, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Exploration du Marché des Enfants Rouges","budget":"faible", "type_activite": "journee", "prix": 0, "duree": 90, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Pique-nique au Jardin du Luxembourg","budget":"faible","type_activite": "journee","prix": 0, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Balade sur la Coulée verte René-Dumont","budget":"faible","type_activite": "journee", "prix": 0, "duree": 150, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Visite du Parc des Buttes-Chaumont","budget":"faible","type_activite": "journee", "prix": 0, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Découverte des passages couverts","budget":"faible","type_activite": "journee","prix": 0, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Promenade au Canal Saint-Martin", "budget":"faible","type_activite": "journee","prix": 0, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Balade au cimetière du Père-Lachaise", "budget":"faible","type_activite": "journee","prix": 0, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},

    {"ville":"paris","nom": "Billet coupe-file Musée du Louvre", "budget":"moyen","type_activite": "journee","prix": 17, "duree": 180, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Tour Eiffel : billet sommet","budget":"moyen","type_activite": "journee", "prix": 26, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Croisière sur la Seine", "budget":"moyen","type_activite": "journee","prix": 15, "duree": 60, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Visite guidée du Musée d'Orsay","budget":"moyen","type_activite": "journee", "prix": 16, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Atelier de fabrication de macarons","budget":"moyen","type_activite": "journee", "prix": 45, "duree": 150, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Visite des Catacombes de Paris", "budget":"moyen","type_activite": "journee","prix": 29, "duree": 90, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Dégustation de vins et fromages", "budget":"moyen","type_activite": "journee","prix": 55, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Visite du Palais Garnier","budget":"moyen","type_activite": "journee", "prix": 14, "duree": 90, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Balade à vélo dans Paris","budget":"moyen","type_activite": "journee", "prix": 30, "duree": 180, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Visite du Musée Rodin","budget":"moyen","type_activite": "journee", "prix": 12, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Visite guidée privée du Louvre","budget":"eleve","type_activite": "journee", "prix": 250, "duree": 180, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Dîner-croisière de luxe","budget":"eleve","type_activite": "journee", "prix": 150, "duree": 180, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Spectacle Moulin Rouge (avec champagne)","budget":"eleve","type_activite": "journee", "prix": 120, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Cours de cuisine gastronomique", "budget":"eleve","type_activite": "journee","prix": 180, "duree": 180, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Excursion en montgolfière au-dessus de Paris","budget":"eleve","type_activite": "journee", "prix": 300, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Séance photo privée à Paris", "budget":"eleve","type_activite": "journee","prix": 200, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Visite en hélicoptère de Paris", "budget":"eleve","type_activite": "journee","prix": 400, "duree": 60, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Dégustation de champagne dans une cave","budget":"eleve","type_activite": "journee", "prix": 100, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Shopping privé dans les boutiques de luxe","budget":"eleve","type_activite": "journee", "prix": 200, "duree": 180, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Visite du Château de Versailles avec guide privé","budget":"eleve","type_activite": "journee", "prix": 280, "duree": 240, "tarifAdulte":0, "tarifEnfant":0},

    {"ville":"paris","nom": "Promenade nocturne sur les Champs-Élysées","type_activite": "soiree", "prix": 0, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Concert dans un bar de jazz","type_activite": "soiree", "prix": 10, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Cinéma en plein air","type_activite": "soiree", "prix": 12, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Soirée dans un bar étudiant", "type_activite": "soiree", "prix": 8, "duree": 180, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Balade le long du Canal Saint-Martin","type_activite": "soiree", "prix": 0, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Visite nocturne du Quartier Latin", "type_activite": "soiree", "prix": 0, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Dégustation de bières artisanales","type_activite": "soiree", "prix": 15, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Spectacle de rue","type_activite": "soiree", "prix": 0, "duree": 60, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Soirée jeux de société dans un café","type_activite": "soiree", "prix": 5, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Karaoké dans un bar","type_activite": "soiree", "prix": 7, "duree": 180, "tarifAdulte":0, "tarifEnfant":0},

    {"ville":"paris","nom": "Spectacle de cabaret","type_activite": "soiree", "prix": 50, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Dégustation de vins", "type_activite": "soiree", "prix": 40, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Visite nocturne d'un musée","type_activite": "soiree", "prix": 25, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Dîner-spectacle","type_activite": "soiree", "prix": 80, "duree": 180, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Soirée dans un club de jazz","type_activite": "soiree", "prix": 35, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Balade en bateau-mouche","type_activite": "soiree", "prix": 20, "duree": 60, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Visite guidée nocturne de Paris","type_activite": "soiree", "prix": 30, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Soirée dans un bar à cocktails","type_activite": "soiree", "prix": 45, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Concert dans une salle de spectacle","type_activite": "soiree", "prix": 60, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Match de football au Parc des Princes","type_activite": "soiree", "prix": 70, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},

    {"ville":"paris","nom": "Opéra à l'Opéra Garnier", "type_activite": "soiree", "prix": 150, "duree": 180, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Dîner gastronomique avec vue","type_activite": "soiree", "prix": 200, "duree": 180, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Soirée privée dans un club exclusif","type_activite": "soiree", "prix": 300, "duree": 180, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Spectacle au Lido","type_activite": "soiree", "prix": 180, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Soirée dans un bar à champagne","type_activite": "soiree", "prix": 120, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Dégustation de grands crus","type_activite": "soiree", "prix": 250, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Ballet à l'Opéra Bastille", "type_activite": "soiree", "prix": 160, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Soirée dans un club de jazz privé","type_activite": "soiree", "prix": 220, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Concert dans une salle de spectacle prestigieuse","type_activite": "soiree", "prix": 280, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
    {"ville":"paris","nom": "Match de football VIP au Parc des Princes","type_activite": "soiree", "prix": 350, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
]  

DB_HOST = os.environ.get("DB_HOST")
if DB_HOST is None:
    raise ValueError("La variable d'environnement 'DB_HOST' n'est pas définie dans .env ou l'environnement.")

DB_NAME = os.environ.get("DB_NAME")
if DB_NAME is None:
    raise ValueError("La variable d'environnement 'DB_NAME' n'est pas définie.")

DB_USER = os.environ.get("DB_USER")
if DB_USER is None:
    raise ValueError("La variable d'environnement 'DB_USER' n'est pas définie.")

DB_PASS = os.environ.get("DB_PASS")
if DB_PASS is None:
    raise ValueError("La variable d'environnement 'DB_PASS' n'est pas définie.")

DB_PORT = os.environ.get("DB_PORT")
if DB_PORT is None:
    raise ValueError("La variable d'environnement 'DB_PORT' n'est pas définie.")

conn = None
cur = None

try:
        conn = mysql.connector.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT
    )        
        db_info = conn.get_server_info()
        print(f"Connexion à la base de données MySQL sur TrueNAS réussie ! Version du serveur : {db_info}")
        # Créer un objet curseur pour exécuter les requêtes SQL
        cur = conn.cursor()

        # --- Requête SQL pour créer la table 'activities' ---
        create_activities_table_query = """
        CREATE TABLE IF NOT EXISTS activities (
            id SERIAL PRIMARY KEY,
            ville VARCHAR(100) NOT NULL,
            nom VARCHAR(255) NOT NULL,
            adresse VARCHAR(255),
            type_activite VARCHAR(50), 
            budget VARCHAR(100) NOT NULL,
            duree INT,                 
            prix DECIMAL(10, 2),       
            tarif_adulte DECIMAL(10, 2), 
            tarif_enfant DECIMAL(10, 2) 
        );
        """
        cur.execute(create_activities_table_query)
        print("Table 'activities' créée ou déjà existante.")
        
        
        
        # --- Requête SQL pour créer la table 'restaurants' ---
        create_restaurants_table_query = """
        CREATE TABLE IF NOT EXISTS restaurants (
            id SERIAL PRIMARY KEY,
            ville VARCHAR(100) NOT NULL,
            nom VARCHAR(255) NOT NULL,
            adresse VARCHAR(255),
            type_activite VARCHAR(50), 
            type_cuisine VARCHAR(100), 
            budget VARCHAR(100) NOT NULL,
            duree_repas INT              
        );
        """
        cur.execute(create_restaurants_table_query)
        print("Table 'restaurants' créée ou déjà existante.")

        # Valider les changements (appliquer les créations de tables)
        conn.commit()
        
         
# Version simplifiée sans ON CONFLICT pour cet exemple, qui permet les doublons si relancé
        insert_query_simple = """
        INSERT INTO activities (ville, nom, adresse, type_activite, duree, prix, tarif_adulte, tarif_enfant)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """

        all_activities_to_insert = []

        for activity in paris_activities_data_list:
            # Vos données incluent 'ville' et 'budget' directement dans chaque dict.
            # 'budget' n'est pas une colonne dans la table 'activities', donc nous l'ignorons à l'insertion.
            # L'adresse est ajoutée ici comme une valeur par défaut "Non spécifié" si elle manque.
            all_activities_to_insert.append((
                activity["ville"],
                activity["nom"],
                activity.get("adresse", "Non spécifié"), # Ajout d'une adresse par défaut si non présente
                activity["type_activite"],
                activity["duree"],
                activity["prix"],
                # Utilisez le prix si tarifAdulte est 0 dans les données, sinon utilisez tarifAdulte
                activity.get("tarifAdulte", 0) if activity.get("tarifAdulte", 0) != 0 else activity["prix"],
                activity.get("tarifEnfant", 0)
            ))

        cur.executemany(insert_query_simple, all_activities_to_insert) # Utilisation de la version simple
        conn.commit()
        print(f"{len(all_activities_to_insert)} activités insérées avec succès pour la ville de Paris.")

except Error as e:
        print(f"Erreur lors de l'insertion des activités : {e}")
        if conn:
            conn.rollback()
finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
        print("Connexion à la base de données fermée.")
        