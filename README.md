# web_api_converter
Language used: Python 3.7
Framework: Flask

List of files:
- converter.py contains the WEB api
- mylib.py contains function for xml file read
- make_get_request.py generates GET requests, used to test the API.

Example of GET:
http://localhost:5000/converter?amount=6&src_currency=NZD&dest_currency=RUB&reference_date=2019-09-24

Operating system used: Windows 10
Step to test:
- run activate.bat
- run converter.py
- run make_get_request.py
