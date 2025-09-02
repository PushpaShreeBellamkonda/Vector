def bal():
    st=[]
    s=input()
    for i in s:
        if i in "{[(":
            st.append(i)
        else:
            if len(st)==0:
                print("not balanced")
                break
            else:
                if i=='}' and st[-1]=='{':
                    st.pop()
                elif i==']' and st[-1]=='[':
                    st.pop()
                elif i==')' and st[-1]=='(':
                    st.pop()
                else:
                    print('Not balanced')
                    break
    else:
        if len(st)==0:
            print("balanced")
        else:
            print("not balanced")
bal()

                    