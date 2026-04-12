import requests
import csv
import time
import os
from urllib.parse import quote

def geocoder(address):
    # urlib quot adds %20 for spaces
    url = "https://api.maptiler.com/geocoding/{}.json".format(quote(address.strip()))

    params = {
        "fuzzyMatch": "true",
        "limit": 1, # top result
        "key": os.environ.get("GEOCODE_API_KEY")
    }

    for attempt in range(5): # if fail once, try four more times
        try:
            response = requests.get(url, params=params, timeout=10)

            if response.status_code == 200:
                features = response.json().get("features", [])

                if features:
                    result = features[0]
                    center = result.get("center", [])

                    if len(center) >= 2:
                        lon = center[0]
                        lat = center[1]

                        return f"({float(lat):.7f}, {float(lon):.7f})"
                return ''

            elif response.status_code == 429 or response.status_code == 503:
                print('You got rate limited. Waiting {} seconds'.format(2 ** attempt))
                time.sleep(2 ** attempt)
                continue

            else:
                print('Error for {}: {}'.format(address, response.status_code))
                return ''

        except Exception as e:
            print('Something went wrong ({}): Trial #{}/5'.format(e, attempt + 1))
            time.sleep(5)

    return ""

def processAddresses(inputFile, outputFile):
    with open(inputFile, mode='r', newline='') as inFile, open(outputFile, "w", newline='') as outFile:
        reader = csv.DictReader(inFile)
        inputFields = reader.fieldnames

        outputFields = list(inputFields) + ["Coordinates"] # add coordinates as a new column
        writer = csv.DictWriter(outFile, fieldnames=outputFields)
        writer.writeheader()

        for index, row in enumerate(reader, 1): # start index at 1
            address = row.get("Property Location", "").strip()

            if address:
                print('Geocoding #{} for {}...'.format(index, address))
                coords = geocoder(address)
                row["Coordinates"] = coords
            else:
                row["Coordinates"] = ""

            writer.writerow(row)
            outFile.flush()  # write to disk right after

            time.sleep(0.05) # to not overwhelm the geocoding server

if __name__ == "__main__":
    processAddresses('3address_output.csv', 'address_output_f.csv')
    print("Completed!")