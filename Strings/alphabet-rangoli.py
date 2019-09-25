import string
def print_rangoli(size):
  letraRangoli = size-1
  linha =[]
  linhaR=[]
  for i in range(0, size):
    for j in range(0, size*4-3):
      if(i-j >= 0):
        linha.insert(j,string.ascii_lowercase[size-1-j])
      else:
        linhaR.extend(linha[:j-1])
        linhaR.reverse()
        #l.extend(linha.pop(0))
        break
    linha.extend(linhaR)
    #print(linha)
    #print(linhaR)
    print(('-'.join(linha)).center(size*4-3,'-'))
    #print(s)
    linha =[]
    linhaR =[]
  for i in range (1,size):
    for j in range(0,size*4-3):
      if(size-1 -i-j >= 0):
        linha.insert(j,string.ascii_lowercase[size-1-j])
      else:
        linhaR.extend(linha[:j-1])
        linhaR.reverse()
        #l.extend(linha.pop(0))
        break
    linha.extend(linhaR)
    #print(linha)
    #print(linhaR)
    print(('-'.join(linha)).center(size*4-3,'-'))
    #print(s)
    linha =[]
    linhaR =[]
