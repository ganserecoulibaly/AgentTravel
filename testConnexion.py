import mysql.connector
from mysql.connector import Error

import os
from dotenv import load_dotenv

# Charger les variables du fichier .env
load_dotenv()

# truenas : créer un dataset et donner les droits
# créer une instance dans maria db en spécifiant le chemin
# 
# 
# 
# 

# --- Remplacez par les informations de votre TrueNAS MySQL/MariaDB ---
#DB_HOST = "192.168.1.25" # Ex: 192.168.1.100
#DB_NAME = "travel" # Ou le nom de votre DB, par défaut souvent vide ou 'mysql'
#DB_USER = "travel" # Ou 'root'
#DB_PASS = "travel"
#DB_PORT = 3306 # Le "Node Port" que vous avez configuré

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
try:
    conn = mysql.connector.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT
    )

    if conn.is_connected():
        db_info = conn.get_server_info()
        print(f"Connexion à la base de données MySQL sur TrueNAS réussie ! Version du serveur : {db_info}")

        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print(f"Vous êtes connecté à la base de données : {record[0]}")

        # Vous pouvez maintenant exécuter vos requêtes de test
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255));")
        conn.commit()
        print("Table 'users' créée ou déjà existante.")

        cursor.execute("INSERT INTO users (name) VALUES ('Alice'), ('Bob');")
        conn.commit()
        print("Utilisateurs insérés.")

        cursor.execute("SELECT * FROM users;")
        users = cursor.fetchall()
        print("\nUtilisateurs dans la base de données :")
        for user in users:
            print(user)

except Error as e:
    print(f"Erreur lors de la connexion ou de l'opération sur MySQL : {e}")
    # Vérifiez votre pare-feu sur TrueNAS si la connexion est refusée
    # Assurez-vous que le conteneur est "Running" dans l'interface TrueNAS
finally:
    if conn and conn.is_connected():
        cursor.close()
        conn.close()
        print("Connexion MySQL fermée.")