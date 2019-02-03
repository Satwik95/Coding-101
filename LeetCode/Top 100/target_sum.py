class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dp = [[-1 for j in range(2000) ]for i in range(len(nums))]
        def helper(cur_sum, nums, s, pos):
            if len(nums)==0:
                if cur_sum - 1000 == s:
                    return 1
                else:
                    return 0
            if dp[pos][cur_sum]!=-1:
                return dp[pos][cur_sum]
            else:
                dp[pos][cur_sum] = helper(cur_sum+nums[0], nums[1:], s, pos+1) + helper(cur_sum-nums[0], nums[1:], s, pos+1)
            return dp[pos][cur_sum]
        
        return helper(1000, nums, S, 0)