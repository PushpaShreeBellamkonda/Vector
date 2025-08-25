# how many times "madam" can be repeated from a given string

def repeated(s,t):
    l=[]
    for i in set(t):
        l.append(s.count(i)//t.count(i))
    return min(l)
s=input()
t=input()
print(repeated(s,t))
        
