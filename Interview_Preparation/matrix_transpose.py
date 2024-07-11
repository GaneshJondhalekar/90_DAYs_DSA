matrix = [
    [1, 2],
    [4, 5],
    [7, 8]
]

row=len(matrix)
col=len(matrix[0])
l=[]

for i in range(col):
    k=[]
    for j in range(row):
        
        k.append(matrix[j][i])
    l.append(k)
print(l)