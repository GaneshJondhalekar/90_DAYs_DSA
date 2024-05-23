def Subsequences(arr,inx,l,result):
    if inx>=len(arr):
        result.append(l[:])#Append a copy of the current subsequence to the result list we can use list(l) alse instead of l[:]
        return             #if we append l directly then it will point to same list l 
                           #that is every list inside result have same address x
    l.append(arr[inx])     #that is every list inside result have same addres
    Subsequences(arr,inx+1,l,result)
    l.remove(arr[inx])
    Subsequences(arr,inx+1,l,result)

arr=[3,2,1]
result=[]
Subsequences(arr,0,[],result)
print(result)