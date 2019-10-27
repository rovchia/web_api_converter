# web_api_converter
Language used: Python 3.7
Framework: Flask
Operating system used: Windows 10

List of files:
- converter.py contains the code to activate the RESTful web service
- mylib.py library with function used by converter to read the XML file containing the exchange rates
- make_get_request.py contains the code for generate GET requests with random parameters. It can be used to test the API.

Example of GET:
http://localhost:5000/converter?amount=6&src_currency=NZD&dest_currency=RUB&reference_date=2019-09-24

Step to test the web API with command prompt:
- run "./activate.bat" and "python converter.py" to activate the web service
- run "python make_get_request.py" to generate the GET request: 
    the parameters of the request (amount, src_currency, dest_currency, date) will be displayed as output on the shell
    the result received as reponse (amount, currency) will be displayed as output
 
Notes: 
- The XML containing the exchange rates is stored dynamically at the startup of the web service
(internet connection is necessary to retreive the file at startup)
