'''
Count frequency of characters
'''

s="Hello world!"

d={}
for i in s:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
print(d)

