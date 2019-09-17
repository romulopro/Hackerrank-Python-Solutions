# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
stringA = list(input())
for repeticoes,letraRepetida in groupby(stringA):
  print(*[(len(list(letraRepetida )),int(repeticoes))], end = " ")
