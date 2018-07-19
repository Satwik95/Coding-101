import math
import sys
sys.setrecursionlimit(1500)
def canPlace(board,i,j,n,number):
    #for col and row
    for x in range(0,n):
        if board[i][x]==number or board[x][j]==number:
            return False
    #for sub_square
    rn = int(math.sqrt(n))
    si = int((i/rn))*rn
    sj = int((j/rn))*rn
    for i in range(si,si+rn):
        for j in range(sj,sj+rn):
            if board[i][j]==number:
                return False
    return True

def sudoku(board,i,j,n):
    #base case, jab n rows ke liye fill ho gaya hai
    if i==n:
        for i in range(0,n):
            for j in range(0,n):
                print(board[i][j],end="|")
            print("")
            print("------------------")
        return True
    #going to next row
    if j==n:
        sudoku(board,i+1,0,n)
    #pre filled case
    if board[i][j]!=0:
        return sudoku(board,i,j+1,n)
    #rec case
    for number in range(1,n+1):
        #print(i,j,number)
        if canPlace(board,i,j,n,number):
            board[i][j]=number
            subProblem = sudoku(board,i,j+1,n)
            if subProblem:
                return True
    #backtrack
    board[i][j]=0
    return False
                    
board=[[5,3,0,0,7,0,0,0,0],
       [6,0,0,1,9,5,0,0,0],
       [0,9,8,0,0,0,0,6,0],
       [8,0,0,0,6,0,0,0,3],
       [4,0,0,8,0,3,0,0,1],
       [7,0,0,0,2,0,0,0,6],
       [0,6,0,0,0,0,2,8,0],
       [0,0,0,4,1,9,0,0,5],
       [0,0,0,0,8,0,0,7,9]]
sudoku(board,0,0,9)
