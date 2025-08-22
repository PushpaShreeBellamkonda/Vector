def reverse():
    s=input()
    st=[]
    for i in s:
        st.append(i)
    rev=""
    while len(st)>0:
        rev=rev+st.pop()
    return rev
print(reverse())
