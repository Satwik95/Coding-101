nums = []
dp = [[-1 for x in range(1000)]for y in range(1000)]
import sys
def custsum(s,e):
    res=0
    for i in range(s,e):
            res+=nums[i]
            res%=100
    return res

def minSmoke(i,j):
    #base case
    if i>=j:#single element
        return 0
    #if answer already completed
    if dp[i][j]!=-1:
        return dp[i][j]
    
    dp[i][j]=sys.maxsize
    for k in range(i,j):
        dp[i][j]=min(dp[i][j],minSmoke(i,k)+minSmoke(k+1,j)+custsum(i,k)*custsum(k+1,j))

    return dp[i][j]

if __name__=="__main__":
    n=int(input())
    for i in range(0,n):
        nums.append(int(input()))
    print(minSmoke(0,n-1))
