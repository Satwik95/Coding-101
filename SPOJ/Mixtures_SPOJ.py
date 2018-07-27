import sys

def custsum(nums,s,e):
    res=0
    for i in range(s,e+1):
            res+=nums[i]
            res%=100
    return res

def minSmoke(nums,i,j):
    #base case
    if i>=j:#single element
        return 0
    #if answer already completed
    if dp[i][j]!=-1:
        return dp[i][j]
    #rec case, break exp at every val of k
    dp[i][j]=sys.maxsize
    for k in range(i,j+1):
        dp[i][j]=min(dp[i][j],minSmoke(nums,i,k)+minSmoke(nums,k+1,j)+(custsum(nums,i,k)*custsum(nums,k+1,j)))

    return dp[i][j]

if __name__=="__main__":
import sys

def custsum(nums,s,e):
    res=0
    for i in range(s,e+1):
            res+=nums[i]
            res%=100
    return res

def minSmoke(nums,i,j):
    #base case
    if i>=j:#single element
        return 0
    #if answer already completed
    if dp[i][j]!=-1:
        return dp[i][j]
    #rec case, break exp at every val of k
    dp[i][j]=sys.maxsize
    for k in range(i,j+1):
        dp[i][j]=min(dp[i][j],minSmoke(nums,i,k)+minSmoke(nums,k+1,j)+(custsum(nums,i,k)*custsum(nums,k+1,j)))

    return dp[i][j]

if __name__=="__main__":
    result=[]
    nums = []
    n=[]
    i=j=0
    try:
        while True:
            inp = input()
            if not inp:
                break
            n.append(int(inp))
            nums.append([int(x) for x in input().split(" ")])
            j+=1
    except EOFError:
            pass
    for a in n:
        dp = [[-1 for x in range(a)]for y in range(a)]
        result.append(minSmoke(nums[i],0,a-1))
        i+=1
    for x in result:
        print(x)

