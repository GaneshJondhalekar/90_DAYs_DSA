'''
find the third largest number in a list without importing any modules and without using nested loops
'''
l=[12,34,2,56,74,90,34,78]
first=second=float('-inf')

for num in l:
    if num>first:
        second=first
        first=num
    elif num>second:
        second=num
   
print(first,second)
