def print_formatted(number):
    # your code goes here
    i=1
    dist = len(str(bin(number))[2:])
    while (i<=number):
        print(str(i).rjust(dist," ")+" "+str(oct(i))[2:].rjust(dist," ")+" "+str(hex(i))[2:].rjust(dist," ").upper()+" "+str(bin(i))[2:].rjust(dist," "))
        i +=1
    return
