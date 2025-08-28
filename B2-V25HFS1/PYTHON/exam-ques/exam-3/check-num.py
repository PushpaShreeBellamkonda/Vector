# if given number contains 3 or 5
def fun(n):
    while n!=0:
        ld=n%10
        if ld==3 or ld==5:
            print("True")
            break
        n=n//10        
n=int(input())
fun(n)