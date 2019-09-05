from collections import OrderedDict
numItens = int(input())
itensSupermercado = OrderedDict()
for x in range(numItens):
        mercadoriaEpreco = list(map(str,input().split()))
        preco = int(mercadoriaEpreco.pop())
        mercadoria = " ".join(mercadoriaEpreco)
        if mercadoria not in itensSupermercado:
                itensSupermercado[mercadoria] = int(preco)
        else:
                itensSupermercado[mercadoria] += int(preco)
for merca, preco in itensSupermercado.items():
        print(merca, preco)




