import json
import requests

def ziskejSituace():
  page = requests.get("https://da-test.frankbold.org/playgroundstatic/PravoNaInformace/1/situace.json")
  y = json.loads(page.content)
  dict = {}

  for x in y["Situace"]:
    dict[x["ID"]] = x["title"]
  return dict

def ziskejDuvody(parent):
  page = requests.get("https://da-test.frankbold.org/playgroundstatic/PravoNaInformace/1/situace.json")
  y = json.loads(page.content)
  dict = {}

  for x in y["Duvody"]:
    if x["parent"] == parent and x["v"] == 1:
      dict[x["ID"]] = x["title"]
  return dict
