'''
Here are the basic rules for binary addition:

0 + 0 = 0
0 + 1 = 1
1 + 0 = 1
1 + 1 = 10 (which is 0 with a carry of 1)
'''



'''
a = "1010"
b = "1011"

n=max(len(a),len(b))
a=a.zfill(n)
b=b.zfill(n)
s=[0]*n
carry=0

for i in range(n-1,-1,-1):
    if a[i]=='1' and b[i]=='1':
        s[i]=1 if carry==1 else 0
        carry=1
    if (a[i]=='1' and b[i]=='0')or(a[i]=='0' and b[i]=='1'):
        if carry==1:
            s[i]=0
            carry=1
        else:
            s[i]=1
    if a[i]=='0' and b[i]=='0':
        if carry==1:
            carry=0
            s[i]=1
        else:
            s[i]=0
if carry==1:
    result='1'+"".join(str(i) for i in s)
else:
   result="".join( str(i) for i in s)
  
print(result)
'''
a = "1010"
b = "1011"
n=max(len(a),len(b))
a=a.zfill(n)
b=b.zfill(n)
s=[0]*n
carry=0
for i in range(n-1,-1,-1):
    bit_a=int(a[i])
    bit_b=int(b[i])
    
    result=bit_a+bit_b+carry
    if result==3:
        carry=1
        s[i]=1
    elif result==2:
        carry=1
        s[i]=0
    elif result==1:
        carry=0
        s[i]=1
    else:
        s[i]=0
        carry=0
if carry == 1:
    result = '1' + ''.join(str(bit) for bit in s)
else:
    result = ''.join(str(bit) for bit in s)

print(result) 
