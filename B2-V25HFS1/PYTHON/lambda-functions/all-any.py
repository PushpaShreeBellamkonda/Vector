l=[True,True,True,True]
print(all(l))
l=[True,True,False,True]
print(all(l))
l=[True,True,False,True]
print(any(l))
l=[False,False,False,False]
print(any(l))
l=[6,9,43,6,87,4,7,3]
print(all(map(lambda x:x>0,l)))
print(any(map(lambda x:x<0,l)))