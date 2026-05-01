from flask import Flask, render_template, request
from scraper import Scraper
from aggregateur import Aggregateur
from stockage import Stockage
from datetime import datetime

app = Flask(__name__)

def preparer_aggregateur():
    agg = Aggregateur()
    urls = [
          "https://www.rfi.fr/fr/rss",
          "https://www.france24.com/fr/actualites/rss"
          "https://feeds.bbci.co.uk/afrique/rss.xml"
          "https://voaafrique.com/api/zmgqo-omqp/"
        ]
    for url in urls:
        agg.ajouter_scraper(Scraper(url))
        return agg
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recherche_web', methods=['GET', 'POST'])
def recherche_web():
    resultats = []
    mot_cle = ""
    if request.method == 'POST':
        mot_cle = request.form.get('mot_cle')
        mon_aggregateur = preparer_aggregateur()
        mon_aggregateur.collecter()
        resultats = mon_aggregateur.filtrer(mot_cle)
        total_collectes = len(resultats)

        if mon_aggregateur.articles:
            mon_stockage = Stockage()
            mon_stockage.initialiser_db()
            mon_stockage.sauvegarder_db(mon_aggregateur.articles)
            mon_stockage.sauvegarder_json(mon_aggregateur.articles)
            
    return render_template('recherche_web.html', articles=resultats, mot=mot_cle)

@app.route('/recherche_db', methods=['GET', 'POST'])
def recherche_db():
    resultats = []
    mot_cle = ""
    if request.method == 'POST':
        mot_cle = request.form.get('mot_cle')
        mon_stockage = Stockage()
        resultats = mon_stockage.rechercher_db(mot_cle=mot_cle)
        
    return render_template('recherche_db.html', articles=resultats, mot=mot_cle)

if __name__ == '__main__':
    app.run(debug=True)


