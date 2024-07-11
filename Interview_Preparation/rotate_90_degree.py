'''
Input:   
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

output:
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]


'''

matrix = [
    [1, 2],
    [4, 5],
    [7, 8]
]

row=len(matrix)
col=len(matrix[0])
l=[[0 for _ in range(row)] for i in range(col)]
print(l)
j=0
for rows in matrix[::-1]:
    
    for i,el in enumerate(rows):
        l[i][j]=el
    j+=1
print(l)