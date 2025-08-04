amt=int(input("enter the amount:"))

n200=amt//200
amt=amt%200

n20=amt//20
amt=amt%20

n5=amt//5
amt=amt%5

n1=amt%1

print("no of 200s are :",n200)
print("no of 20s are :",n20)
print("no of 5s are :",n5)
print("no of 1s are :",n1)
