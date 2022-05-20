from django.db import models

# Create your models here.

class Groupedemetal(models.Model):
    registre = models.CharField(max_length=100)
    sous_registre = models.CharField(max_length=100)
    nom_du_groupe = models.CharField(max_length=100)
    nationalite = models.CharField(max_length=100)
    annee_de_creation = models.DateField(blank = True, null = True)
    nombre_album = models.IntegerField(blank = False)
    courte_description = models.TextField(null = True, blank = True)
    typedemetal = models.ForeignKey('typedemetal', on_delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = f"{self.nom_du_groupe} est un groupe de {self.registre}, {self.sous_registre}, de nationalité {self.nationalite}. Le groupe a vu le jour en {self.annee_de_creation} et compte aujourd'hui {self.nombre_album} album. {self.courte_description}."
        return chaine

    def dico(self):
        return {"nom_du_groupe":self.nom_du_groupe, "registre":self.registre, "sous_registre":self.sous_registre, "nationalite":self.nationalite, "anne_de_creation":self.annee_de_creation, "nombre_album":self.nombre_album, "courte_description":self.courte_description, "typedemetal":self.typedemetal}

class Typedemetal(models.Model):
    registre = models.CharField(max_length=100)
    sous_registre = models.CharField(max_length=100)
    resume = models.TextField(null  = True, blank = True)

    def __str__(self):
        rendue = f"Dans le registre du {self.registre} on retrouve {self.sous_registre}"
        return rendue

    def dico(self):
        return {"registre":self.registre, "sous_registre":self.sous_registre, "resume":self.resume}