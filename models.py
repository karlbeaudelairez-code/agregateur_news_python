

class Article:
    def __init__(self, titre, source, date, lien, resume):
        self.titre = titre
        self.source = source
        self.date = date
        self.lien = lien
        self.resume = resume
    def __str__(self):
        return f"Titre: {self.titre}\nSource: {self.source},\nDate: {self.date},\nLien: {self.lien},\nResume: {self.resume}"
    def to_dict(self):
        return {
            "titre": self.titre,
            "source": self.source,
            "date": self.date,
            "lien": self.lien,
            "resume": self.resume
        }
    def contient_mot_cle(self, mot_cle):
        return mot_cle.lower() in self.titre.lower() or mot_cle.lower() in self.resume.lower()