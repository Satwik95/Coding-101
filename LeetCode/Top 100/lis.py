class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        """dp = [1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    
        return max(dp)
        """
        temp = [0]*len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i!=j:
                mid = int((i+j)/2)
                if temp[mid]<x:
                    i = mid + 1
                else:
                    j = mid
            temp[i] = x
            size = max(size, i+1)
        return size