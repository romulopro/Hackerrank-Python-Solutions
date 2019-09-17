# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
palavra, comb = map(str, input().split())
for x in range(1, int(comb)+1):
        print(*[''.join(i) for i in combinations(sorted(palavra) ,x)], sep="\n")
