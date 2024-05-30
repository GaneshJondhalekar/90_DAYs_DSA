'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, 
return the index where it would be if it were inserted in order
'''
def search(nums,target):
    left = 0
    right = len(nums) - 1
    while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return 'found at {}'.format(mid)
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    
        # The target was not found, so left is the index where it should be inserted
    return left
        
nums=[12,33,56,78,90,123]
print(search(nums,39))