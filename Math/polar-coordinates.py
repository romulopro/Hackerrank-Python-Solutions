import cmath
litstr = str(input())
real = 0
imag = 0
#for letra in litstr:
# if letra =='+' or letra =='-':
#  real = (litstr[:letra])
#   imag = (litstr[letra+1:-1])
  
  

print(*cmath.polar(complex(litstr)), sep="\n")
