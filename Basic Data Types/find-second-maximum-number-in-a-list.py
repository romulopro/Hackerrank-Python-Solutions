if __name__ == '__main__':
  n = int(input())
  arr = map(int, input().split())
  lista= list(arr)
  lista.sort()
  i=0
  final2 = []
  #print(lista[i])
#print(len(lista))
  while i<len(lista):
    if lista[i] not in final2:
      final2.append(lista[i])
    i = i+ 1
  final2.pop()
  print(final2[len(final2) - 1])
