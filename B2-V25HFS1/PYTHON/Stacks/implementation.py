def stack():
    st=[]
    while True:
        print("1.push 2.pop 3.peek 4.exit")
        ch=int(input())
        match ch:
            case 1:
                st.append(int(input()))
            case 2:
                if len(st)==0:
                    print("stack is underflow")
                else:
                    print(st.pop())
            case 3:
                if len(st)==0:
                    print("stack is empty")
                else:
                    print(st[-1])
            case _:
                break
stack() 