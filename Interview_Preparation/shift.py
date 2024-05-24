"""
Shift s elements to  right or left
"""

def right_shift(s,l):
    n=len(l)
    k=l[n-s:]+l[0:n-s]
    return k
    
l=[1,2,3,4,5,6]
print(right_shift(1,l))

def left_shift(s,l):
    
    k=l[s:]+l[0:s]
    return k
    
l=[1,2,3,4,5,6]
print(left_shift(4,l))