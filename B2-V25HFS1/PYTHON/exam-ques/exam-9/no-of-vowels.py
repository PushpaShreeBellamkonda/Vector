# number of vowels in a string

def vowels(s):
	c=0
	for i in s:
		if i in "aeiou":
			c+=1
	return c
s=input()
print(vowels(s))			