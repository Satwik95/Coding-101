level_sum = [4,1,2,3]
dp = [0]*len(level_sum)
dp[0] = level_sum[0]
dp[1] = level_sum[1]

for i in range(2, len(level_sum)):
    dp[i] = max(dp[i-2]+level_sum[i], dp[i-1])
print(dp[-1])
