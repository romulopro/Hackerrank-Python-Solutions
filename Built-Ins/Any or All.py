numInteger, listInteger = int(input()), list(map(int, input().split()))
print(any([str(number)==str(number)[::-1] for number in listInteger]) and all([number>=0 for number in listInteger]))