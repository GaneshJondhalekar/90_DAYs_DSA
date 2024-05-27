col1=int(input("Enter no of col of 1st matrix"))
row1=int(input("Enter no of col of 1st matrix"))
col2=int(input("Enter no of col of 2nd matrix"))
row2=int(input("Enter no of col of 2nd matrix"))

if col1 != row2:
    print("Matrix multiplication is not possible. The number of columns in the first matrix must be equal to the number of rows in the second matrix.")
else:
    mat1=[]
    for i in range(row1):
        l=list(map(int,input().split(" ")))
        mat1.append(l)
        
    mat2=[]
    for i in range(row2):
        l=list(map(int,input().split(" ")))
        mat2.append(l)
       
    result=[[0]*col2 for _ in range(row1)]
    
    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                result[i][j]+=mat1[i][k]*mat2[k][j]
            
    print(result)