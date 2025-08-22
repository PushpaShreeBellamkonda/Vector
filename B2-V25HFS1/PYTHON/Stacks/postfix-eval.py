def postfix():
    st=[]
    s=input()
    for i in s:
        if i.isdigit():
            st.append(int(i))
        else:
            b=st.pop()
            a=st.pop()
            match i :
                case '+':
                    r=a+b
                case '-':
                    r=a-b
                case '*':
                    r=a*b
                case'/':
                    r=a/b
                case '%':
                    r=a%b
            st.append(r)
    print(st[-1])
postfix()
