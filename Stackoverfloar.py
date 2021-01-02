import requests
from pprint import pprint
list_of_questions = [ ]
response = requests.get("https://api.stackexchange.com/2.2/questions", params = {"order": "desc", "fromdate": "1609372800", "todate": "1609545600", "sort": "activity", "site": "ru.stackoverflow"})
response.raise_for_status()
data = response.json()
#pprint(data)
c = data["items"]
for element in c:
  if "python" in element["tags"]:
    url = element["link"]
    pprint(element["title"])