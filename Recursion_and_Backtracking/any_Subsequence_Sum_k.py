# Print any subsequence having sum k
def Any_Sum_K(inx,arr,s,sum1,l):
    if inx>=len(arr):
        if s==sum1:
            print(l)
            return True
        return False
    s+=arr[inx]
    l.append(arr[inx])
    if Any_Sum_K(inx+1,arr,s,sum1,l)==True:
        return True
    s-=arr[inx]
    l.remove(arr[inx])
    if Any_Sum_K(inx+1,arr,s,sum1,l)==True:
        return True
    return False
    
arr=[1,2,3,4]
Any_Sum_K(0,arr,0,5,[])