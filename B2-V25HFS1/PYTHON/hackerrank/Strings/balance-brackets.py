def matched(s):
    st=[]
    for i in s:
        if i in "{[(":
            st.append(i)
        else:
            if len(st)==0:
                print("NO")
                return
            else:
                if i=='}' and st[-1]=='{':
                    st.pop()
                elif i==']' and st[-1]=='[':
                    st.pop()
                elif i==')' and st[-1]=='(':
                    st.pop()
                else:
                    print("NO")
                    return
    else:
        if len(st)==0:
            print("YES")
        else:
            print("NO")
n=int(input())
for i in range(n):
    s=input()
    matched(s)