'''
To find the maximum difference between any two elements in a list such that 
the larger element comes after the smaller one without using nested loops or any imported modules
'''
l=[12,34,2,56,74,90,34,78]
min_element=l[0]
max_diff=float('-inf')

for num in l:
    diff=num-min_element
    if diff>max_diff:
        max_diff=diff
    if num<min_element:
        min_element=num
        
print(f"max_difference: {max_diff}")