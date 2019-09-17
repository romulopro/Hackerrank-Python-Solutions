# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
A = list(map(int, input().split()))
B = list(map(int, input().split()))
for x in A:
        for y in B:
                print("(%d, %d)" %(x,y), end = ' ')
#print(list(product(A,B)))


