import random

ok=[
"T'es trop beau ",
"Tu mérites de faire et avoir ce que tu veux",
"Tu trouveras ce que tu cherches",
"Tu accompliras ta légende personnelle",
"L'univers est avec toi",
"Ta famille t'aimes",

]

def motiver():
  rand = random.randrange(0,len(ok)-1)
  print(ok[rand])
  input("")

while(True):
  motiver()