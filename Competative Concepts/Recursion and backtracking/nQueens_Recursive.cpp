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
        //on return false in the base case, ill be getting all the possible configs
        //return false;
    }
    //for every initial pos of queen in the first row there is a different valid config
    //in the first function call we are actually checking for the first row,and the recursively going to the next row
    //EXIT condition, if row=n, which means in one of the recursive call all the queens are placed, now this final rec fn will return true to 
    //return statement stops execution and returns to the calling function
    //so for n-1 rows ho gaya toh 1st ke liye true return hoga
    //agar nahi hua toh i.e false return hua, toh j will increment and so on if the entire loop runs n2time for the first function call
    //hence no valid config at all
    //but in this code I am only priniting one form of config, how to find all forms of config?
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
