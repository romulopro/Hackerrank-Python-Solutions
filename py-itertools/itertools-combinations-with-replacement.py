# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
palavra, comb = map(str, input().split())
print(*[''.join(i) for i in combinations_with_replacement(sorted(palavra) ,int(comb))], sep="\n")
