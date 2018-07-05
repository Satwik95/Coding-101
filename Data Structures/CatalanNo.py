dp = [0]*100

def catalan(n):
    if n==0: return 1
    if dp[n]!=0:
        return dp[n]
    ans = 0
    for i in range(1,n+1):
        ans+=catalan(i-1)*catalan(n-i)
    dp[n] = ans #if computed for the first time
    return ans

print(catalan(3))
