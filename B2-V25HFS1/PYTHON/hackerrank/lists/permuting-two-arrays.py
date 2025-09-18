def permute(A,B,k):
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        if A[i]+B[i]<k:
            print("NO")
            return
    print("YES")
q=int(input())
for _ in range(q):
    n,k=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    permute(A,B,k)