def Pallindrom(s,start,end):
    if start>=end:
        return True
    if s[start]!=s[end]:
        return False
    return Pallindrom(s,start+1,end-1)
s='adccda'
print(Pallindrom(s,0,len(s)-1))