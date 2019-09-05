#!/bin/python3

import sys
from collections import Counter, OrderedDict
from collections import defaultdict
class OrderedCounter(Counter, OrderedDict):
	pass


if __name__ == "__main__":       
        dicLetras = OrderedCounter(sorted(input())).most_common(3)
  
        for k in dicLetras:
                print(*k)
                
        

