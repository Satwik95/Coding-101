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
        nums = []
        n = []
        j=0
        while i<=cases:
                inp = int(input())
                n.append(inp)
                nums.append([int(x) for x in input().split(" ")])
                i+=1
        for a in n:
                count = collections.Counter(nums[j])
                result.append(maxCoins(count,nums[j],a))
                j+=1
        for i in range(0,cases):
                print("Case "+str(i+1)+": "+str(sresult[i]))
