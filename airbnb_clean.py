import csv
import requests
import json


def cleanup():
    with open('airbnb-listings.csv', 'r', encoding='ISO-8859-1') as fh:
        reader = csv.DictReader(fh)
        count = 0
        total = []
        for row in reader:
            if count >= 500:
                break
            listing_url = row.get('Listing Url', None)
            if listing_url:
                res = requests.get(listing_url)
                histories = res.history
                if histories == []:
                    print(f"Expired url for {listing_url}")
                    continue
                else:
                    total.append(row)
                    count += 1
                    print(f'Fetch successfullty for {listing_url} @ {count}')
    print('All finished')
    return json.dumps(total)

with open('output.json', 'w') as fh:
    result = cleanup()
    fh.write(result)


