'''
Write a function to find the longest palindromic substring in a given string
'''

def is_palindrom(s):
    #print(s)
    return True if s[::-1]==s else False


s = "babad"
n=len(s)
l=[]
for i in range(n-1):
    for j in range(n-1,i,-1):
        if is_palindrom(s[i:j+1]):
            l.append(s[i:j+1])
mx=len(l[0])
result=l[0]
for ch in l:
    if len(ch)>mx:
        mx=len(ch)
        result=ch
print(result)