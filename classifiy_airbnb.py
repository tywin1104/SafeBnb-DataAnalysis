import json
import requests
from airbnb import Airbnb


with open('output.json', 'r') as fh:
    raw = fh.read()
    listings = json.loads(raw)

    result = []
    for listing in listings[:10]:
        pic_url = listing.get('XL Picture Url')
        if not pic_url:
            print('No pic url, skip')
            continue
        zip_code = listing.get('Zipcode')
        if not zip_code:
            print('No zipcode·, skip')
            continue
        geocode_endpoint = f'http://www.mapquestapi.com/geocoding/v1/address?key=Ss0Djui9aTLold64q5lAtzw2lcg6kiJN&location={zip_code}'

        res = requests.get(geocode_endpoint)
        if not res.ok:
            raise Exception("Unable to fetch geocode info")
        jsonRes = res.json()
        coord = jsonRes['results'][0]['locations'][0]['latLng']
        lat = coord['lat']
        lng = coord['lng']

        obj = Airbnb(lat, lng)

        analysis = obj.process_danger_level()

        listing['danger_index'] = analysis.get('danger_index')
        listing['crimes_count'] = analysis.get('crimes_count')
        print(f'processed one danger_index successfully')

        result.append(listing)

    with open('alldata.json', 'w') as fh:
        fh.write(json.dumps(result))

