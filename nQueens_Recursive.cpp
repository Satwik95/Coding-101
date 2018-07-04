#include <iostream>

using namespace std;

bool isSafe(int board[][10],int row,int col,int n)
{
    //check for the same column
    int i = row;
    while(i>=0){
        if(board[i][col]==1){
            return false;
        }
        i--;
    }
    //check for left dig
    int x = row;
    int y = col;
    while(x>=0 && y>=0)
    {
        if(board[x][y]==1){
            return false;
        }
        x--;
        y--;
    }
    //check for right dig
    x = row;
    y = col;
    while(x>=0 && y<n)
    {
        if(board[x][y]==1){
            return false;
        }
        x--;
        y++;
    }

    return true;
}
bool nqueens(int board[][10],int row,int n)
{
    if(row==n)
    {
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(board[i][j]==1)
                {
                    cout<<"Q ";
                }
                else
                {
                    cout<<". ";
                }
            }cout<<endl;
        }
        return true;
    }
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            if(isSafe(board,i,j,n)){
                board[i][j]=1;
                bool next_sub_board = nqueens(board,i+1,n);
                if(next_sub_board)
                    return true;//this is for the first row eventually we will return true from here!
            }
        }
    }
    return false;
}

int main()
{
    int board[10][10];
    int n;
    cin>>n;
    
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            board[i][j]=0;
        }
    }
    cout<<nqueens(board,0,n);

    return 0;
}
