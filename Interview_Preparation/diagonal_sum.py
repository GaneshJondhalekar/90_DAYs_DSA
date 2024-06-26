matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
s=0
n=len(matrix)
for i in range(n):
    s+=matrix[i][i]
    j=n-1-i
    if i!=j:
        s+=matrix[i][j]
print(s)