'''
Count no of digits in x
Input: x=1989
Output: 4
Input: x=45
Output: 
'''
x=int(input("Enter No"))
n=0
while x>0:
    x=x//10
    n+=1
print(n)