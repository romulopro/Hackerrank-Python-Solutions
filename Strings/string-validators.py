if __name__ == '__main__':
    isalnum, isalpha, isdigit, islower, issuper =False,False,False,False,False,
    s = input()
    for letra in s:
        if(letra.isalnum()):
            isalnum = True
        if(letra.isalpha()):
            isalpha = True
        if(letra.isdigit()):
            isdigit = True
        if(letra.islower()):
            islower = True
        if(letra.isupper()):
            issuper = True
    print("%r \n%r \n%r \n%r \n%r" %(isalnum, isalpha, isdigit, islower, issuper))
        

