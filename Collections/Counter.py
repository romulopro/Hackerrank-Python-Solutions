# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
numSapatos=  int(input())
dinheiroVendas = 0
lisTamanhoSapatos= list(map(int, input().split()))
numConsumidores = int(input())
for i in range (0,numConsumidores):
        tamSapato, precoSapato = map(int, input().split())
        if tamSapato in Counter(lisTamanhoSapatos).keys():
                dinheiroVendas += precoSapato
                lisTamanhoSapatos.remove(tamSapato)
print(dinheiroVendas)
