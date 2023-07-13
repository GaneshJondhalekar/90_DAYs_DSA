
def Is_Safe(row,col,board,k,n):

    #row
    row1=row-1
    while row1!=-1:
        if board[row1][col]=='E':
            if board[row1][row1]==k:
                return False
        row1-=1
    
    #column
    col-=1
    while col!=-1:
        if board[row][col]=='E':
            if board[col][col]==k:
                return False
        col-=1
    return True

def Solve(row,col,board,n,colors):
    if row==n:
        return True
    for i in range(colors):
       
        #print(i,Is_Safe(row,col,board,i,n))
        if Is_Safe(row,col,board,i,n):
            board[row][col]=i
            break
        else:
            if i==colors-1:
                return False
    result=Solve(row+1,col+1,board,n,colors)
    return result

colors=3
n=4
edges=4
s={(1,2),(2,3),(3,4),(4,1),(3,1)}
board=[[' ']*n for _ in range(n)]
for e in s:
    board[e[0]-1][e[1]-1]='E'
print(board)
print(Solve(0,0,board,n,colors))
print(board)



