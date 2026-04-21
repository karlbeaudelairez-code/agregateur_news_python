from scraper import Scraper

mot_cle = input("Veuillez entrer le mot cle: ")
scraper_obj = Scraper("https://www.bbc.com/afrique")
scraper_obj.scraper()

article_trouve = False
for article in scraper_obj.articles:
    if(article.contient_mot_cle(mot_cle)):
        print(article)
        article_trouve = True
if(article_trouve == False):
    print("Aucun article trouve pour ce mot cle.")