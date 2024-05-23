'''Print number 1 to N without using plus operator'''

def Sum(i,n):
    if i<1:
        return
    Sum(i-1,n)
    print(i)#here we print after recursive call means this will execute at last function call means Sum(1) this is backtracking
Sum(5,5)
