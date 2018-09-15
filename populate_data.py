import csv
import time
from distance import distance

start = time.time()

MCIS = ['Break and Enter', 'Assault', 'Theft Over', 'Robbery', 'Auto Theft']

MCIS_WEIGHT= {
    "Break and Enter": 1.2,
    "Assault": 1.5,
    "Theft Over": 0.6,
    "Robbery": 1.5,
    "Auto Theft": 0.3
}

example_listing_location = (43.6590996, -79.3821182)

crimes = dict()
for mic in MCIS:
    crimes[mic] = 0


with open('MCI_2014_to_2017.csv', 'r') as fh:
    reader = csv.DictReader(fh)
    danger_index = 0
    for row in reader:
        incident_lat = row.get('Lat')
        incident_long = row.get('Long')

        dist = distance(example_listing_location, (incident_lat, incident_long))
        if dist < 2:
            mci = row.get('MCI')
            current_count = crimes.get(mci, 0)
            crimes[mci] = current_count + 1
            danger_index += MCIS_WEIGHT.get(mci)

    print(f'The danger index for this property area is {danger_index}')

print(crimes)


finish = time.time()
print(f'Finished simple iteration in {finish-start} seconds')
