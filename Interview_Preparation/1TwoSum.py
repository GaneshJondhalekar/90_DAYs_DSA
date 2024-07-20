'''
Input=[2,7,11,15] target=9
		output=[0,1] if target=13 then [0,2]
		Input=[3,4,2] target=6
		output=[1,2]
		Input=[3,3] target=6
		output=[0,1]

'''
def index_of_num(nums):
    d={}
    for i,k in enumerate(nums):
        d[k]=i
    return d


nums = [2, 7, 11, 15] 
target = 9
nums=[3,4,2]
target=6
nums=[3,3]
target=6
r=[]
for k,i in enumerate(nums):
    s=target-i
    d=index_of_num(nums)
    print(d)
    j=d[s]
   
    if s in nums and j!=k:
        r.append(k)
        r.append(j)
        break

print(r)