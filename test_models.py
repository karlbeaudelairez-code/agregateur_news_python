
from models import Article 
from stockage import Stockage
def test_contient_mot_cle():
    article = Article("Iran actualites", "BBC", "", "", "")
    assert article.contient_mot_cle("Iran") == True
    assert article.contient_mot_cle("Football") == False

def test_to_dict():
    article = Article("Iran actualites", "BBC", "2026-04-22", "https://bbc.com", "Resume test")
    d = article.to_dict()
    assert d["titre"] == "Iran actualites"
    assert d["source"] == "BBC"

def test_str():
    article = Article("Titre test", "RFI", "2026-04-22", "https://rfi.fr", "Resume")
    assert "Titre test" in str(article)
    assert "RFI" in str(article)

def test_charger_json():
    stockage = Stockage()
    assert stockage.charger_json() is not None

def test_sauvegarder_db():
    stockage = Stockage()
    stockage.initialiser_db()
    stockage.sauvegarder_db([Article("Test DB", "Test Source", "2026-04-22", "https://test.com", "Resume test")])
    assert stockage.rechercher_db("Test DB") is not None