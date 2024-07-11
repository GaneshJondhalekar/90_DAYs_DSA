matrix = [
    [1, 2, 3],
    [4, 15, 6],
    [7, 8, 9]
]

max_e=float('-inf')

for row in matrix:
    for e in row:
        if e>max_e:
            max_e=e
print(max_e)s