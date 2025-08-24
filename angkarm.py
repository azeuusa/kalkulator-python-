import random

def tebak_angka():
  rahasia = random.randint(1, 10)
  tebakan = None
  while tebakan != rahasia:
      tebakan = int(input("tebak tebakan kontol dari si DFTr ini jawab: "))
      if tebakan < rahasia:
          print("letik san goblok")
      elif tebakan > rahasia:
           print("badag teing kontol")
  print ("maneh bener anjijggggggg: ", rahasia)
tebak_angka()