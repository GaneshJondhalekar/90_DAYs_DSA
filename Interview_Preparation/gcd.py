def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
        
a=48
b=18
print(gcd(a,b))

'''
def gcd(a,b):
    k=min(a,b)
    for i in range(k,0,-1):
        if a%i==0 and b%i==0:
           return i
           
    else:
        return None
        
a=48
b=18
print(gcd()a,b)
'''