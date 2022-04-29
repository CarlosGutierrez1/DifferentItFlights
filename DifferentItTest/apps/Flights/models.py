from tabnanny import verbose
from django.db import models


class Flight(models.Model):
    numberFlightID = models.BigAutoField(primary_key=True)
    departureTimestamp = models.CharField(max_length=100)
    arrivalTimestamp = models.CharField(max_length=100)
    departureIata = models.CharField(max_length=100)
    arrivalIata = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    class Meta:
        ordering = ['numberFlightID']
        verbose_name = 'Flight'
        verbose_name_plural = 'Flights'
    def __str__(self):
        return 'Flight  {} {} - {}'.format(str(self.numberFlightID), self.departureIata, self.arrivalIata)

