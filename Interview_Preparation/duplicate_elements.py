'''
Write a function that finds all elements that appear twice in a list of integers 
where 1 ≤ a[i] ≤ n (n = size of the list). Return a list of these duplicate numbers.
'''

nums = [4,3,2,7,8,2,3,1]
l=[]
d=[]
for i in nums:
    if i not in l:
        l.append(i)
    else:
        d.append(i)
print(d)
