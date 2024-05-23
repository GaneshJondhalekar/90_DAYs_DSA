"""
Merge two sorted lists 
"""

l=[1,34,45,46]
s=[2,3,56,78,90]
r=[]
st=ed=0
while st<len(l) and ed<len(s):
    if l[st]<=s[ed]:
        r.append(l[st])
        st+=1
    else:
        r.append(s[ed])
        ed+=1
#copy remaining elements         
r+=l[st:]
r+=s[ed:]
print(r)
        