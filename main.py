from scraper import Scraper
from aggregateur import Aggregateur
from stockage import Stockage

while True:
    print("<-------------------------------------------- AGREGATEUR DE NEWS -------------------------------------------->\n")
    print("\t\t\t\t\tMenu\n1- Rechercher des articles par mot cle\n2- Rechercher dans la base de donnees\n3- Quitter\n")
    Choix = input("Votre choix: ")
    match Choix:
        case "1":
            articles_filtres = []

            mot_cle = input("Veuillez entrer le mot cle: ")

            scraper1 = Scraper("https://www.rfi.fr/fr/afrique/rss")
            scraper2 = Scraper("https://www.france24.com/fr/afrique/rss")
            scraper3 = Scraper("https://feeds.bbci.co.uk/afrique/rss.xml")
            scraper4 = Scraper("https://voaafrique.com/api/zmgqo-omqp/")

            mon_aggregateur = Aggregateur()
            mon_aggregateur.ajouter_scraper(scraper1)
            mon_aggregateur.ajouter_scraper(scraper2)
            mon_aggregateur.ajouter_scraper(scraper3)
            mon_aggregateur.ajouter_scraper(scraper4)
            mon_aggregateur.collecter()
            articles_filtres = mon_aggregateur.filtrer(mot_cle)

            if len(articles_filtres) > 0:
                print(f"{len(articles_filtres)} articles trouves pour le mot cle '{mot_cle}'.")
                for article in articles_filtres:
                    print(article)
                    print("\n")
            else:
                print(f"Aucun article trouve pour le mot cle '{mot_cle}'.")

            if len(mon_aggregateur.articles) > 0:
                mon_stockage = Stockage()
                mon_stockage.initialiser_db()
                mon_stockage.sauvegarder_json(mon_aggregateur.articles)
                mon_stockage.sauvegarder_db(mon_aggregateur.articles)
                print("Articles sauvegardes en JSON et dans la base de donnees !")
            else:
                print("Aucun article a sauvegarder !")
        case "2":
            mot_cle = input("Veuillez entrer le mot cle pour la recherche dans la base de donnees: ")
            mon_stockage = Stockage()
            resultats = mon_stockage.rechercher_db(mot_cle = mot_cle)
            if resultats:
                print(f"{len(resultats)} articles trouves pour le mot cle '{mot_cle}' dans la base de donnees.\n")
                for resultat in resultats:
                    print(f"Titre: {resultat[1]}\nSource: {resultat[2]}\nDate: {resultat[3]}\nLien: {resultat[4]}\nResume: {resultat[5]}\n")
            else:
                print(f"Aucun article trouve pour le mot cle '{mot_cle}' dans la base de donnees.\n")
        case "3":
            print("Nous vous remercions d'avoir utilise notre agregateur\nAu revoir !")
            break
        case _:
            print("Choix invalide ! Veuillez choisir une option valide.\n")