def editDistance(inp_str,out_str):
    m=len(inp_str)
    n=len(out_str)
    dp = [[0 for x in range(n+1)]for y in range(m+1)]
    for i in range(1,n+1):
        dp[0][i]=1+dp[0][i-1]#insertion
    for i in range(1,m+1):
        dp[i][0]=1+dp[i-1][0]#deletion
    for i in range(1,m+1):
        for j in range(1,n+1):
            on_del=dp[i-1][j]
            on_repl=dp[i-1][j-1]
            on_ins=dp[i][j-1]
            x = 1 if inp_str[i-1]!=out_str[j-1] else 0
            dp[i][j]=min(on_repl,on_del,on_ins)+ x
    return dp[m][n]

if __name__=="__main__":
    inp_str = input()
    out_str = input()
    print(editDistance(inp_str,out_str))
