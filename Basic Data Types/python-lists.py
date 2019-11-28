if __name__ == '__main__':
    N = int(input())
    novaLista = []
    
    for i in range(0,N):
        ent = input().split()
        comando=ent[0]
        argu = ent[1:]
        if comando != "print":
            comando = comando+"("+ ",".join(argu)+ ")"
            eval("novaLista."+comando)
        else:
            print (novaLista, sep=',')
            
            
            
