import sqlite3
import csv
from datetime import datetime

DB_PATH = 'database/ventes.db'

#fonction qui permet de se connecter à la base de données SQLite
def get_connection():
    return sqlite3.connect(DB_PATH)

#fonction qui permet de lire un fichier CSV et retourner une liste de dictionnaires
def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)