'''
Matrix Transpose
'''

mat=[]
row=3
for i in range(row):
    l=list(map(int,input().split(' ')))
    mat.append(l)
    

c=len(mat[0])

r=[[] for i in range(c)]

for i in mat:
    for index,value in enumerate(i):
        r[index].append(value)
        
print(r)
        