def paths(i,j):
    if i==end[0] and j=end[1]:
        return 1
    else if maze[i][j]=="t":
        return 0
    else if i<0 or j<0:
        return 0
    else if i>m or j>n:
        return 0
    if dp[i][j]!=0:
        return dp[i][j]
    # if end is above start
    if end[0]<start[0]:              #up           left           right
        dp[i][j] = min(dp[i][j], paths(i-1,j) + paths(i,j-1) + paths(i,j+1))
    else if end[0]==start[0]:#same level
        dp[i][j] = min(dp[i][j], paths(i,j-1) + paths(i,j+1))
    else:                            #down         left           right
        dp[i][j] = min(dp[i][j], paths(i+1,j) + paths(i,j-1) + paths(i,j+1))
    return 1
