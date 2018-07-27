import sys
sys.setrecursionlimit(10000)

def isSafe(board,i,j):
    #check for column
    for row in range(0,n):
        if board[row][j]==1:
            return False
    #check for left diagonal
    row=i
    col=j
    while row>=0 and col>=0:
        if board[row][col]==1:
            return False
        row-=1
        col-=1
    #check for right diagonal
    row=i
    col=j
    while row>=0 and col>=0:
        if board[row][col]==1:
            return False
        row-=1
        col+=1

    return True

def nqueens(board,i,n):
    if i==n-1:
        for i in range(0,n):
            for j in range(0,n):
                if board[i][j]==1:
                    print("Q ",end = "")
                else:
                    print(". ",end="")
            print("\n")
        #return false will work for all the configs!
        return True

    for i in range(0,n):
        for j in range(0,n):
            if isSafe(board,i,j):
                #if safe place the queen
                board[i][j] = 1
                nextQueen = nqueens(board,i+1,n)
                #now while backtracking, if there is any i,j where it returns false,
                #it will set the board[i][j]=0, and go back, and start again from that point
                if nextQueen:
                    return True
            board[i][j]=0

    return False

n=int(input())
board = [[0 for x in range(n)] for y in range(n)]
print(nqueens(board,0,n))
