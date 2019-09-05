from collections import deque
dequee = deque()
numComandos = int(input())
for x in range(0, numComandos):
        comando = list(map(str,input().split()))
        if comando[0] == "popleft":
                dequee.popleft()
        elif comando[0] == "pop":
                dequee.pop()
        elif comando[0] == "append":
                dequee.append(int(comando[1]))
        elif comando[0] == "appendleft":
                dequee.appendleft(int(comando[1]))
print(*dequee)
                        
                       
        
