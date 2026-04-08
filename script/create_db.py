from connexion_sqlit_readfile import get_connection

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    
    #création de la table produits
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produits (
            id_produit TEXT PRIMARY KEY,
            nom TEXT,
            prix REAL,
            stock INTEGER
        )
    """)
    
    #création de la table magasins
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS magasins (
            id_magasin INTEGER PRIMARY KEY AUTOINCREMENT,
            ville TEXT,
            nombre_salaries INTEGER
        );
    """)
    #création de la table ventes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ventes (
            id_vente INTEGER PRIMARY KEY AUTOINCREMENT,
            date_ventes TEXT,
            id_produit TEXT,
            quantite INTEGER,
            id_magasin INTEGER,
            foreign key (id_produit) references produits(id_produit),
            foreign key (id_magasin) references magasins(id_magasin)
        );
    """)
    
    #creation de la table analyses_resultats (analyses et calculs historiques)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analyses_resultats (
            id_analyse INTEGER PRIMARY KEY AUTOINCREMENT,
            type_analyse TEXT,
            valeur REAL,
            date_analyse TEXT
        );
    """)
    
    conn.commit()
    conn.close()
    
    print('Tables créées avec succès.')
    
    if __name__ == '__main__':
        create_table()