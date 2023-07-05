#Print 1 to  N numbers without using plus
def Print(i,n):
    if i<=0:
        return 
    Print(i-1,n) #here we call print recursively and it will return when i ==0 so we backtrack and print reversly 
    print(i)     #that is F(i=1,n )will print first then f(i=2,n)

Print(5,5)