def ladder(n):
    if n==0:
        return 1
    elif dp[n]!=0:
        return dp[n]
    else:
        for i in [1,2,3]:
            if n-i>=0:
                dp[n] += ladder(n-i)
        return dp[n]
n=4
dp = [0]*(n+1)
ladder(n)
