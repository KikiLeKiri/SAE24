from django.db import models

class Capteur(models.Model):
    id = models.AutoField(primary_key=True)
    nom_capteur = models.CharField(max_length=50)
    piece = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'capteur'

class Donnee(models.Model):
    id = models.AutoField(primary_key=True)
    datte = models.DateField()
    heure = models.TimeField()
    temperature = models.FloatField()
    id_capteur = models.ForeignKey(Capteur, on_delete=models.CASCADE, db_column='id_capteur')

    class Meta:
        managed = False
        db_table = 'donnee'

