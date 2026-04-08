-- Table PRODUIT
CREATE TABLE IF NOT EXISTS produits (
            id_produit TEXT PRIMARY KEY,
            nom TEXT,
            prix REAL,
            stock INTEGER
        )

-- Table MAGASIN
CREATE TABLE IF NOT EXISTS magasins (
            id_magasin INTEGER PRIMARY KEY AUTOINCREMENT,
            ville TEXT,
            nombre_salaries INTEGER
        );

-- Table VENTE 
CREATE TABLE IF NOT EXISTS ventes (
            id_vente INTEGER PRIMARY KEY AUTOINCREMENT,
            date_ventes TEXT,
            id_produit TEXT,
            quantite INTEGER,
            id_magasin INTEGER,
            foreign key (id_produit) references produits(id_produit),
            foreign key (id_magasin) references magasins(id_magasin)
        );

-- Table RESULTATS_ANALYSE
CREATE TABLE IF NOT EXISTS analyses_resultats (
            id_analyse INTEGER PRIMARY KEY AUTOINCREMENT,
            type_analyse TEXT,
            valeur REAL,
            date_analyse TEXT
);

