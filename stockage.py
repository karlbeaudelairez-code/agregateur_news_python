import json
import sqlite3

class Stockage:
    def __init__(self):
        self.fichier_json = "articles.json"
        self.fichier_db = "articles.db"

    def sauvegarder_json(self, articles):
        try:
            list_dict = []
            for article in articles:
                list_dict.append(article.to_dict())
            with open(self.fichier_json, "w", encoding = "utf-8") as f:
                json.dump(list_dict, f, ensure_ascii = False, indent = 4)
        except Exception as e:
            print(f"Erreur lors de la sauvegarde du fichier json: {e}")
        
    def charger_json(self):
        try:
            with open(self.fichier_json, "r", encoding = "utf-8") as f:
                data = json.load(f)
            return data
        except Exception as e:
            print(f"Erreur lors du chargement du fichier json: {e}")
    
    def initialiser_db(self):
        connexion = sqlite3.connect(self.fichier_db)
        curseur = connexion.cursor()
        curseur.execute('''
            CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,      
                titre TEXT,
                source TEXT,
                date TEXT,
                lien TEXT,
                resume TEXT
                )
        ''')
        connexion.commit()
        connexion.close()

    def sauvegarder_db(self, articles):
        try:
            connexion = sqlite3.connect(self.fichier_db)
            curseur = connexion.cursor()
            for article in articles:
                curseur.execute('''
                    SELECT * FROM articles WHERE lien = ?
                ''', (article.lien,))
                if not curseur.fetchone():
                    curseur.execute('''
                        INSERT INTO articles (titre, source, date, lien, resume) 
                        VALUES (?, ?, ?, ?, ?)
                    ''', (article.titre, article.source, article.date, article.lien, article.resume))
            connexion.commit()
            connexion.close()
        except Exception as e:
            print(f"Erreur lors de la sauvegarde des articles dans  la base de donnees {e}")

    def rechercher_db(self, mot_cle):
        try:
            connexion = sqlite3.connect(self.fichier_db)
            curseur = connexion.cursor()
            curseur.execute('''
                SELECT * FROM articles
                WHERE titre LIKE ? OR resume LIKE ?
            ''', (f'%{mot_cle}%', f'%{mot_cle}%'))
            resultats = curseur.fetchall()
            connexion.close()
            return resultats
        except Exception as e:
            print(f"Erreur lors de la recherche dans la base de donnees ! {e}")