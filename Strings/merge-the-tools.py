def merge_the_tools(string, k):
  strpr =[]
  for x in range(0, int((len(string))/k)):
    for y in range( 0, k):
      if (string[x*k + y] not in strpr):
        strpr.append(string[x*k +y])
    print(''.join(strpr))
    strpr =[]    
  return
