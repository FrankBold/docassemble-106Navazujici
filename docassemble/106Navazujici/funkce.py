import json
import requests
from docassemble.base.util import *

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
    if x["parent"] == int(parent) and x["titleMinus"] != None:
      dict[x["ID"]] = x["titleMinus"]
  return dict

def obsahArgumentu(id):
  page = requests.get("https://da-test.frankbold.org/playgroundstatic/PravoNaInformace/1/argumenty.json")
  y = json.loads(page.content)
  dict = {}

  for x in y["Argumenty"]:
    if x["ID"] == int(id):
      dict = x.copy()
  return dict

def obsahDuvodu(id):
  page = requests.get("https://da-test.frankbold.org/playgroundstatic/PravoNaInformace/1/duvody.json")
  y = json.loads(page.content)
  dict = {}

  for x in y["Duvody"]:
    if x["ID"] == int(id):
      dict = x.copy()
  return dict

def obsahSituace(id):
  page = requests.get("https://da-test.frankbold.org/playgroundstatic/PravoNaInformace/1/situace.json")
  y = json.loads(page.content)
  dict = {}

  for x in y["Situace"]:
    if x["ID"] == int(id):
      dict = x.copy()
  return dict
