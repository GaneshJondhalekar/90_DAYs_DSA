'''Given a list (Arr) of tintegers, print sums of all subsets in it. 
Output should be printed in increasing order of sums.
Input:
N = 3
Arr = [5, 2, 1] 
Output: 0 1 2 3 5 6 7 8 '''

def Subset(arr,inx,s,result):
    if inx>=len(arr):
        result.append(s)
        return
    s+=arr[inx]
    Subset(arr,inx+1,s,result)
    s-=arr[inx]
    Subset(arr,inx+1,s,result)
    return result
arr=[5,2,1]
result=[]
ans=Subset(arr,0,0,result)
ans.sort()
print(ans)