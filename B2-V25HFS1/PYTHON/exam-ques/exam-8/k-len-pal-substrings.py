# count how many k-len palindromic substrings exist in a given string

def palsub(s,k):
    for i in range(len(s),0,-1):
        for j in range(len(s)-i+1):
            t=s[j:j+i]
            if len(t)==k:
                if t==t[::-1]:
                    print(t)
s=input()
k=int(input())
palsub(s,k)