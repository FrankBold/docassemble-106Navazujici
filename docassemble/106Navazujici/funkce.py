import json
import requests

def ziskejSituace():
  page = requests.get("https://da-test.frankbold.org/playgroundstatic/PravoNaInformace/1/situace.json")
  y = json.loads(page.content)
  dict = {}

  for x in y["Situace"]:
    dict[x["ID"]] = x["title"]
  return dict
