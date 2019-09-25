def minion_game(string):
  ptStuart = 0
  ptKevin = 0
  tamanhoString = len(string)
  vogais = 'AEIOU'
  for x in range (0, tamanhoString):
    if (string[x] not in vogais):
      ptStuart += len(string)-x
         #print("stuart " + string[x:y])
    else:
      ptKevin += len(string)-x
          #print("kevin " + string[x:y])
  if(ptStuart>ptKevin):
    print("Stuart %d" %ptStuart)
  elif(ptStuart<ptKevin):
    print("Kevin %d" %ptKevin)
  else:
    print("Draw")
