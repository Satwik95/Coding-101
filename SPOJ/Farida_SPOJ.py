import collections

def maxCoins(count,nums,n):
        if n==1:
                return nums[0]
        dp = [0]*(n+1)
        for i in range(1,n+1): 
                dp[i]=max((i*count[i])+dp[i-2],dp[i-1])
        return dp[n]

if __name__=="__main__":
        cases = int(input())
        i=1
        result = []
        while i<=cases:
                n = int(input())
                nums = list(map(int, input().split(" ")))
                count = collections.Counter(nums)
                result.append(maxCoins(count,nums,n))
                i+=1
        for i in range(0,cases):
                print("Case "+str(i+1)+":",result[i])
