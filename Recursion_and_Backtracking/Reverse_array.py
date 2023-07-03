def ReverseList(l,start,end):
    if start>=end:
        return l
    l[start],l[end]=l[end],l[start]
    return ReverseList(l,start+1,end-1)

l=[5,4,3,2,0]
print(ReverseList(l,0,len(l)-1))