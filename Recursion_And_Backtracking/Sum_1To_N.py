def SumN(i,n,s):
    if i>n:
        return s
    s+=i
    return SumN(i+1,n,s)
print(SumN(1,2,0))