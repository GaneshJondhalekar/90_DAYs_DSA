'''
Write a function that performs basic string compression using the counts of repeated characters. 
For example, the string "aabcccccaaa" should become "a2b1c5a3". 

'''
s="aabcccdd"
d={}
for i in s:
    d[i]=d.get(i,0)+1

print(d)
ans=''
for key,value in d.items():
    ans+=key+str(value)
print(ans)