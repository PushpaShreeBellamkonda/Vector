# longest word length from a list of strings

def longest(l):
	max=len(l[0])
	el=l[0]
	for i in l:
		if len(i)>max:
			max=len(i)
			el=i
	return max
l=list(input().split())
print(longest(l))
		