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

def f(n):
    if n==1:
        return 0
    if dp[n]!=0:
        return dp[n]
    dp[n] = 1+f(n-1)
    if n%3==0:
        dp[n]=min(dp[n],1+f(int(n/3)))
    if n%2==0:
        dp[n]=min(dp[n],1+f(int(n/2)))
    return dp[n]

if __name__=='__main__':        
    n=10
    dp = [0]*(n+1)
    print(min_steps_to_one(n))
                
