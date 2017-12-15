
cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):

    listOfFibNums = [0,1]
    if(n == 0): return []
    elif (n==1 ): return [0]
    else:
        for x in range(1, n-1):
            listOfFibNums.append(listOfFibNums[x-1] + listOfFibNums[x])
    return listOfFibNums
    # return a list of fibonacci numbers
    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
    
