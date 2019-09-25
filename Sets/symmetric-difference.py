m = input()
mlis = list(map(int, input().split()))
n = input()
listfinal =[]
nlis = list(map(int, input().split()))
for numero in (set(mlis)).difference(nlis):
  listfinal.append(numero)
for numero in (set(nlis)).difference(mlis):
  listfinal.append(numero)
listfinal.sort()
for numero in listfinal:
  print(numero)
