n, k = input().split()
k = int(k)
s = str(sum(int(d) for d in n) * k)

while len(s) > 1:
    s = str(sum(int(d) for d in s))

print(s)