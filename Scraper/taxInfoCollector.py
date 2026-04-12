import requests
import re
import csv

# avoid creating new connections each time
session = requests.Session()

def convertToAddress(street, cityState, zipCode):
	street = street.strip()
	# r'[\s,] + ([A-Z]{2})$' finds whitespace and commas, then gets the state abbreviation
	cityState = re.sub(r'[\s,]+([A-Z]{2})$', r', \1', cityState.strip()) # and then replaces it as City, ST
	zip = zipCode.strip()[0:5]

	return '{}, {} {}'.format(street, cityState, zip)

def main(accountID, townID, townName):
	headers = {
		'Host': 'api.edmundsgovtech.cloud',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:149.0) Gecko/20100101 Firefox/149.0',
		'Accept': 'application/json, text/plain, */*',
		'X-Wipp-Id': townID
	}

	endpoints = [ # until I find more
        'https://api.edmundsgovtech.cloud/wipp-core/v1/wippTaxes/{}'.format(accountID),
        'https://api.edmundsgovtech.cloud/wipp-core/v1/wippPropInfo/{}'.format(accountID)
	]

	# saving some space
	ownerName = propertyLocation = address = None
	landValue = improvementValue = netValue = None
	taxTotals = {}

	for url in endpoints:
		response = session.get(url, headers=headers, timeout=5)
		if (response.status_code != 200):
			# print('Something\'s wrong: {} | URL to check: {}'.format(response.status_code, url))
			continue

		json = response.json()
		data = json['propertyInfo'] if 'propertyInfo' in json else json
		foundData = False

		if 'ownerName' in data:
			ownerName = data['ownerName'].strip()
			propertyLocation = data['propertyLoc'].strip() + ", " + townName
			ownerStreet, ownerCitySt, ownerZip = data['ownerStreet1'], data['ownerCitySt'], data['ownerZip']
			address = convertToAddress(ownerStreet, ownerCitySt, ownerZip)
			landValue = data['landValue']
			improvementValue = data['imprValue']
			netValue = data['netValue']
			foundData = True

		if 'taxYears' in json:
			for year in json['taxYears']:
				try:
					total = sum([
						float(json['taxYears'][year]['NJTAX'][0]['qtr1OrigBilled'] or 0),
						float(json['taxYears'][year]['NJTAX'][0]['qtr2OrigBilled'] or 0),
						float(json['taxYears'][year]['NJTAX'][0]['qtr3OrigBilled'] or 0),
						float(json['taxYears'][year]['NJTAX'][0]['qtr4OrigBilled'] or 0)
					])
					taxTotals[year] = f'{total:.2f}' # creates a list with year and total tax
				except:
					pass

		if foundData: break # to get wippTaxes before before wippPropInfo if wippTaxes doesn't have a valid field'

	T2026 = taxTotals.get('2026', '0.00') # default to 0.00 if none
	T2025 = taxTotals.get('2025', '0.00')
	T2024 = taxTotals.get('2024', '0.00')
	T2023 = taxTotals.get('2023', '0.00') # only goes back to 2023, I believe

	return [ownerName, propertyLocation, address, T2026, T2025, T2024, T2023, landValue, improvementValue, netValue]

if __name__ == '__main__':
	with open('3address_output.csv', mode='w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(['Account ID', 'Owner Name', 'Property Location', 'Owner Location', '2026 Tax', '2025 Tax', '2024 Tax', '2023 Tax', 'Land Value', 'Improvement Value', 'Net Value']) # need help

		for i in range(0, 18500):
			accountID = '{:08d}'.format(i) # generate integers padded with 0s until 8 digits
			elements = main(accountID, '1204', 'EAST BRUNSWICK, NJ 08816')
			if elements and elements[0]: # make sure ownerName is not empty
				writer.writerow([accountID] + elements)
			if (i % 100 == 0): print('{} elements gotten'.format(i))