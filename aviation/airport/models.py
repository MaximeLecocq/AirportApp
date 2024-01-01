from django.db import models

# Create your models here.

class Airport (models.Model):
    def __str__(self):
        return self.airport_name

    # variables for airport types
    LARGE = "LARGE"
    MEDIUM = "MEDIUM"
    SMALL = "SMALL"
    SEAPLANE = "SEAPLANE"
    HELIPORT = "HELIPORT"

    AIRPORT_TYPES = [
        (LARGE, "large airport"),
        (MEDIUM, "medium airport"),
        (SMALL, "small airport"),
        (SEAPLANE, "seaplane base"),
        (HELIPORT, "heliport"),
    ]

    # variables for continents
    ASIA = "ASIA"
    SOUTH_AND_CENTRAL_AMERICA = "SOUTH_AND_CENTRAL_AMERICA"
    OCEANIA = "OCEANIA"
    AFRICA = "AFRICA"
    EUROPE = "EUROPE"
    NORTH_AMERICA = "NORTH_AMERICA"
    ANTARTICA = "ANTARTICA"

    CONTINENTS = [
        (ASIA, "Asia"),
        (SOUTH_AND_CENTRAL_AMERICA, "South and Central America"),
        (OCEANIA, "Oceania"),
        (AFRICA, "Africa"),
        (EUROPE, "Europe"),
        (NORTH_AMERICA, "North America"),
        (ANTARTICA, "Antartica"),
    ]

    airport_id = models.IntegerField(("id of airport"), null=False, blank=False, primary_key=True)
    airport_name = models.CharField(("name of airport"),max_length=100, null=False, blank=False)
    airport_type = models.CharField(("type of airport"),max_length=25,choices=AIRPORT_TYPES)
    latitude = models.FloatField("latitude degree")
    longitude = models.FloatField("longitude degree")
    elevation = models.IntegerField("elevation", null=True, blank=True)
    continent = models.CharField(("continent"),max_length=40,choices=CONTINENTS)
    country = models.CharField(("country"),max_length=100)
    municipality = models.CharField(("municipality"),max_length=100, null=True, blank=True)
    

    class Meta:
        ordering = ['airport_id', 'airport_name', 'airport_type', 'latitude', 'longitude','elevation','continent','country','municipality']