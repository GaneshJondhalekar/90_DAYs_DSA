#print all sunsequences of list having sum k
def Sum_k(arr,inx,l,s,sum1,result):
    if inx>=len(arr):
        if s==sum1:
            result.append(l[:])
        return
    s+=arr[inx]
    l.append(arr[inx])
    Sum_k(arr,inx+1,l,s,sum1,result)
    s-=arr[inx]
    l.remove(arr[inx])
    Sum_k(arr,inx+1,l,s,sum1,result)

arr=[1,2,3,4]
result=[]
Sum_k(arr,0,[],0,5,result)
print(result)