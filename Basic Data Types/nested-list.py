if __name__ == '__main__':
    listaNome = []
    listaNota = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        listaNome.append(name)
        listaNota.append(score)
    listaNotaOrdem=[]
    listaNotaOrdem.extend(listaNota)
    listaNotaOrdem.sort()
    listaNotaOrdemSemRep =[]
    i=0
    while i < len(listaNotaOrdem):
      if listaNotaOrdem[i] not in listaNotaOrdemSemRep:
        listaNotaOrdemSemRep.append(float(listaNotaOrdem[i]))
      i=i+1
    #print(listaNotaOrdemSemRep)
    listaNotaOrdemSemRep.pop(0)
    #print(listaNotaOrdemSemRep)
    listaNomeOrdem =[]
    for x in range (0, len(listaNota)):
      #print(listaNota[x])
      if (listaNota[x] == listaNotaOrdemSemRep[0]):
        listaNomeOrdem.append(listaNome[x])
    listaNomeOrdem.sort()
    i=0
    for i in range(0, len(listaNomeOrdem)):
      print(listaNomeOrdem[i])
      
    
        
        
