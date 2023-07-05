def Subsequences(arr,inx,l,result):
    if inx>=len(arr):
        result.append(l[:])
        return result
    l.append(arr[inx])
    Subsequences(arr,inx+1,l,result)
    l.remove(arr[inx])
    Subsequences(arr,inx+1,l,result)
    return result
arr=[3,2,1]
print(Subsequences(arr,0,[],[]))