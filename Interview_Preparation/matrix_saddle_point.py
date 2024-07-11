'''
A saddle point in a matrix is an element which is the smallest in its row and the largest in its column. 
Write a function to find all saddle points in a given 2D array.
'''
matrix = [
    [7, 8, 9],
    [5, 3, 7],
    [1, 2, 3]
]

col=len(matrix[0])
row=len(matrix)
c,r=0,0
for i in range(row):
    lx=matrix[i][0]
    mx=float('-inf')
    for j in range(col):
        if lx>matrix[i][j]:
            lx=matrix[i][j]
            r=i
            c=j
    for k in range(row):
        if mx<matrix[k][i]:
            mx=matrix[k][i]
            r=k
            c=i
    if lx==mx:
        break

if lx==mx:
    print(f'{lx},({r},{c})')
else:
    print("No such element")