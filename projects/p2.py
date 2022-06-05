from urllib import response
from urllib.request import urlopen
import json
url="https://api.github.com"
response=urlopen(url)
data_json=json.loads(response.read())
print(data_json)