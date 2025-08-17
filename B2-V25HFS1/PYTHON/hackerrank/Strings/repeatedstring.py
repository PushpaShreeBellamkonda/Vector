s=input()
n=int(input())
a_s=s.count("a") #count of 'a' in the string
r=n//len(s)  #no of times to repeat the string
rem=n%len(s)  #remaining characters after full repeats
a_rem=s[:rem].count("a") #count of 'a' in the remaining part of the string
#total count of 'a' in the repeated string
total=r*a_s+a_rem
print(total)

