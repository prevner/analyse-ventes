from create_db import create_table
from import_data import import_magasins, import_produits, import_ventes
from analyse import chiffre_affaire, ventes_par_produit, ventes_par_ville

print("Création de la base de données...")
create_table()  
print("Importation des données...")
import_magasins()
import_produits()
import_ventes()

print("Analyse des données...")
chiffre_affaire()   
ventes_par_produit()
ventes_par_ville()