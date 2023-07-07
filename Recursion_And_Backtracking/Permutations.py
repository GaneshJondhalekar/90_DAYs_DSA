
def Permutations(arr,inx,l,result):
    if len(l)==len(arr):
        result.append(l[:])
        return
    
    for i in range(len(arr)):
        if arr[i] in l:
            continue
        l.append(arr[i])
        Permutations(arr,i+1,l,result)
        l.remove(arr[i])
    return result
arr=[1,2,3]
n=3
print(Permutations(arr,0,[],[]))