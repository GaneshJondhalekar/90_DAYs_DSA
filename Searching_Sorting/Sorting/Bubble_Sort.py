def Bubble(arr):
    for passes in range(len(arr)-1):
        for i in range(len(arr)-passes-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr
arr=[23,1,34,5,78,9,6,0,90]
print(Bubble(arr))