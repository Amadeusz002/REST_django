from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'


class Pvgis(models.Model):
    city = models.CharField(max_length=25)
    lon = models.IntegerField()
    lat = models.IntegerField()
    slope = models.IntegerField()
    azimuth = models.IntegerField()
    technology = models.CharField(max_length=25)
    peakPower = models.IntegerField()
    loss = models.IntegerField()

