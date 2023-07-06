#find subsequences of elements of array having sum k
def Sum_K(arr,inx,l,k,s,result):
    if inx>=len(arr):
        if s==k:
            result.append(l[:])
        return 
    s+=arr[inx]
    l.append(arr[inx])
    Sum_K(arr,inx+1,l,k,s,result)
    s-=arr[inx]
    l.remove(arr[inx])
    Sum_K(arr,inx+1,l,k,s,result)
    return result
arr=[10,1,2,7,6,1,5]
k=8
print(Sum_K(arr,0,[],k,0,[]))