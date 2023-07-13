#solve sudoku n*n having zero/one empty space in each row. we can place number 1 to n.
# Input n=3,board=[[' ',3,2],[3,' ',1],[2,1,' ']]
#Output -board=[[1,3,2],[3,2,1],[2,1,3]]


def Is_Empty(row,col,board):
    if board[row][col]==' ':
        return True
    return False

def Is_Safe(row,col,board,n,k):
    if k in board[row]:
        return False
    row+=1
    while row!=n:
        if board[row][col]==k:
            return False
        row+=1
    return True

def Solve(col,board,n):
    if col==n:
        return
    for row in range(n):
        if Is_Empty(row,col,board):
            for i in range(1,n+1):
                if Is_Safe(row,col,board,n,i):
                    board[row][col]=i
                    Solve(col+1,board,n)

        else:
            Solve(col+1,board,n)
    return board
n=4
board1=[[' ',3,2],[3,' ',1],[2,1,' ']]
board2=[[1,3,' ',4],[2,1,4,' '],[3,4,' ',2],[' ',2,3,1]]
print(Solve(0,board2,n))
