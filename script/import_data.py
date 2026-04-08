from connexion_sqlit_readfile import get_connection, read_csv

def import_produits():
    data = read_csv('data/produits.csv')
    conn = get_connection()
    cur = conn.cursor()
    for row in data:
        cur.execute("""
            INSERT OR REPLACE INTO produits (id_produit,nom, prix, stock) VALUES (?, ?, ?, ?)
        """, (row['Reference_produit'], row['Nom'], row['Prix'], row['Stock']))

    conn.commit()
    conn.close()
    
    print('Produits importés avec succès.')
    
# importation des magasins
def import_magasins():
    data = read_csv('data/magasins.csv')
    conn = get_connection()
    cur = conn.cursor()
    for row in data:
        cur.execute("""
            INSERT OR REPLACE INTO magasins (id_magasin, ville, nombre_salaries) VALUES (?, ?, ?)
        """, (row['ID_Magasin'], row['Ville'], row['Nombre_salaries']))

    conn.commit()
    conn.close()
    
    print('Magasins importés avec succès.')

# permets de vérifier si une vente existe déjà dans la base de données pour éviter les doublons
def vente_existe(datee, id_produit, id_magasin):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT 1 FROM ventes WHERE date_ventes = ? AND id_produit = ? AND id_magasin = ?
    """, (datee, id_produit, id_magasin))
    
    exists = cur.fetchone() is not None
    conn.close()
    return exists


# importation des ventes
def import_ventes():
    conn = get_connection()
    data  = read_csv('data/ventes.csv')
    cur = conn.cursor()
    
    counter = 0 #counter le nombre de ventes importées
    
    for row in data:
        date_v = row['date_ventes']
        id_produit = row['Reference_produit']
        id_magasin = row['ID_Magasin']
        
        if not vente_existe(date_v, id_produit, id_magasin):
            cur.execute("""
                INSERT INTO ventes (date_ventes, id_produit, quantite, id_magasin) VALUES (?, ?, ?, ?)
            """, (date_v, id_produit, row['Quantite'], id_magasin))
            counter += 1
        
    conn.commit()
    conn.close()
    
    print(f'{counter} ventes importées avec succès.')
if __name__== "__main__":
    import_produits()
    import_magasins()
    import_ventes()