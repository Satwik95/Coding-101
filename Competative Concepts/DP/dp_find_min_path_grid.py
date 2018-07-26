grid = [[1,2,6],
        [4,8,2],
        [1,5,3]]
#need to reach from 1 to 3 in min cost possible
dp = [[0 for x in range(3)]for y in range(3)]

#dp grid valc
dp[0][0]=grid[0][0]
for i in range(1,3):
    dp[0][i] = dp[0][i-1]+grid[0][i]
    dp[i][0] = dp[i-1][0]+grid[i][0]
#bottom up
for i in range(1,3):
    for j in range(1,3):
        dp[i][j]=min(dp[i][j-1],dp[i-1][j])+grid[i][j]

print("min cost",dp[2][2])
