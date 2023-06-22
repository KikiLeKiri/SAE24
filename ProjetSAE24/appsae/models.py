from django.db import models

# Create your models here.

class Maison1(models.Model):
    messageid = models.AutoField(db_column='messageID', primary_key=True)
    id = models.CharField(max_length=50)
    piece = models.CharField(max_length=100)
    date_field = models.DateField(db_column='date_')
    heure = models.TimeField()
    temperature = models.FloatField()

    class Meta:
        managed = False
        db_table = 'maison1'

