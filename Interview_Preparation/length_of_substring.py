'''
Write a function to find the length of the longest substring without repeating characters in a given string.
'''
s='abcbacab'
st=[]
for i in range(len(s)):
    l=[]
    for e in s[i:]:
        
        if e not in l:
            
            l.append(e)
        else:
            st.append(''.join(l))
            break
    else:
        st.append(''.join(l))
print(st)