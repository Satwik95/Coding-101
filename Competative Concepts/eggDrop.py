import sys
def eggDrop(eggs,floors):
    dp=[[0 for x in range(floors+1)]for y in range(eggs+1)]
    for i in range(floors+1):
        dp[1][i]=i
    for i in range(2,eggs+1):
        for j in range(1,floors+1):
            dp[i][j]=sys.maxsize
            for k in range(1,j+1):
                cur=1+(max(dp[i-1][k-1],dp[i][j-k]))
                dp[i][j]=min(dp[i][j],cur)
    
    return dp[eggs][floors]

print(eggDrop(1,36))
