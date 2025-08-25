# count frequency of every char in a string
def count(s):
    d={}
    for i in s:
        d[i]=d.get(i,0)+1
    return d
s=input()
print(count(s))