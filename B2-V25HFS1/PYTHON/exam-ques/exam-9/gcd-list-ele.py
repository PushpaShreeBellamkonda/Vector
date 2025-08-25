# gcd of list of numbers

from functools import reduce
import math
l=list(map(int,input().split()))
print(reduce(math.gcd,l))