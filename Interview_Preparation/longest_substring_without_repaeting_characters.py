s = "abcabcdeebb"

r=[]
for i,v in enumerate(s):
    l=[v]
    for j in s[i+1:]:
        if j not in l:
            l.append(j)
        else:
            r.append(len(l))
print(max(r))

'''
s="subksusnud"
d={}
start=0
longest=0
lon_str=""

for i,v in enumerate(s):
    if v in d and d[v]>=start:
        start=d[v]+1
    d[v]=i
    if i-start+1 > longest:
        longest=i-start+1
        lon_str=s[start:i+1]
print(lon_str)
        
'''


