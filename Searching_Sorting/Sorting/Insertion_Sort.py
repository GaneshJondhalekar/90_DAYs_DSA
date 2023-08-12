def Insertion(arr):
    for i in range(1,len(arr)):
        for j in range(i-1,-1,-1):
            if arr[i]<arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
                i-=1
    return arr
arr=[0,18,10,19,1,5,100,3]
print(Insertion(arr))