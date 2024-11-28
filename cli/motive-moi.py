import json
import random

def chercheMotivation():
  with open("../motivation.json", encoding='UTF8') as ok:
    motivation=json.load(ok)
  return motivation

def motiver(motivation):
  rand = random.randrange(0,len(motivation)-1)
  print(motivation[rand])
  input("")

if __name__ == "__main__":
  motivation = chercheMotivation()
  while(True):
    motiver(motivation)