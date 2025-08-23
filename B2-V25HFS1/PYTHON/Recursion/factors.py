def fact(n,i=1):
    if n==i:
        print(n)
    else:
        if n%i==0:
            print(i)
        fact(n,i+1)
n=int(input())
fact(n)