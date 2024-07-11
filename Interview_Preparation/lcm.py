'''
gcd(a,b)*lcm(a,b)=a*b
'''
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
        
a=48
b=18
lcm=(a*b)//gcd(a,b)
print(lcm)