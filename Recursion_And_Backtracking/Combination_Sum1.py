'''Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.
'''

def Combinations(arr,inx,target,l,result):
    if inx>=len(arr):
        if target==0:
            result.append(l[:])
        return
    if arr[inx]<=target:
        target-=arr[inx]
        l.append(arr[inx])
        Combinations(arr,inx,target,l,result)
        target+=arr[inx]
        l.remove(arr[inx])
    Combinations(arr,inx+1,target,l,result)
    return result
arr=[2,3,5]
target=8
print(Combinations(arr,0,target,[],[]))