import requests
from bs4 import BeautifulSoup
from models import Article
class Scraper:
    def __init__(self, url):
        self.url = url
        self.articles = []
    def scraper(self):
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
            reponse = requests.get(self.url, headers=headers, timeout=90)
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
            print(f"{len(self.articles)} articles trouves.")
        except Exception as e:
            print(f"Erreur de connexion : {e}")