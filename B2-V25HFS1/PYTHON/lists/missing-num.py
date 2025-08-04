# A list contains numbers between m to n except one number,display the missing number

l=list(map(int,input().split()))
for i in range(min(l),max(l)):
    if i not in l:
        print(i)
        break
