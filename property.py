import csv
import time
from distance import distance


class Property:
    MCIS_WEIGHT = {
            "Break and Enter": 1.2,
            "Assault": 1.5,
            "Theft Over": 0.5,
            "Robbery": 1.5,
            "Auto Theft": 0.1
    }
    MCIS =(
        [
            'Break and Enter', 'Assault',
            'Theft Over', 'Robbery',
            'Auto Theft']
    )

    def __init__(self, _lat, _long):
        self.location = (_lat, _long)
        self.crimes_count = dict()
        self.danger_index = 0

    def process_danger_level(self):
        for mic in self.MCIS:
            self.crimes_count[mic] = 0

        with open('MCI_2014_to_2017.csv', 'r') as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                incident_lat = row.get('Lat')
                incident_long = row.get('Long')

                incident_location = (incident_lat, incident_long)
                dist = distance(self.location, incident_location)

                if dist < 2:
                    mci = row.get('MCI')
                    current_count = self.crimes_count.get(mci, 0)
                    self.crimes_count[mci] = current_count + 1
                    self.danger_index += self.MCIS_WEIGHT.get(mci)

    def show_result(self):
        if len(self.crimes_count) == 0:
            raise Exception('Must process danger level first')

        print(self.crimes_count)
        print(f'Property unsafe index: {self.danger_index}')
