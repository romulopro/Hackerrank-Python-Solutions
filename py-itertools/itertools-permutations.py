from itertools import permutations
a = list(map(str, input().split()))
palavra = sorted(a[0])
nDePermutacoes = int(a[1])
print(*[''.join(i) for i in permutations("".join(palavra), nDePermutacoes)], sep="\n")


