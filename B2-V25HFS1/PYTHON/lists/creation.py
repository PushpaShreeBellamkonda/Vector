# when inputs are in line by line
n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
print(l)

print()

# when inputs are in same line
l=list(map(int,input().split()))
print(l)

print()

# list comprehension (ip are line by line)
n=int(input())
l=[int(input()) for i in range(n)]
print(l)

print()

#another method
l=[]
for i in input().split():
    l.append(int(i))
print(l)

print()

# another method
l=[int(i) for i in input().split()]
print(l)
