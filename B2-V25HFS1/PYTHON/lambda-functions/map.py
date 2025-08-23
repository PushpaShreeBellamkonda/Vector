import math
l=[1,2,3,4]
print(list(map(math.factorial,l)))
print(list(map(lambda x:x*2,l)))

def sqrt(n):
    return "{:.2f}".format(n**0.5)
l=[1,2,3,4]
print(list(map(sqrt,l)))