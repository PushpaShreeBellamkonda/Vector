# remove negative numbers from a list

from functools import *
l=list(map(int,input().split()))
print(list(filter(lambda x:x>=0,l)))