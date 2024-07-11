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