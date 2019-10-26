import xml.dom.minidom
import urllib.request
import urllib.error

def convert_fun(date_to_search, curr_to_search, doc):

	# date_to_search = '2019-08-08'
	# curr_to_search = 'ISK'

	rate_res = 0
	#doc = xml.dom.minidom.parse('fee_change.xml')
	# url = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml'
	
	# doc = xml.dom.minidom.parse(urllib.request.urlopen(url))
	# print(doc.nodeName)
	# print(doc.firstChild.tagName)

	# cubes = doc.getElementsByTagName('Cube')
	env = doc.firstChild.childNodes[2] # main
	# print('--a-- ' + str(env.childNodes.length)) 
	#cube_main = env.childNodes[0] # main Cube
	for cube_bydate in env.childNodes:
		# print("\t " + str(cube_bydate.attributes['time'].value))
		
		for curr in cube_bydate.childNodes:
			#print(str(curr))
			date = cube_bydate.attributes['time'].value
			curr_str = curr.attributes['currency'].value
			if date == date_to_search and curr_str == curr_to_search:
				rate = curr.attributes['rate'].value
				print('date ' + date + ' curr = ' + curr_str + ' rate = ' + rate)
				rate_res = float(rate)

	return rate_res

