#!flask/bin/python
from flask import Flask
from flask import request, jsonify
from mylib import *
import xml.dom.minidom
import urllib.request
import urllib.error
from datetime import date
import datetime

app = Flask(__name__)

# PARAMS = {"amount": str(tot), "currency" : dest }
try:
	url = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml'
	doc = xml.dom.minidom.parse(urllib.request.urlopen(url))
except Exception as e:
	print('Error unable to retreive exchange rate')
	raise e

all_curr = ['USD', 'JPY', 'BGN', 'CZK', 'DKK', 'GBP', 'HUF', 'PLN', 'RON', 'SEK', 'CHF', 'ISK', 'NOK', 'HRK', 'RUB', 'TRY', 'AUD', 'BRL', 'CAD', 'CNY', 'HKD', 'IDR', 'ILS', 'INR', 'KRW', 'MXN', 'MYR', 'NZD', 'PHP', 'SGD', 'THB', 'ZAR']

	
@app.route('/converter', methods=['GET'])
def convert():
	
	if 'amount' in request.args:
		try:
			x = int(request.args['amount'])
		except Exception as e:
			code = 802
			msg = 'Bad format amount to convert'
			return msg, code
	else:
		return "Error: No field amount."
	if 'src_currency' in request.args:
		src = request.args['src_currency']
		if src not in all_curr:
			code = 803
			msg = 'Start currency not found'
			return msg, code
	else:
		return "Error: No field src_currency."
	if 'dest_currency' in request.args:
		dest = request.args['dest_currency']
		if dest not in all_curr:
			code = 803
			msg = 'End currency not found'
			return msg, code
	else:
		return "Error: No field dest_currency."
	if 'reference_date' in request.args:
		try:
			in_date = request.args['reference_date']
			end_date = date.today().toordinal()
			start_date = date.today().toordinal() - 90
			this_date = datetime.datetime.strptime(in_date, '%Y-%m-%d').toordinal()
			
			if this_date < start_date or this_date > end_date:
				code = 801
				msg = 'date out of range (90 days ago, today)'
				return msg, code
			temp_date = date.fromordinal(this_date)
			weekday = temp_date.weekday()
			if weekday == 5 or weekday == 6:
				code = 804
				msg = 'saturdays and sundays not accepted'
				return msg, code
		except Exception as e:
			return "Error: date bad format"
		
	else:
		return "Error: No field reference_date."

	rate1 = convert_fun(in_date, src, doc)
	rate2 = convert_fun(in_date, dest, doc)

	result = (float(x) * rate1) / rate2
	result = float("{0:.2f}".format(result))

	PARAMS = {"amount": str(result), "currency" : dest }

	return jsonify(PARAMS)
	

if __name__ == '__main__':

	app.run(debug=True)
