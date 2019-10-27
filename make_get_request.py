
# importing the requests library 
import requests 
import json
import random
from random import randrange
from datetime import date
  

def main():
	# api-endpoint  --- my local url
	URL = "http://localhost:5000/converter"
	  
	all_curr = ['USD', 'JPY', 'BGN', 'CZK', 'DKK', 'GBP', 'HUF', 'PLN', 'RON', 'SEK', 'CHF', 'ISK', 'NOK', 'HRK', 'RUB', 'TRY', 'AUD', 'BRL', 'CAD', 'CNY', 'HKD', 'IDR', 'ILS', 'INR', 'KRW', 'MXN', 'MYR', 'NZD', 'PHP', 'SGD', 'THB', 'ZAR']
	
	curr_1 = randrange(len(all_curr))
	while 1:
		curr_2 = randrange(len(all_curr))
		if curr_1 != curr_2:
			break

	# random currency
	src = all_curr[curr_1]
	dest = all_curr[curr_2]

	# random amount
	x = randrange(20)
	

	# random date
	while 1:
		end_date = date.today().toordinal()
		start_date = date.today().toordinal() - 90
		ref_date = date.fromordinal(random.randint(start_date, end_date))
		weekday = ref_date.weekday()
		if weekday != 5 and weekday != 6:
			break

	print(ref_date)

	PARAMS = {"amount": str(x), "src_currency": src, "dest_currency" : dest, 'reference_date' : ref_date }
	print('GET request: ' + str(PARAMS))
	  
	# sending get request and saving the response as response object 
	r = requests.get(url = URL, params = PARAMS) 
	
	if r.status_code != 200:
		# This means something went wrong.
		print('error '+ str(r.status_code))
		# extracting data in json format 
	else:
		data = r.json() 
		json_str = json.dumps(data)
		result = json.loads(json_str)
		print('RESPONSE ' + str(result))
	
if __name__ == "__main__":
	main();
