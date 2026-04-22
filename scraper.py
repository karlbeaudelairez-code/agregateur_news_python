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
            reponse = requests.get(self.url, headers=headers, timeout=60)
            soupe = BeautifulSoup(reponse.text, "xml")
            items = soupe.find_all("item")
            for item in items:
                article = Article(
                    titre = item.title.text.strip() if item.title else "",
                    source = self.url,
                    date = item.pubDate.text.strip() if item.pubDate else "",
                    lien = item.link.text.strip() if item.link else "",
                    resume = item.description.text.strip() if item.description else ""
                )
                self.articles.append(article)
        except Exception as e:
            print(f"Erreur de connexion : {e}")