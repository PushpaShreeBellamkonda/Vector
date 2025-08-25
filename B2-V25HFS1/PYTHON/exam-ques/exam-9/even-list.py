# return a new list with even numbers from a given list

def even_list(l):
	l1=[]
	for i in l:
		if i%2==0:
			l1.append(i)
	return l1
l=list(map(int,input().split()))
print(even_list(l))