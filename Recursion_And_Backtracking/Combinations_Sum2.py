
def Combinations(inx,arr,target,l,result):
    if inx>=len(arr):
        if target==0:
            result.append(l[:])
        return
    
    for i in range(len(arr)):

        if arr[inx]<=target:
            l.append(arr[inx])
            target-=arr[inx]
            Combinations(inx+1,arr,target,l,result)
            l.remove(arr[inx])
            target+=arr[inx]
            Combinations(inx+1,arr,target,l,result)
        else:
            return 