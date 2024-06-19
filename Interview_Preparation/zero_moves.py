'''
Write a function that takes a list of integers and moves all the zeroes 
to the end while maintaining the relative order of the non-zero elements.
'''
nums = [0, 1, 0, 3, 12]
zero_count=0
for i,v in enumerate(nums):
    if v==0:
        nums.pop(i)
        zero_count+=1
        
for i in range(zero_count):
    nums.append(0)
print(nums)