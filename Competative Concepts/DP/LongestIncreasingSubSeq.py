def LIS(nums):
    dp=[1]*len(nums)
    best=-1
    for i in range(1,len(nums)):
        for j in range(0,i):
            if nums[j]<=nums[i] and dp[i]<dp[j]+1:
                dp[i]=dp[j]+1
        best=max(best,dp[i])
    return dp,best
if __name__=="__main__":
    nums=[]
    print("Enter the numbers")
    nums = [x for x in input().split(" ")]
    print(LIS(nums))
