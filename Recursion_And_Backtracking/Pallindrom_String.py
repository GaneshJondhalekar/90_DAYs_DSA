def Pallindrom(s,inx):
    if inx>=len(s)//2:
        return True
    if s[inx]==s[len(s)-inx-1]:
        return Pallindrom(s,inx+1)
    else:
        return False
print(Pallindrom('kmdamk',0))