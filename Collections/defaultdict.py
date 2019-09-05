from collections import defaultdict
numPalavras, quantGrupos = map(int, input().split())
dictPalavrasA = defaultdict(list)
#grupo A de palavras
for x in range (1, numPalavras+1):
        palavra = str(input())
        dictPalavrasA[palavra].append(x)
for x in range (1, quantGrupos+1):
        palavra = str(input())
        if palavra  in dictPalavrasA.keys():
                print(*dictPalavrasA.get(palavra))
        else:
                print('-1')


         
                

