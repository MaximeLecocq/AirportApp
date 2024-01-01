from django.test import TestCase

from .models import Airport


#test for Airport model

from django.test import TestCase
from .models import Airport

class AirportModelTest(TestCase):

    # Set up the test data
    def setUp(self):
        Airport.objects.create(
            airport_id=1,
            airport_name="Test Airport",
            airport_type=Airport.SMALL,
            latitude=40.7128,
            longitude=-74.0060,
            elevation=50,
            continent=Airport.NORTH_AMERICA,
            country="United States",
            municipality="New York"
        )

    def test_airport_str(self):
        # Test for the string representation of the Airport model
        airport = Airport.objects.get(airport_id=1)
        # Check if the string representation matches the expected value
        self.assertEqual(airport.__str__(), "Test Airport")

    # Test for the choices of airport types in the model
    def test_airport_type_choices(self):
        # Retrieve an instance of Airport from the test data
        airport = Airport.objects.get(airport_id=1)
        # Check if the displayed airport type matches the expected value
        self.assertEqual(airport.get_airport_type_display(), "small airport")

    def test_airport_continent_choices(self):
        airport = Airport.objects.get(airport_id=1)
        self.assertEqual(airport.get_continent_display(), "North America")

    
    def test_airport_ordering(self):
        # Retrieve all instances of Airport with the specified ordering
        airports = Airport.objects.all().order_by(
            'airport_id', 'airport_name', 'airport_type', 'latitude', 'longitude', 'elevation', 'continent', 'country', 'municipality'
        )
        # Get the ordering fields as a list from the query object
        ordering_fields = list(airports.query.order_by)
        # Check if the retrieved ordering matches the expected ordering
        self.assertEqual(
            ordering_fields,
            ['airport_id', 'airport_name', 'airport_type', 'latitude', 'longitude', 'elevation', 'continent', 'country', 'municipality']
        )