if __name__ == '__main__':
    n = int(input())
    modulo=int(n%2)
    
    if (modulo==1) or (5<n<21):
        print("Weird")
    else:
        print("Not Weird")

