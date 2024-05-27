n=31
c=1
for i in range(2,n//2):
    
    if n%i==0:
        c=0
        break

if c:
    print('prime')
else:
    print("not")