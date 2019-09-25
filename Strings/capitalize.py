import string
def capitalize(stringa):
  listaPalavras = []
  #listaPalavras =stringa 
  listaPalavras.append(stringa[0].upper())
  for x in range (0,len(stringa)-1):
    if(stringa[x] == " "):
      listaPalavras.append(stringa[x+1].upper())
    else:
       listaPalavras.append(stringa[x+1])  
      #print(listaPalavras[x])
  s = "".join(listaPalavras)
  return s
