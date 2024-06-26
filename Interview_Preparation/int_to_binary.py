n=10
s=[]
while n>0:
    r=n%2
    s.append(r)
    n=n//2
s.reverse()
print(''.join(str(i) for i in s))