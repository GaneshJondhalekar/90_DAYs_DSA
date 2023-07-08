def Is_safe(board,col,row,n):
    #check in current row
    if 'Q' in board[row]:
        return False

    # Check the upper diagonal
    row1= row -1
    col1 = col -1
    while row1 >= 0 and col1 >= 0:
        if board[row1][col1] == 'Q':
            return False
        row1 -= 1
        col1 -= 1

    

    # Check the lower diagonal
    col-=1
    row+=1
    while col >= 0 and row < n:
        if board[row][col] == 'Q':
            return False
        col -= 1
        row += 1

    return True

def Solve(board,col,n,result):
    if col==n:
        result.append([row[:] for row in board])
        return
    
    for row in range(0,n):
        if Is_safe(board,col,row,n):
            board[row][col]='Q'
            Solve(board,col+1,n,result)
            board[row][col]='_'
    return result

n=8
board=[[] for _ in range(n)]

for row in range(n):
    for col in range(n):
        board[row].append('_')
print(Solve(board,0,n,[]))

    



