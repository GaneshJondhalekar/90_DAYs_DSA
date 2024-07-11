
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
    
l=[18,48,30,15]
result=l[0]
for i in l[1:]:
    result=gcd(result,i)
print(result)