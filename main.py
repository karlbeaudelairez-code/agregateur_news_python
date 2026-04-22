from scraper import Scraper
from aggregateur import Aggregateur

articles_filtres = []

mot_cle = input("Veuillez entrer le mot cle: ")

scraper1 = Scraper("https://www.rfi.fr/fr/afrique/rss")
scraper2 = Scraper("https://www.france24.com/fr/afrique/rss")
scraper3= Scraper("https://feeds.bbci.co.uk/afrique/rss.xml")

mon_aggregateur = Aggregateur()
mon_aggregateur.ajouter_scraper(scraper1)
mon_aggregateur.ajouter_scraper(scraper2)
mon_aggregateur.ajouter_scraper(scraper3)

mon_aggregateur.collecter()
articles_filtres = mon_aggregateur.filtrer(mot_cle)

if len(articles_filtres) > 0:
    print(f"{len(articles_filtres)} articles trouves pour le mot cle '{mot_cle}'.")
    for article in articles_filtres:
        print(article)
        print("\n")
else:
    print(f"Aucun article trouve pour le mot cle '{mot_cle}'.")