def Reverse(arr,start,end):
    if start>=end:
        return
    arr[start],arr[end]=arr[end],arr[start]
    Reverse(arr,start+1,end-1)
arr=[11,2,3,4,10]
Reverse(arr,0,len(arr)-1)
print(arr)