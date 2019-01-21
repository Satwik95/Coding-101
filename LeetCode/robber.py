class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<1:
            return 0
        if len(nums)==1:
            return nums[0]
        dp = [None]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])
            
        return dp[-1]