'''Write a function to find the smallest positive integer that is missing from a list of integers without using nested loops or 
any imported modules. The list can contain both positive and negative integers.'''

l=[3,4,-1,1]
l.sort()
for i in range(len(l)-1):
    if abs(l[i]-l[i-1])>=2 :
        if l[i]+1>0:
            print(l[i]+1)
            break
'''
if sort() is not allowed
'''
l=[3,4,-1,1,-3]
m=l[0]
mx=l[0]
for i in l[1:]:
    if i<m:
        m=i
    if i>mx:
        mx=i
        
for i in range(m,mx+1,1):
    if i not in l and i>0: 
        print(i)
        break