n=int(input())
for _ in range(n):
    s1=input()
    s2=input()
    for i in s2:
        if i in s1:
            print("YES")
            break
    else:
        print("NO")