from functools import *
import math
l=[4,5,6,8,2,5]
print(reduce(lambda x,y:x+y,l))
print(reduce(lambda x,y:x if x>y else y,l))

# gcd of list of numbers
l1=[12,24,18,15,29,63]
print(reduce(math.gcd,l))