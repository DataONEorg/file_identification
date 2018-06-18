import requests

#url = "http://localhost/~pratikshrivastava/fgdc-1998/01_fgdc-1998.xml"
url = "http://localhost/~pratikshrivastava/eml-211/00_eml-211.xml"

request = requests.get(url)

print(request.headers)
print(url)
print(request)
