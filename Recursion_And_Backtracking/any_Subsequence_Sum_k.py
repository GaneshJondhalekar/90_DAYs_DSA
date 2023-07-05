#Print any subsequence having sum equal to k
def Any_Sum_K(arr,inx,k,s,l,result):
    if inx>=len(arr):
        if s==k:
            result.append(l[:])
            return True
        return False
    s+=arr[inx]
    l.append(arr[inx])
    if Any_Sum_K(arr,inx+1,k,s,l,result):
        return True
    s-=arr[inx]
    l.remove(arr[inx])
    if Any_Sum_K(arr,inx+1,k,s,l,result):
        return True
    return False

arr=[1,2,3,4]
k=3
result=[]
Any_Sum_K(arr,0,k,0,[],result)
print(result)
        