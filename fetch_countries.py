import codecs
import json
import requests


url = "https://restcountries.com/v3.1/all"


response = requests.get(url)
data = response.json()


countries = []
for country in data:
    code = country["cca2"]
    name = country["translations"]["ara"]["official"]
    idd_root = country.get("idd", {}).get("root", "")
    idd_suffixes = country.get("idd", {}).get("suffixes", [])
    key = idd_root + "".join(idd_suffixes)
    countries.append({"code": code, "name": name, "key": key})

with codecs.open("countries.json", "w", encoding='utf-8') as file:
    json.dump(countries, file, ensure_ascii=False, indent=4)
