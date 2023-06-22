from django.db import models

# Create your models here.

class Capteur(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    nom_capteur = models.CharField(max_length=50)
    piece = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'capteur'


class Donnee(models.Model):
    id_capteur = models.ForeignKey(Capteur, models.DO_NOTHING, db_column='id_capteur')
    date_field = models.DateField(db_column='date_')
    heure = models.TimeField()
    temperature = models.FloatField()

    class Meta:
        managed = False
        db_table = 'donnee'

