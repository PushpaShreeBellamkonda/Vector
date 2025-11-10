def fun(s, t, k):
    same = 0
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            same += 1
        else:
            break

    # find how many total operations needed
    ops = (len(s) - same) + (len(t) - same)

    # check if possible
    if k >= ops and ( (k - ops) % 2 == 0 or k >= len(s) + len(t) ):
        print("Yes")
    else:
        print("No")

s = input()
t = input()
k = int(input())
fun(s, t, k)
