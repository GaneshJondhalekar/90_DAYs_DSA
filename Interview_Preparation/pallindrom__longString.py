s = "A man, a plan, a canal: Panama"
sp=[';',':','?',' ',',']
s1=[i.upper() for i in s if i not in sp]

for i in range(len(s1)//2):
    if s1[i]==s1[len(s1)-1-i]:
        continue
    else:
        print(False)
        break
else:
    print(True)