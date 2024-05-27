'''
Matrix addition can only be performed if both matrices have the same dimensions.
'''

mat1=[]
for i in range(4):
    l=list(map(int,input().split(" ")))
    mat1.append(l)
    
mat2=[]
for i in range(4):
    l=list(map(int,input().split(" ")))
    mat2.append(l)
   
result=[[0]*4 for _ in range(4)]

for i in range(4):
    for j in range(4):
        result[i][j]=mat1[i][j]+mat2[i][j]
        
print(result)