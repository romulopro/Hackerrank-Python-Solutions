m = list(map(int, input().split()))
n = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))
totalhappiness = 0

ab = a.union(b)

#n.sort()

for numero in n:
  if (numero in ab):
    if(numero in a):
      totalhappiness += 1
    else:
      totalhappiness -= 1
  

print(totalhappiness)
