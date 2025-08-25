def toh(n,s,d,a):
    if n==1:
        print(f"disc 1 moved from {s} to {d}")
    else:
        toh(n-1,s,a,d)
        print(f"disc {n} moved from {s} to {d}")
        toh(n-1,a,d,s)
n=int(input())
toh(n,'sc','dt','ax')
