n=int(input())
w="hackerrank"
for _ in range(n):
    s=input()
    i=0
    for ch in w:
        i=s.find(ch,i)
        if i==-1:
            print("NO")
            break
        i+=1
    else:
        print("YES")
