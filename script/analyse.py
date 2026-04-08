from connexion_sqlit_readfile import get_connection
from datetime import datetime

def save_results(type_analyse, valeur):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""INSERT INTO analyses_resultats (type_analyse, valeur, date_analyse) VALUES (?, ?, ?)""", (type_analyse, valeur, datetime.now().isoformat()))
    conn.commit()
    conn.close()
    
def chiffre_affaire():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""SELECT SUM(prix*quantite) FROM ventes 
                JOIN produits USING(id_produit)""")
    result = cur.fetchone()[0] or 0
    
    save_results("Le chiffre affaire total :", result) 
    conn.close()
    return result

def ventes_par_produit():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""SELECT nom, SUM(quantite) FROM ventes 
                JOIN produits USING(id_produit)
                GROUP BY nom""")
    result = cur.fetchall()
   
    for nom, total in result:
        save_results(f"Ventes pour le produit '{nom}':", total)
    
    print("Ventes par produit :", result)
    
    conn.close()
    return result

def ventes_par_ville():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""SELECT ville, SUM(prix*quantite) FROM ventes 
                JOIN produits USING(id_produit)
                JOIN magasins USING(id_magasin)
                GROUP BY ville""")
    result = cur.fetchall()
    for ville, total in result:
        save_results(f"Ventes pour la ville '{ville}':", total)
    
    print("Ventes par ville :", result)
    conn.close()
    return result

if __name__ == "__main__":
    chiffre_affaire()
    ventes_par_produit()
    ventes_par_ville()  