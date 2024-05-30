s="Hello Ganesh"
s="ama"
if s==s[::-1]:
    print("Pallindrom")
else:
    print("Not")
    
#Logic 2
n=len(s)
c=1
for i in range(n//2):
    if s[i]!=s[n-i-1]:
        c=0
        break
if c:
    print("Pallendrom")
else:
    print("not")