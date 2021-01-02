import requests
dict_superhero = { }
ready_superhero = [ ]
with open ("Супергерои") as f:
  list_of_superhero = f.readlines()
  for superhero in list_of_superhero:
    response = requests.get("https://superheroapi.com/api/2619421814940190/search/"+ superhero)
    data = response.json()
    ready_superhero.append(data)
    for datas in ready_superhero:
      d = datas["results"]
      for element in d:
        if element["name"] == "Hulk" or element["name"] == "Captain America" or element["name"] == "Thanos":
          a = element["name"]
          c = element["powerstats"]
          dict_superhero[a] = c["intelligence"]
          f = 0
smart_superhero = " "
for k, v in dict_superhero.items():
  i = int(v)
  if i > f:
    f = i
    smart_superhero = k
print("Самый умный супергерой:", smart_superhero)


