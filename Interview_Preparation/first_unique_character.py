'''
Write a function to find the first non-repeating character in a string and return its index. If it doesn't exist, return -1
'''

s = "leetcodel"
for i,v in enumerate(s):
    if v not in s[i+1:]:
        print(i,v)
        break
else:
    print("Not unique character available")

'''
s = "leetcodel"
d={}
for i in s:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1

for i,v in enumerate(s):
    if d[v]==1:
        print(i,v)
        break
'''