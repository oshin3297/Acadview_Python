#Question1:Use the "https://api.forismatic.com/api/1.0/" api to get random quotes using the correct endpoints.
import requests
quote=requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en")
import json
data=quote.json()
print(type(data))
print(data["quoteText"])
