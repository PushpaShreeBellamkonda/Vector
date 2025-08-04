#first case

for i in range(10,20):
    if i%3==0:
        print(i)
        break
print("\n")
#second case

for i in range(10,20):
    if i%3==0:
        break
    print(i)
print("\n")
#third case

for i in range(10,20):
    print(i)
    if i%3==0:
        break
print("\n")
# fourth case

for i in range(11,25):
    if i%5==0 or i%7==0:
        break
    print(i)
