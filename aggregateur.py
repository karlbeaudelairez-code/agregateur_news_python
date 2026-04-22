from scraper import Scraper
from models import Article
class Aggregateur:
    def __init__(self):
        self.scrapers = []
        self.articles = []

    def ajouter_scraper(self, scraper):
        if len(self.scrapers) < 20:
            self.scrapers.append(scraper)
        else:
            print("Impossible d'ajouter un nouveau scraper. On continue avec les scrapers qui sont la.\n")
    def collecter(self):
        for scrap in self.scrapers:
            scrap.scraper()
            self.articles += scrap.articles
    def filtrer(self, mot_cle):
        articles_filtres = []
        for article in self.articles:
            if article.contient_mot_cle(mot_cle):
                articles_filtres.append(article)
        return articles_filtres

    
