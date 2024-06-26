'''
Write a function that removes duplicates in-place from a sorted list of integers and returns the new length of the list.
 The relative order of the elements should be kept the same

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]

'''

nums = [0,0,1,1,1,2,2,3,3,4]

d={}
for i in nums:
    if i in d.keys():
        d[i]=d[i]+1
    else:
        d[i]=1

for i,v in d.items():
    v=v-1
    while v:
        nums.remove(i)
        nums.append('_')
        v-=1
print(nums)