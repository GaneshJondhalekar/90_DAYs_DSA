'''
find the third largest number in a list without importing any modules and without using nested loops
'''

l=[12,34,2,56,74,90,34,78]
first=second=third=float('-inf')

for num in l:
    if num>first:
        third=second
        second=first
        first=num
    elif num>second:
        third=second
        second=num
    elif num>third:
        third=num

print(first,second,third)