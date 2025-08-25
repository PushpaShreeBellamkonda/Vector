# form the largest possible number from digits in a string,if no digitd print -1

def largest(s):
    l=[]
    for i in s:
        if i.isdigit():
            l.append(i)
    if len(l)==0:
        return -1
    l.sort(reverse=True)
    return "".join(l)
s=input()
print(largest(s))