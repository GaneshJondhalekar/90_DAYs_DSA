
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
s=0
l=[]
for i in matrix:
    s=0
    for j in i:
        s+=j
    l.append(s)
print(l)

'''
time complexity for both will same O(n*m)
row_sums = [sum(row) for row in matrix]

print(row_sums)
'''