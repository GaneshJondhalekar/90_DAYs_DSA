l=[12,-3,4,-30,5,-1,8]

cur_sum=0
max_sum=float('-inf')
start=end=s=0
for i,num in enumerate(l):
    if num >cur_sum+num:
        cur_sum=num
        s=i
    else:
        cur_sum+=num
       
    if cur_sum>max_sum:
        max_sum=cur_sum
        start=s
        end=i
        
print(max_sum,l[start:end+1])