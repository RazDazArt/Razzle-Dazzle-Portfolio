import requests
import json

BASE_URL = "https://api.github.com/repos/fawaz-strawberry/fawaz-strawberry.github.io/contents/stock_data.js"
# HEADERS = {"APCA-API-KEY-ID":API_KEY, "APCA-API-SECRET-KEY":SECRET_KEY}
HEADERS = {"Accept": "application/vnd.github.v3+json"}

import base64
data = open("C:/Users/Fawaz Mujtaba/Documents/GitHub/fawaz-strawberry.github.io/stock_data.js", "rb").read()
encoded = base64.b64encode(data)
print(str(encoded))
encoded = json.dumps(encoded.decoded
#DATA = {"message":"Updated Tickers", "content":encoded}

r = requests.put(url=BASE_URL, data=encoded, headers=HEADERS, auth=("fawaz-strawberry", "3933c72e12d9f89bcbd608579b0717ac6f883163"))
print(r.request.url)
print(json.loads(r.content))