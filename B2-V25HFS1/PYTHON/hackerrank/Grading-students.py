n=int(input())
grades=[int(input()) for _ in range(n)]
rg=[]
for i in grades:
    if i>=38:
        nm=(((i//5)+1)*5)
        if (nm-i)<3:
            rg.append(nm)
        else:
            rg.append(i)
    else:
        rg.append(i)
for i in rg:
    print(i)