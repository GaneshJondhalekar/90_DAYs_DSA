def selection(arr):
    for i in range(len(arr)-1):
        min=i
        for j in range(i+1,len(arr)):
            if arr[min]>arr[j]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    return arr
arr=[23,1,45,6,12,0,100,1]
print(selection(arr))
            
        