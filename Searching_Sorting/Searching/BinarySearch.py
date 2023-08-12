
def BinarySearch(arr,target,start,end):
    if start>end:
        return 'No target Found'
    mid=(start+end)//2
    if target==arr[mid]:
        return mid
    if target<arr[mid]:
        return BinarySearch(arr,target,start,mid-1)
    return BinarySearch(arr,target,mid+1,end)

arr=[23,45,67,89,90]
arr.sort()
print(BinarySearch(arr,89,0,len(arr)))
print(BinarySearch(arr,80,0,len(arr)))
print(BinarySearch(arr,23,0,len(arr)))