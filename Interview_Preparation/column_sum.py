matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10,11,12]
]
s=0
l=[]

col=len(matrix[0])
row=len(matrix)

for i in range(col):
    s=0
    for j in range(row):
        s+=matrix[j][i]
    l.append(s)
print(l)