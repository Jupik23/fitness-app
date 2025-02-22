from django.db import models


class ZajecieFitness(models.Model):
    nazwa = models.CharField(max_length=100)
    instruktor = models.CharField(max_length=100)
    data = models.DateTimeField()
    liczba_miejsc = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nazwa} - {self.data.strftime('%d-%m-%Y %H:%M')}"
