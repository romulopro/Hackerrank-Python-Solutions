from collections  import OrderedDict
numPalavras = int(input())
dicQuantPalavras = OrderedDict()
for x in range(0, numPalavras):
        palavra = str(input())
        if palavra not in dicQuantPalavras:
                dicQuantPalavras[palavra] = 1
        else:
                dicQuantPalavras[palavra] += 1
print(len(dicQuantPalavras))
for palavra in dicQuantPalavras:
        print (dicQuantPalavras[palavra], end=" ")
               
