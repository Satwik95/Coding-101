import sys
def min_steps_to_one(n):
    dp = [0]*(n+1)
    dp[2]=1
    for i in range(3,n+1):
        res = sys.maxsize
        res = min(res,dp[i-1]+1)
        if i%2==0:
            res = min(res,dp[int(i/2)]+1)
        elif i%3==0:
            res = min(res,dp[int(i/3)]+1)
        dp[i]=res
    return dp[n]

print(min_steps_to_one(10))
            
