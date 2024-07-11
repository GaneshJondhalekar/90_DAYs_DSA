'''
Write a function that performs basic string compression using the counts of repeated characters. 
For example, the string "aabcccccaaa" should become "a2b1c5a3". 

'''
s="aaabcccddaa"
n=len(s)
count=1
compressed=''
for i in range(1,n):
    if s[i]==s[i-1]:
        count+=1
    else:
        compressed+=s[i-1]+str(count)
        count=1
compressed+=s[-1]+str(count)
print(compressed)
