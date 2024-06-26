
s = "aabccoccaacc"

count=1
compressed=[]

for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count+=1
    else:
        compressed.append(s[i])
        compressed.append(str(count))
        count=1
compressed.append(s[-1])
compressed.append(str(count))
print(''.join(compressed))