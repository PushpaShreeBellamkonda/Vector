# return a new list with square of all elements from a given list

from functools import *
l=list(map(int,input().split()))
print(list((map(lambda x:x*2,l))))
	