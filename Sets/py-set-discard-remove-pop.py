n = int(input())
s = set(map(int, input().split())) 
commandos = int(input())
for x in range (0,commandos):
  entrada = list((input().split()))
  if entrada[0]== 'pop':
    s.pop()
  elif entrada[0]== 'remove':
    s.remove(int(entrada[1]))
  elif entrada[0]== 'discard':
    s.discard(int(entrada[1]))
  #print(s)
print(int(sum(s)))
