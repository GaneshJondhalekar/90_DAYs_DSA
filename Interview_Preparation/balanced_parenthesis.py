op=['{','[','(']
cl=['}',']',')']
d={'}':'{',']':'[',')':'('}
s='{}[]({)'
s1='[{()}]'
st=[]
for i in s1:
    if i in op:
        st.append(i)
    else:
        if len(st)==0 or st[-1]!=d[i]:
            print("not Balanced")
            break
        else:
            st.pop()
else:
    print("balanced")