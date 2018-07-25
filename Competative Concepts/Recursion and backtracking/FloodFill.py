import sys
sys.setrecursionlimit(1500)

#W,N,E,S
dx = [0,-1,0,+1]
dy = [-1,0+1,0]

def FloodFill(board,i,j,ch,color):
    #base for the matrix
    if i<0 or j<0 or i>=R or j>=C:
        return
    #hidden boundary condition
    if board[i][j]==ch:
        #fill color
        board[i][j]=color
        for k in range(0,4):
            return FloodFill(board,i+dx[k],j+dy[k],ch,color)

if __name__=="__main__":
    R=int(input())
    C=int(input())
    board = [[input() for x in range(C)] for y in range(R)]
    print(board)
    FloodFill(board,1,1,'2','$')
    print(board)
