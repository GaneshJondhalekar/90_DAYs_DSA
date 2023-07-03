def Sum(i,n):
    if i>n:
        return
    print(i)
    Sum(i+1,n)
Sum(1,5)