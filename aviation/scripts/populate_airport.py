#scripts populate_airport.py
import os
import sys
import csv
import django
from aviation.airport.models import Airport  # Import Django model


aviation_project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "C:/Users/mmlec/Desktop/AWD Midterm/aviation"))
sys.path.append(aviation_project_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aviation.settings')

django.setup()

def load_airport_data_from_csv(file_path):
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            # Create an instance of the Airport model for each row in the CSV
            airport = Airport(
                airport_id=row['airport_id'],
                airport_name=row['airport_name'],
                airport_type=row['airport_type'],
                latitude=row['latitude'],
                longitude=row['longitude'],
                elevation=row['elevation'],
                continent=row['continent'],
                country=row['country'],
                municipality=row['municipality']
            )
            airport.save()

if __name__ == '__main__':
    # Path to the CSV file
    csv_file_path = 'C:/Users/mmlec/Desktop/AWD Midterm/aviation/airports.csv'
    
    # Call the function to load data from CSV to the Airport model
    load_airport_data_from_csv(csv_file_path)