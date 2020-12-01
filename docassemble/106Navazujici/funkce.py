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
  page = requests.get("https://da-test.frankbold.org/playgroundstatic/PravoNaInformace/1/duvody.json")
  y = json.loads(page.content)
  dict = {}

  for x in y["Duvody"]:
    if x["parent"] == int(parent) and x["v"] == 1:
      dict[x["ID"]] = x["title"]
  return dict

def ziskejArgumentyProti(parent):
  page = requests.get("https://da-test.frankbold.org/playgroundstatic/PravoNaInformace/1/argumenty.json")
  y = json.loads(page.content)
  dict = {}

  for x in y["Argumenty"]:
    if x["parent"] == int(parent):
      dict[x["ID"]] = x["titleMinus"]
  return dict
