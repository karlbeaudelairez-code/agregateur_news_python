import requests
from bs4 import BeautifulSoup
from models import Article
class Scraper:
    def __init__(self, url):
        self.url = url
        self.articles = []
    def scraper(self):
        reponse = requests.get(self.url)
        soupe = BeautifulSoup(reponse.text, "html.parser")
        titres = soupe.find_all("h2")
        for titre in titres:
            article = Article(
                titre = titre.text,
                source = self.url,
                date = "",
                lien = "",
                resume = ""
            )

            self.articles.append(article)