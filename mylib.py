import xml.dom.minidom
import urllib.request
import urllib.error

def convert_fun(date_to_search, curr_to_search, doc):

	rate_res = 0

	env = doc.firstChild.childNodes[2] # main

	for cube_bydate in env.childNodes:

		
		for curr in cube_bydate.childNodes:
			#print(str(curr))
			date = cube_bydate.attributes['time'].value
			curr_str = curr.attributes['currency'].value
			if date == date_to_search and curr_str == curr_to_search:
				rate = curr.attributes['rate'].value
				print('date ' + date + ' curr = ' + curr_str + ' rate = ' + rate)
				rate_res = float(rate)

	return rate_res

