'''
Write a function to find the contiguous subarray within a list of integers which has the largest product.
'''
nums = [2,-3,2,4]

max_product=0
cur_product=1
start=end=s=0
for i,num in enumerate(nums):
    if cur_product*num<num:
        cur_product=num
        s=i
    else:
        cur_product*=num
    
    if max_product<cur_product:
        max_product=cur_product
        start=s
        end=i
print(max_product,print(nums[start:end+1]))
